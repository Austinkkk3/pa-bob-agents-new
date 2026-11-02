"""Generate the two Lab 1 Exercise 5 images: a flow diagram and a time comparison."""
import sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

OUT = sys.argv[1]
INK, MUTED, GRID, SURFACE = "#0b0b0b", "#52514e", "#d9d8d4", "#ffffff"
BLUE, ORANGE = "#2a78d6", "#eb6834"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})


def box(ax, x, y, w, h, title, body=None, accent=False, container=False):
    edge = BLUE if accent else ("#a8a7a2" if container else "#7d7c78")
    face = "#eaf2fc" if accent else ("#f6f6f4" if container else SURFACE)
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=0.015",
                                linewidth=2 if accent else 1.2, edgecolor=edge, facecolor=face,
                                zorder=1 if container else 3))
    if container:
        ax.text(x + 0.015, y + h - 0.045, title, ha="left", va="center", fontsize=12,
                fontweight="bold", color=MUTED, zorder=4)
    else:
        ty = y + h / 2 + (0.035 if body else 0)
        ax.text(x + w / 2, ty, title, ha="center", va="center", fontsize=12.5,
                fontweight="bold", color=INK, zorder=4)
        if body:
            ax.text(x + w / 2, y + h / 2 - 0.045, body, ha="center", va="center",
                    fontsize=10.5, color=MUTED, zorder=4)


def arrow(ax, start, end, label, label_xy, rad=0.0, ha="center"):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=16,
                                 linewidth=1.6, color="#5f5e5a",
                                 connectionstyle=f"arc3,rad={rad}", zorder=5))
    ax.text(*label_xy, label, ha=ha, va="center", fontsize=10.5, color=INK, zorder=6,
            bbox=dict(boxstyle="round,pad=0.25", facecolor=SURFACE, edgecolor="none"))


# ---------- 1. Flow diagram ----------
fig, ax = plt.subplots(figsize=(12, 5.2), dpi=160)
ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
fig.patch.set_facecolor(SURFACE)
ax.text(0.02, 0.96, "What Bob does in Exercise 5", fontsize=16, fontweight="bold", color=INK, va="center")
ax.text(0.02, 0.90, "Bob turns six CSV files into a working TM1 model on the DemoGuide server, then checks it",
        fontsize=11.5, color=MUTED, va="center")

ROW_Y, ROW_H = 0.38, 0.22
box(ax, 0.02, 0.25, 0.38, 0.55, "Your laptop", container=True)
box(ax, 0.04, ROW_Y, 0.14, ROW_H, "6 CSV files", "assets/ folder")
box(ax, 0.23, ROW_Y, 0.15, ROW_H, "IBM Bob", "PA mode\n+ PA skill", accent=True)
box(ax, 0.56, 0.25, 0.42, 0.55, "Planning Analytics on TechZone", container=True)
box(ax, 0.58, ROW_Y, 0.16, ROW_H, "PA MCP server", "cube and\nserver tools")
box(ax, 0.79, ROW_Y, 0.17, ROW_H, "DemoGuide", "6 dimensions\n1 cube · 280 rows")

mid = ROW_Y + ROW_H / 2
def harrow(x0, x1, y):
    ax.add_patch(FancyArrowPatch((x0, y), (x1, y), arrowstyle="-|>", mutation_scale=16,
                                 linewidth=1.6, color="#5f5e5a", zorder=5))
harrow(0.18, 0.23, mid)
harrow(0.38, 0.58, mid)
harrow(0.74, 0.79, mid)
lab = dict(ha="center", va="bottom", fontsize=10.5, color=INK, zorder=6)
ax.text(0.205, ROW_Y + ROW_H + 0.025, "1 reads", **lab)
ax.text(0.48, mid + 0.025, "2 sends TI processes\n(rows inside the code)", **lab)
ax.text(0.765, ROW_Y + ROW_H + 0.025, "3 runs", **lab)

# 4: read-back loop under the boxes, from DemoGuide back to Bob
y_low = 0.15
ax.plot([0.875, 0.875, 0.305], [ROW_Y, y_low, y_low], color="#5f5e5a", linewidth=1.6, zorder=5,
        solid_joinstyle="miter")
ax.add_patch(FancyArrowPatch((0.305, y_low), (0.305, ROW_Y), arrowstyle="-|>", mutation_scale=16,
                             linewidth=1.6, color="#5f5e5a", zorder=5))
ax.text(0.59, y_low - 0.03, "4 reads cells back with MDX to check the load", ha="center", va="top",
        fontsize=10.5, color=INK, zorder=6)

ax.text(0.02, 0.02, "Why the rows travel inside the TI code: the PA server runs in the cloud and cannot read files on your laptop.",
        fontsize=10.5, color=MUTED, va="center")
fig.savefig(f"{OUT}/lab1-ex5-00-what-bob-does.png", facecolor=SURFACE, bbox_inches="tight", pad_inches=0.15)
plt.close(fig)

# ---------- 2. Time comparison ----------
fig, ax = plt.subplots(figsize=(11, 3.6), dpi=160)
fig.patch.set_facecolor(SURFACE); ax.set_facecolor(SURFACE)
labels = ["By hand\n(estimate, experienced TM1 developer)", "IBM Bob\n(measured on DemoGuide)"]
ys = [0, 1]
ax.errorbar(75, 0, xerr=[[15], [15]], fmt="o", color=ORANGE, ecolor=ORANGE, elinewidth=2.2,
            capsize=7, markersize=11, zorder=4)
ax.plot([6.5], [1], "o", color=BLUE, markersize=11, zorder=4)
ax.text(6.5 + 2.5, 1, "about 6.5 min", va="center", ha="left", fontsize=11.5, color=INK, fontweight="bold")
ax.text(75, 0.22, "60–90 min", va="bottom", ha="center", fontsize=11.5, color=INK, fontweight="bold")
ax.set_ylim(-0.5, 1.5)
ax.set_yticks(ys, labels, fontsize=11, color=INK)
ax.set_xlim(0, 105)
ax.set_xticks(range(0, 106, 15))
ax.set_xlabel("Minutes to build 6 dimensions, 1 cube and load 280 rows", color=MUTED, fontsize=10.5)
ax.tick_params(axis="x", colors=MUTED, labelsize=10)
ax.tick_params(axis="y", length=0)
ax.grid(axis="x", color=GRID, linewidth=0.8, zorder=0)
for s in ["top", "right", "left"]:
    ax.spines[s].set_visible(False)
ax.spines["bottom"].set_color(GRID)
fig.suptitle("Bob builds the Exercise 5 model about 10× faster than building it by hand",
             x=0.015, y=0.99, ha="left", fontsize=14, fontweight="bold", color=INK)
fig.text(0.015, 0.875, "The by-hand time is an estimate, not a measurement; someone new to TM1 would take longer",
         ha="left", fontsize=10.5, color=MUTED)
fig.tight_layout(rect=(0, 0, 1, 0.86))
fig.savefig(f"{OUT}/lab1-ex5-06-time-vs-manual.png", facecolor=SURFACE, bbox_inches="tight", pad_inches=0.15)
plt.close(fig)
print("ok")
