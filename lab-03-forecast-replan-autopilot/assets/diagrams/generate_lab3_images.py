"""Generate the two Lab 3 overview images: what Bob does, and the reforecast it writes back."""
import sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

OUT = sys.argv[1] if len(sys.argv) > 1 else "."
INK, MUTED, GRID, SURFACE = "#0b0b0b", "#52514e", "#d9d8d4", "#ffffff"
BLUE, ORANGE, AQUA = "#2a78d6", "#eb6834", "#1baf7a"   # categorical slots 1-3
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11, "text.parse_math": False})


# ---------- 1. What Bob does in Lab 3 ----------
def box(ax, x, y, w, h, title, body, accent=False, face=SURFACE):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=0.012",
                                linewidth=2 if accent else 1.2,
                                edgecolor=BLUE if accent else "#7d7c78",
                                facecolor="#eaf2fc" if accent else face, zorder=3))
    ax.text(x + w / 2, y + h - 0.045, title, ha="center", va="top", fontsize=12,
            fontweight="bold", color=INK, zorder=4)
    ax.text(x + w / 2, y + h - 0.115, body, ha="center", va="top", fontsize=10,
            color=MUTED, zorder=4, linespacing=1.35)


def harrow(ax, x0, x1, y):
    ax.add_patch(FancyArrowPatch((x0, y), (x1, y), arrowstyle="-|>", mutation_scale=15,
                                 linewidth=1.6, color="#5f5e5a", zorder=5))


fig, ax = plt.subplots(figsize=(13, 5.6), dpi=160)
ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
fig.patch.set_facecolor(SURFACE)
ax.text(0.01, 0.97, "What you do in Lab 3", fontsize=16, fontweight="bold", color=INK, va="center")
ax.text(0.01, 0.91, "One conversation with Bob: find the January miss, explain it, replan Q1 and write the new forecast into Planning Analytics",
        fontsize=11, color=MUTED, va="center")

steps = [
    ("1  Find", "Jan 2024 actual\nvs budget, flag\n>$100K or >20%"),
    ("2  Explain", "Timing (deals slipped)\nor structural\n(new run-rate)?"),
    ("3  Replan", "Q1 reforecast\ntable, checked\nbefore writing"),
    ("4  Write back", "6 cells into\nFC-Q1 / V3 with the\nFPA_Write_Forecast\nTI process"),
    ("5  Verify", "Actual, budget and\nreforecast side by\nside + CFO summary"),
]
W, H, Y, GAP = 0.165, 0.36, 0.38, 0.032
xs = [0.01 + i * (W + GAP) for i in range(5)]
for i, (x, (t, b)) in enumerate(zip(xs, steps)):
    box(ax, x, Y, W, H, t, b, accent=(i == 3))
    if i < 4:
        harrow(ax, x + W + 0.003, x + W + GAP - 0.003, Y + H / 2)

# what each step touches in PA
ax.add_patch(FancyBboxPatch((0.01, 0.06), 0.98, 0.22, boxstyle="round,pad=0,rounding_size=0.012",
                            linewidth=1.2, edgecolor="#a8a7a2", facecolor="#f6f6f4", zorder=1))
ax.text(0.025, 0.265, "Planning Analytics · smartco · FPA_Variance", fontsize=11, fontweight="bold",
        color=MUTED, va="top")
ax.text(xs[0] + W / 2, 0.14, "reads Actual (V1)\nand Budget (V2)", ha="center", va="center", fontsize=10, color=INK)
ax.text(xs[1] + W / 2, 0.14, "reads the root cause\ntext stored in the cube", ha="center", va="center", fontsize=10, color=INK)
ax.text(xs[2] + W / 2, 0.14, "reads Feb/Mar budget;\nnothing written yet", ha="center", va="center", fontsize=10, color=INK)
ax.text(xs[3] + W / 2, 0.14, "writes Reforecast\n(scenario FC-Q1, V3)", ha="center", va="center", fontsize=10,
        color=INK, fontweight="bold")
ax.text(xs[4] + W / 2, 0.14, "reads V1, V2 and V3\nback with MDX", ha="center", va="center", fontsize=10, color=INK)
for x in xs:
    ax.plot([x + W / 2, x + W / 2], [Y, 0.28], color="#a8a7a2", linewidth=1, linestyle=(0, (2, 2)), zorder=2)
ax.text(0.01, 0.015, "Lab 1 and Lab 2 only read data. Step 4 is the first time Bob changes data in PA; the facilitator clears it afterwards with FPA_Reset_Forecast.",
        fontsize=10, color=MUTED, va="center")
fig.savefig(f"{OUT}/lab3-00-what-you-do.png", facecolor=SURFACE, bbox_inches="tight", pad_inches=0.15)
plt.close(fig)


# ---------- 2. The reforecast Bob writes back (NA Sales, Q1 2024) ----------
months = ["Jan", "Feb", "Mar"]
data = {
    "REV-001  Finished Goods Revenue": {
        "Budget (V2)": [500000, 520000, 540000],
        "Reforecast (FC-Q1 / V3)": [325000, 720000, 540000],
        "Actual (V1)": [325000, 695000, 525000],
        "note": "Jan miss of $175K moves to Feb (+$200K of slipped deals)",
    },
    "OPEX-001  Sales & Distribution OpEx": {
        "Budget (V2)": [120000, 125000, 130000],
        "Reforecast (FC-Q1 / V3)": [145000, 133500, 138500],
        "Actual (V1)": [145000, 128000, 135000],
        "note": "+$8,500/month new hire from Feb; the $18K trade show is one-time",
    },
}
series = [("Budget (V2)", BLUE), ("Reforecast (FC-Q1 / V3)", ORANGE), ("Actual (V1)", AQUA)]

fig, axes = plt.subplots(1, 2, figsize=(13, 4.9), dpi=160)
fig.patch.set_facecolor(SURFACE)
bw, gap = 0.26, 0.012
for ax, (acct, d) in zip(axes, data.items()):
    ax.set_facecolor(SURFACE)
    for j, (name, color) in enumerate(series):
        xs_ = [i + (j - 1) * (bw + gap) for i in range(3)]
        bars = ax.bar(xs_, d[name], width=bw, color=color, zorder=3, label=name)
        if name.startswith("Reforecast"):   # direct-label the written values only
            for x, v in zip(xs_, d[name]):
                ax.text(x, v, f"{v/1000:,.1f}K".replace(".0K", "K"), ha="center", va="bottom",
                        fontsize=9.5, color=INK, fontweight="bold", zorder=4)
    ax.set_xticks(range(3), months, fontsize=11, color=INK)
    top = max(max(d[n]) for n, _ in series)
    ax.set_ylim(0, top * 1.18)
    ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f"{v/1000:,.0f}K"))
    ax.tick_params(axis="y", colors=MUTED, labelsize=9.5, length=0)
    ax.tick_params(axis="x", length=0)
    ax.grid(axis="y", color=GRID, linewidth=0.8, zorder=0)
    for s in ["top", "right", "left"]:
        ax.spines[s].set_visible(False)
    ax.spines["bottom"].set_color(GRID)
    ax.set_title(acct, loc="left", fontsize=12.5, fontweight="bold", color=INK, pad=22)
    ax.text(0, 1.03, d["note"], transform=ax.transAxes, fontsize=10, color=MUTED, va="bottom")

handles, labels = axes[0].get_legend_handles_labels()
fig.legend(handles, labels, loc="lower center", ncol=3, frameon=False, fontsize=10.5,
           bbox_to_anchor=(0.5, -0.02))
fig.suptitle("The reforecast Bob writes back: NA Sales, Q1 2024", x=0.01, y=1.0, ha="left",
             fontsize=15, fontweight="bold", color=INK)
fig.text(0.01, 0.925, "Six orange values go into FC-Q1 / V3. Q1 vs budget: REV-001 +$25K, OPEX-001 +$42K. Actuals are already in the cube, so you can see how good the replan was.",
         ha="left", fontsize=10.5, color=MUTED)
fig.tight_layout(rect=(0, 0.05, 1, 0.9))
fig.savefig(f"{OUT}/lab3-00-reforecast-q1.png", facecolor=SURFACE, bbox_inches="tight", pad_inches=0.15)
plt.close(fig)
print("ok")
