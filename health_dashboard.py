import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np

# ── Simulation Data ─────────────────────────────────────
days         = [0,       30,      60,      90,      180    ]
torso_mass   = [34.2366, 33.8942, 33.5519, 33.2095, 32.1824]
pelvis_mass  = [11.7770, 11.6592, 11.5415, 11.4237, 11.0704]
muscle_force = [12972.0, 12431.5, 11891.0, 11350.5,  9729.0]
l4l5_load    = [2318.70,    2.27,    2.17,    2.07,    1.77]
muscle_loss  = [0.00,       4.17,    8.33,   12.50,   25.00]
bone_loss    = [0.00,       1.00,    2.00,    3.00,    6.00 ]
ercspn_force = [2500.0, 2395.8, 2291.7, 2187.5, 1875.0]
health_score = [100,    30,     25,     20,     10     ]

# ── Colors ───────────────────────────────────────────────
BG_COLOR    = "#0d1117"
PANEL_COLOR = "#161b22"
GRID_COLOR  = "#21262d"
TEXT_COLOR  = "#e6edf3"
GREEN       = "#3fb950"
YELLOW      = "#d29922"
RED         = "#f85149"
BLUE        = "#58a6ff"
PURPLE      = "#bc8cff"
ORANGE      = "#ffa657"

# ── Style Helper ────────────────────────────────────────
def style_ax(ax, title):
    ax.set_facecolor(PANEL_COLOR)
    ax.set_title(title, color=TEXT_COLOR,
                 fontsize=10, fontweight="bold", pad=8)
    ax.tick_params(colors=TEXT_COLOR, labelsize=8)
    ax.xaxis.label.set_color(TEXT_COLOR)
    ax.yaxis.label.set_color(TEXT_COLOR)
    ax.grid(True, color=GRID_COLOR,
            linestyle="--", linewidth=0.5, alpha=0.6)
    for spine in ax.spines.values():
        spine.set_edgecolor(GRID_COLOR)

# ── Figure ───────────────────────────────────────────────
fig = plt.figure(figsize=(22, 16), facecolor=BG_COLOR)

# Main title — give it more room
fig.suptitle(
    "Astronaut Spine Health Monitor  --  ISS 6-Month Mission\n"
    "Simulating NASA HRP Study  |  Dr. Ashley Weaver, Wake Forest",
    fontsize=14, fontweight="bold",
    color=TEXT_COLOR, y=0.97
)

# Outer grid: top 6 panels + bottom 1 panel
outer = gridspec.GridSpec(
    2, 1,
    figure=fig,
    height_ratios=[2, 1],
    hspace=0.52,
    top=0.93, bottom=0.06,
    left=0.06, right=0.97
)

# Top 6 panels grid (2 rows x 3 cols)
top_grid = gridspec.GridSpecFromSubplotSpec(
    2, 3,
    subplot_spec=outer[0],
    hspace=0.55, wspace=0.38
)

# Bottom 1 panel
bot_grid = gridspec.GridSpecFromSubplotSpec(
    1, 1,
    subplot_spec=outer[1]
)

# ════════════════════════════════════════════════════════
# PANEL 1 — Bone Mass Loss
# ════════════════════════════════════════════════════════
ax1 = fig.add_subplot(top_grid[0, 0])
style_ax(ax1, "Bone Mass Loss Over Mission")

ax1.plot(days, torso_mass, "o-",
         color=BLUE, linewidth=2.5,
         markersize=6, label="Torso")
ax1.plot(days, pelvis_mass, "s-",
         color=PURPLE, linewidth=2.5,
         markersize=6, label="Pelvis")
ax1.fill_between(days, torso_mass,
                 alpha=0.12, color=BLUE)
ax1.fill_between(days, pelvis_mass,
                 alpha=0.12, color=PURPLE)

ax1.set_xlabel("Mission Day", fontsize=8)
ax1.set_ylabel("Mass (kg)", fontsize=8)
ax1.legend(facecolor=PANEL_COLOR,
           labelcolor=TEXT_COLOR,
           fontsize=8, loc="upper right")

# Single clean annotation — no arrow overlap
ax1.text(170, torso_mass[-1] - 0.6,
         "-6%", color=RED,
         fontsize=9, fontweight="bold",
         ha="center")

# ════════════════════════════════════════════════════════
# PANEL 2 — Muscle Force Atrophy
# ════════════════════════════════════════════════════════
ax2 = fig.add_subplot(top_grid[0, 1])
style_ax(ax2, "Spine Muscle Force Atrophy")

ax2.plot(days, muscle_force, "o-",
         color=GREEN, linewidth=2.5,
         markersize=6, label="Total Spine")
ax2.plot(days, ercspn_force, "D-",
         color=ORANGE, linewidth=2.5,
         markersize=6, label="Erector Spinae R")
ax2.fill_between(days, muscle_force,
                 alpha=0.12, color=GREEN)

ax2.set_xlabel("Mission Day", fontsize=8)
ax2.set_ylabel("Max Force (N)", fontsize=8)
ax2.legend(facecolor=PANEL_COLOR,
           labelcolor=TEXT_COLOR,
           fontsize=8, loc="upper right")

ax2.text(155, ercspn_force[-1] - 180,
         "-25%", color=RED,
         fontsize=9, fontweight="bold",
         ha="center")

# ════════════════════════════════════════════════════════
# PANEL 3 — L4/L5 Compressive Load
# ════════════════════════════════════════════════════════
ax3 = fig.add_subplot(top_grid[0, 2])
style_ax(ax3, "L4/L5 Compressive Load (Log)")

bar_colors = [GREEN] + [RED] * 4
bars = ax3.bar(days, l4l5_load,
               color=bar_colors, width=11,
               edgecolor=GRID_COLOR, linewidth=0.8)
ax3.set_xlabel("Mission Day", fontsize=8)
ax3.set_ylabel("Load (N)", fontsize=8)
ax3.set_yscale("log")

labels_bar = ["2319N", "2N", "2N", "2N", "2N"]
for bar, lbl in zip(bars, labels_bar):
    ypos = bar.get_height() * 1.5
    ax3.text(bar.get_x() + bar.get_width() / 2,
             ypos, lbl,
             ha="center", va="bottom",
             color=TEXT_COLOR,
             fontsize=7, fontweight="bold")

# ════════════════════════════════════════════════════════
# PANEL 4 — Bone Density Loss
# ════════════════════════════════════════════════════════
ax4 = fig.add_subplot(top_grid[1, 0])
style_ax(ax4, "Cumulative Bone Density Loss")

ax4.fill_between(days, bone_loss,
                 alpha=0.35, color=RED)
ax4.plot(days, bone_loss, "o-",
         color=RED, linewidth=2.5, markersize=6)
ax4.axhline(y=1, color=YELLOW, linestyle="--",
            linewidth=1.5, label="1%/month threshold")

ax4.set_xlabel("Mission Day", fontsize=8)
ax4.set_ylabel("Bone Loss (%)", fontsize=8)
ax4.legend(facecolor=PANEL_COLOR,
           labelcolor=TEXT_COLOR,
           fontsize=8, loc="upper left")

# Clean text box — no arrow
ax4.text(95, 4.6,
         "NASA: ~1%/month\nwithout countermeasures",
         color=YELLOW, fontsize=7.5,
         ha="center",
         bbox=dict(boxstyle="round,pad=0.3",
                   facecolor=PANEL_COLOR,
                   edgecolor=YELLOW,
                   alpha=0.85))

# ════════════════════════════════════════════════════════
# PANEL 5 — Muscle Atrophy %
# ════════════════════════════════════════════════════════
ax5 = fig.add_subplot(top_grid[1, 1])
style_ax(ax5, "Cumulative Muscle Atrophy")

ax5.fill_between(days, muscle_loss,
                 alpha=0.35, color=ORANGE)
ax5.plot(days, muscle_loss, "o-",
         color=ORANGE, linewidth=2.5, markersize=6)
ax5.axhline(y=10, color=YELLOW, linestyle="--",
            linewidth=1.3, label="10% caution")
ax5.axhline(y=20, color=RED,    linestyle="--",
            linewidth=1.3, label="20% danger")

ax5.set_xlabel("Mission Day", fontsize=8)
ax5.set_ylabel("Muscle Loss (%)", fontsize=8)
ax5.legend(facecolor=PANEL_COLOR,
           labelcolor=TEXT_COLOR,
           fontsize=8, loc="upper left")

# ════════════════════════════════════════════════════════
# PANEL 6 — Risk Timeline
# ════════════════════════════════════════════════════════
ax6 = fig.add_subplot(top_grid[1, 2])
style_ax(ax6, "Spine Health Risk Timeline")

risk_scores = [0, 4, 4, 4, 4]
risk_colors = [GREEN, RED, RED, RED, RED]
risk_labels = ["None", "Critical",
               "Critical", "Critical", "Critical"]

ax6.scatter(days, risk_scores,
            c=risk_colors, s=180, zorder=5,
            edgecolors=TEXT_COLOR, linewidths=1.2)
ax6.plot(days, risk_scores, "--",
         color=GRID_COLOR, linewidth=1.5, zorder=4)

ax6.set_xlabel("Mission Day", fontsize=8)
ax6.set_ylabel("Risk Level", fontsize=8)
ax6.set_yticks([0, 1, 2, 3, 4])
ax6.set_yticklabels(
    ["None", "Low", "Moderate", "High", "Critical"],
    color=TEXT_COLOR, fontsize=8
)
ax6.set_ylim(-0.5, 5.2)

# Stagger label offsets to avoid overlap
v_offsets = [14, 14, 22, 14, 14]
for d, r, l, c, vo in zip(
        days, risk_scores,
        risk_labels, risk_colors, v_offsets):
    ax6.annotate(
        l, (d, r),
        textcoords="offset points",
        xytext=(0, vo),
        ha="center", fontsize=7.5,
        color=c, fontweight="bold"
    )

# ════════════════════════════════════════════════════════
# PANEL 7 — Combined Health Score (full width)
# ════════════════════════════════════════════════════════
ax7 = fig.add_subplot(bot_grid[0])
style_ax(ax7, "Combined Spine Health Score  --  Mission Timeline")

# Zones
ax7.axhspan(70,  115, alpha=0.10, color=GREEN)
ax7.axhspan(40,   70, alpha=0.10, color=YELLOW)
ax7.axhspan(0,    40, alpha=0.10, color=RED)

# Zone labels on right margin
ax7.text(192, 92,  "Healthy",  color=GREEN,
         fontsize=8, va="center", fontweight="bold")
ax7.text(192, 55,  "Caution",  color=YELLOW,
         fontsize=8, va="center", fontweight="bold")
ax7.text(192, 20,  "Critical", color=RED,
         fontsize=8, va="center", fontweight="bold")

# Health score line
ax7.plot(days, health_score, "o-",
         color=BLUE, linewidth=3,
         markersize=10, zorder=5,
         label="Spine Health Score")
ax7.fill_between(days, health_score,
                 alpha=0.18, color=BLUE)

# Point labels — alternating above/below to avoid overlap
point_labels = [
    "Earth Baseline\n(Full gravity)",
    "1 Month\n(Bone loss begins)",
    "2 Months\n(Muscle -8.3%)",
    "3 Months\n(Countermeasures\ncritical)",
    "6 Months\n(25% atrophy\nreturn risk)"
]
y_offsets  = [14, 14, 14, 14, 14]

for d, s, lbl, yo in zip(
        days, health_score, point_labels, y_offsets):
    ax7.annotate(
        lbl, (d, s),
        textcoords="offset points",
        xytext=(0, yo),
        ha="center", fontsize=7.5,
        color=TEXT_COLOR,
        bbox=dict(
            boxstyle="round,pad=0.25",
            facecolor=PANEL_COLOR,
            edgecolor=GRID_COLOR,
            alpha=0.9
        )
    )

# Mission phase dividers
phases = [
    (0,   30,  "Pre-Launch",          BLUE),
    (30,  90,  "Early Mission (ISS)", YELLOW),
    (90,  180, "Extended Mission",    RED),
]
for start, end, lbl, col in phases:
    ax7.axvline(x=start if start > 0 else 0,
                color=col, linestyle=":",
                alpha=0.5, linewidth=1.5)
    ax7.text((start + end) / 2, 107,
             lbl, ha="center",
             fontsize=8, color=col,
             fontweight="bold")

ax7.set_xlabel("Mission Day", fontsize=10)
ax7.set_ylabel("Health Score (0-100)", fontsize=10)
ax7.set_xlim(-10, 200)
ax7.set_ylim(0, 118)
ax7.legend(facecolor=PANEL_COLOR,
           labelcolor=TEXT_COLOR,
           fontsize=9, loc="center right")

# ── Save ────────────────────────────────────────────────
out = r"C:\SpineSimulation\Results\spine_health_dashboard.png"
plt.savefig(out, dpi=150,
            bbox_inches="tight",
            facecolor=BG_COLOR)
print(f"\n  Dashboard saved --> {out}")
plt.show()
print("  Done -- no emoji warnings!")