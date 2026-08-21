"""Generate the stacked bar chart showing each surgeon's patient risk-mix (the lurking variable)."""
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'DejaVu Sans'

bg = '#282a36'
fg = '#f8f8f2'
low_color = '#50fa7b'
high_color = '#ffb86c'

doctors = ['Dr. Jones', 'Dr. Smith']
low_risk = [80, 20]
high_risk = [20, 80]

fig, ax = plt.subplots(figsize=(8, 5.5), facecolor=bg)
ax.set_facecolor(bg)

bars_low = ax.barh(doctors, low_risk, color=low_color, edgecolor=bg, label='Low-Risk Patients')
bars_high = ax.barh(doctors, high_risk, left=low_risk, color=high_color, edgecolor=bg, label='High-Risk Patients')

for i, (lr, hr) in enumerate(zip(low_risk, high_risk)):
    ax.text(lr/2, i, f'{lr}', ha='center', va='center', color=bg, fontsize=13, fontweight='bold')
    ax.text(lr + hr/2, i, f'{hr}', ha='center', va='center', color=bg, fontsize=13, fontweight='bold')

ax.set_xlabel('Patients (out of 100)', color=fg, fontsize=12)
ax.set_xlim(0, 100)
ax.tick_params(axis='x', colors=fg)
ax.tick_params(axis='y', colors=fg, labelsize=13)
ax.legend(facecolor=bg, edgecolor=fg, labelcolor=fg, fontsize=11, loc='upper center', bbox_to_anchor=(0.5, -0.12), ncol=2)

for spine in ax.spines.values():
    spine.set_color(fg)
    spine.set_alpha(0.3)

ax.set_title("The Lurking Variable: Who Treats Which Patients", color=fg, fontsize=14, fontweight='bold', pad=15)

plt.tight_layout()
plt.savefig('../Images/simpsons_paradox_caseload.png', dpi=150, facecolor=bg)
print("saved")
