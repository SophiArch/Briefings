"""Generate a side-by-side scatter plot showing within-group trends reversing
in the aggregate.

Left panel: the raw data with no group labels (all grey) — looks like one
downward trend. Right panel: the same data colored by group, revealing three
upward within-group trends while the combined trend still falls (matches the
classic Simpson's Paradox illustration).
"""
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'DejaVu Sans'
np.random.seed(7)

bg = '#282a36'
fg = '#f8f8f2'
grey = '#6272a4'
group_colors = ['#ffb86c', '#ff5555', '#50fa7b']

n_per_group = 26

# Each group is a tight diagonal streak sloping UP-and-right. Cluster origins
# step down-and-right overall, so the aggregate trend reverses to downward.
direction = (0.45, 1.0)
stream_len = 4.5
perp_noise = 0.6

origins = [(0.0, 5.5), (1.8, 1.5), (3.6, -2.5)]
directions = [direction, direction, direction]

group_points = []
all_x, all_y = [], []

for (dx, dy), (ox, oy) in zip(directions, origins):
    norm = np.hypot(dx, dy)
    gux, guy = dx / norm, dy / norm
    px, py = -guy, gux  # perpendicular unit vector

    t = np.random.uniform(0, stream_len, n_per_group)
    jitter = np.random.normal(0, perp_noise, n_per_group)

    x_base = ox + gux * t + px * jitter
    y_base = oy + guy * t + py * jitter

    group_points.append((x_base, y_base))
    all_x.extend(x_base)
    all_y.extend(y_base)

all_x, all_y = np.array(all_x), np.array(all_y)
m_all, b_all = np.polyfit(all_x, all_y, 1)
xs_all = np.linspace(all_x.min(), all_x.max(), 50)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5.5), facecolor=bg)

# --- Left panel: ungrouped, all grey ---
ax1.set_facecolor(bg)
ax1.scatter(all_x, all_y, color=grey, s=55, alpha=0.8, edgecolor=bg, linewidth=0.6, zorder=3)
ax1.plot(xs_all, m_all * xs_all + b_all, color=fg, linewidth=3.5, linestyle='--', zorder=4)
ax1.set_xlabel('X', color=fg, fontsize=12)
ax1.set_ylabel('Y', color=fg, fontsize=12)
ax1.tick_params(axis='both', colors=fg)
for spine in ax1.spines.values():
    spine.set_color(fg)
    spine.set_alpha(0.3)
ax1.set_title("No Groups: Looks Like One Downward Trend", color=fg, fontsize=13, fontweight='bold', pad=12)

# --- Right panel: grouped, colored ---
ax2.set_facecolor(bg)
for i, (x_base, y_base) in enumerate(group_points):
    ax2.scatter(x_base, y_base, color=group_colors[i], s=55, alpha=0.9,
                label=f'Group {i+1}', edgecolor=bg, linewidth=0.6, zorder=3)
    m, b = np.polyfit(x_base, y_base, 1)
    xs = np.linspace(x_base.min(), x_base.max(), 10)
    ax2.plot(xs, m * xs + b, color=group_colors[i], linewidth=3, alpha=0.95, zorder=2)

ax2.plot(xs_all, m_all * xs_all + b_all, color=fg, linewidth=3.5, linestyle='--',
         label='Combined trend', zorder=4)
ax2.set_xlabel('X', color=fg, fontsize=12)
ax2.set_ylabel('Y', color=fg, fontsize=12)
ax2.tick_params(axis='both', colors=fg)
ax2.legend(facecolor=bg, edgecolor=fg, labelcolor=fg, fontsize=10,
           loc='upper center', bbox_to_anchor=(0.5, -0.14), ncol=4)
for spine in ax2.spines.values():
    spine.set_color(fg)
    spine.set_alpha(0.3)
ax2.set_title("Grouped: Each Group Trends Up", color=fg, fontsize=13, fontweight='bold', pad=12)

plt.tight_layout()
plt.savefig('../Images/simpsons_paradox_trend_reversal.png', dpi=150, facecolor=bg)
print("saved")
