"""Generate the grouped bar chart comparing Dr. Jones vs. Dr. Smith success rates."""
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'DejaVu Sans'

bg = '#282a36'
fg = '#f8f8f2'
jones_color = '#8be9fd'
smith_color = '#ff79c6'

categories = ['Low-Risk\nPatients', 'High-Risk\nPatients', 'Overall\n(Combined)']
jones = [90, 70, 86]
smith = [95, 75, 79]

x = np.arange(len(categories))
width = 0.32

fig, ax = plt.subplots(figsize=(9, 5.5), facecolor=bg)
ax.set_facecolor(bg)

bars1 = ax.bar(x - width/2, jones, width, label='Dr. Jones', color=jones_color, edgecolor=bg)
bars2 = ax.bar(x + width/2, smith, width, label='Dr. Smith', color=smith_color, edgecolor=bg)

for bars in (bars1, bars2):
    for b in bars:
        h = b.get_height()
        ax.annotate(f'{h}%', xy=(b.get_x() + b.get_width()/2, h),
                    xytext=(0, 4), textcoords='offset points',
                    ha='center', va='bottom', color=fg, fontsize=12, fontweight='bold')

ax.set_ylabel('Success Rate (%)', color=fg, fontsize=12)
ax.set_ylim(0, 105)
ax.set_xticks(x)
ax.set_xticklabels(categories, color=fg, fontsize=12)
ax.tick_params(axis='y', colors=fg)
ax.legend(facecolor=bg, edgecolor=fg, labelcolor=fg, fontsize=11, loc='upper center', bbox_to_anchor=(0.5, -0.12), ncol=2)

for spine in ax.spines.values():
    spine.set_color(fg)
    spine.set_alpha(0.3)

ax.axvline(x=1.5, color=fg, alpha=0.3, linestyle='--', linewidth=1)

ax.set_title("Dr. Smith Wins Every Subgroup - Yet Loses Overall", color=fg, fontsize=14, fontweight='bold', pad=15)

plt.tight_layout()
plt.savefig('../Images/simpsons_paradox_surgeons.png', dpi=150, facecolor=bg)
print("saved")
