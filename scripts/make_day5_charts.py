#!/usr/bin/env python3
"""Day 5 charts for 'Regulation and Competitiveness' deck.
Georgetown palette; faithful to sourced figures from the Day 5 readings.
Outputs into the slides repo assets/ folder.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, FancyArrowPatch
import numpy as np
import os

NAVY = "#041e42"
BLUE = "#365f91"
TAUPE = "#8a7f75"
PALE = "#dce4ed"
MUTED = "#71839b"
PAPER = "#ffffff"

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 20,
    "axes.edgecolor": "#c9cfd6",
    "axes.linewidth": 1.0,
    "figure.facecolor": PAPER,
    "axes.facecolor": PAPER,
    "savefig.facecolor": PAPER,
})

OUT = os.path.expanduser("~/course-ai-economy-slides/assets")
os.makedirs(OUT, exist_ok=True)

def save(fig, name):
    path = os.path.join(OUT, name)
    fig.savefig(path, dpi=200, bbox_inches="tight", pad_inches=0.25)
    plt.close(fig)
    print("wrote", path)

# ---------------------------------------------------------------------------
# 1. Foundation AI models developed in 2024: EU 3, China 15, US 40
# ---------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(12, 6.75))
labels = ["European\nUnion", "China", "United\nStates"]
vals = [3, 15, 40]
colors = [MUTED, BLUE, NAVY]
bars = ax.bar(labels, vals, color=colors, width=0.62)
for b, v in zip(bars, vals):
    ax.text(b.get_x() + b.get_width()/2, v + 0.8, str(v),
            ha="center", va="bottom", fontsize=30, fontweight="bold", color=NAVY)
ax.set_ylim(0, 46)
ax.set_ylabel("Notable foundation models (2024)")
ax.spines[["top", "right"]].set_visible(False)
ax.tick_params(length=0)
ax.set_yticks([0, 10, 20, 30, 40])
ax.margins(x=0.04)
save(fig, "day5_foundation_models.png")

# ---------------------------------------------------------------------------
# 2. Investment need: 2024 report ~EUR 800bn/yr -> 2025 update ~EUR 1,200bn/yr
# ---------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(12, 6.75))
labels = ["Draghi Report\n(Sep 2024)", "One Year On\n(Sep 2025)"]
vals = [800, 1200]
bars = ax.bar(labels, vals, color=[BLUE, NAVY], width=0.55)
for b, v in zip(bars, vals):
    ax.text(b.get_x() + b.get_width()/2, v + 22, f"€{v:,}bn",
            ha="center", va="bottom", fontsize=30, fontweight="bold", color=NAVY)
ax.set_ylim(0, 1360)
ax.set_ylabel("Extra investment needed, per year")
ax.spines[["top", "right"]].set_visible(False)
ax.tick_params(length=0)
ax.set_yticks([0, 400, 800, 1200])
ax.set_yticklabels(["0", "400", "800", "1,200"])
ax.text(0.5, -0.19, "About 5% of EU GDP every year, several times the Marshall Plan's share",
        transform=ax.transAxes, ha="center", va="top", fontsize=17, color=MUTED, style="italic")
ax.margins(x=0.06)
save(fig, "day5_investment_need.png")

# ---------------------------------------------------------------------------
# 3. EU AI Act risk pyramid (four tiers)
# ---------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(12, 7.2))
ax.axis("off")
# Trapezoid tiers from top (narrow) to bottom (wide)
tiers = [
    ("Unacceptable risk", "Banned", NAVY, "#ffffff", 20),
    ("High risk", "Strict duties + registration", BLUE, "#ffffff", 23),
    ("Limited risk", "Transparency (Art. 50)", "#7c93b5", NAVY, 23),
    ("Minimal risk", "No extra rules for most AI", PALE, NAVY, 23),
]
n = len(tiers)
H = 1.0            # height per tier
gap = 0.06
top_hw = 2.0      # half-width at apex
bot_hw = 4.7      # half-width at base
for i, (title, sub, fc, tc, tfs) in enumerate(tiers):
    # width interpolates from narrow (top, i=0) to wide (bottom, i=n-1)
    w_top = top_hw + (bot_hw - top_hw) * (i) / n
    w_bot = top_hw + (bot_hw - top_hw) * (i + 1) / n
    y_top = (n - i) * (H + gap)
    y_bot = y_top - H
    poly = Polygon([(-w_top, y_top), (w_top, y_top), (w_bot, y_bot), (-w_bot, y_bot)],
                   closed=True, facecolor=fc, edgecolor="white", linewidth=2)
    ax.add_patch(poly)
    yc = (y_top + y_bot) / 2
    ax.text(0, yc + 0.15, title, ha="center", va="center",
            fontsize=tfs, fontweight="bold", color=tc)
    ax.text(0, yc - 0.24, sub, ha="center", va="center",
            fontsize=15, color=tc)
ax.set_xlim(-bot_hw - 0.3, bot_hw + 0.3)
ax.set_ylim(0, (n) * (H + gap) + 0.5)
save(fig, "day5_ai_act_tiers.png")

# ---------------------------------------------------------------------------
# 4. Digital Omnibus timeline: high-risk duties pushed back
# ---------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(12.5, 6.4))
ax.axis("off")
# main axis line
x0, x1 = 0.03, 0.97
y = 0.52
ax.annotate("", xy=(x1, y), xytext=(x0, y),
            arrowprops=dict(arrowstyle="-|>", color=NAVY, lw=2.4))
# points: (xfrac, label, sublabel, color, above?)
points = [
    (0.10, "Aug 2026", "Original\nhigh-risk start", TAUPE, False, True),
    (0.30, "Dec 2026", "Content labelling;\nnew abuse-image ban", BLUE, False, False),
    (0.50, "Aug 2027", "Sandboxes\nin place", BLUE, False, False),
    (0.72, "Dec 2027", "High-risk duties\n(standalone)", NAVY, True, False),
    (0.92, "Aug 2028", "High-risk duties\n(in products)", NAVY, True, False),
]
for xf, lab, sub, col, above, struck in points:
    ax.plot([xf], [y], "o", ms=15, color=col, zorder=5)
    if above:
        ax.text(xf, y + 0.10, lab, ha="center", va="bottom", fontsize=20, fontweight="bold", color=NAVY)
        ax.text(xf, y + 0.235, sub, ha="center", va="bottom", fontsize=14.5, color=MUTED)
    else:
        ax.text(xf, y - 0.10, lab, ha="center", va="top", fontsize=20, fontweight="bold",
                color=(TAUPE if struck else NAVY))
        ax.text(xf, y - 0.235, sub, ha="center", va="top", fontsize=14.5,
                color=(TAUPE if struck else MUTED))
# "was" -> "now" shift arrow from Aug 2026 to Dec 2027
arr = FancyArrowPatch((0.10, y + 0.03), (0.72, y + 0.03),
                      connectionstyle="arc3,rad=-0.26",
                      arrowstyle="-|>", mutation_scale=22, lw=2.2,
                      color="#b23a48", zorder=4)
ax.add_patch(arr)
ax.text(0.41, y + 0.40, "Delayed about 16 months", ha="center", va="center",
        fontsize=18, fontweight="bold", color="#b23a48")
ax.set_xlim(0, 1)
ax.set_ylim(0.02, 0.98)
save(fig, "day5_omnibus_timeline.png")

print("done")
