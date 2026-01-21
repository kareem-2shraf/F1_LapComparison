import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter
from style import COLORS

def animate_ghost(tel1, tel2, sectors, times1, times2):
    plt.rcParams.update({
        "figure.facecolor": COLORS["background"],
        "axes.facecolor": COLORS["background"],
        "axes.edgecolor": COLORS["grid"],
        "axes.labelcolor": COLORS["text"],
        "text.color": COLORS["text"],
        "xtick.color": COLORS["text"],
        "ytick.color": COLORS["text"]
    })

    fig = plt.figure(figsize=(14, 8))
    gs = fig.add_gridspec(
        2, 3,
        width_ratios=[2.2, 0.05, 1],
        height_ratios=[2, 1],
        hspace=0.15
    )

    ax_track = fig.add_subplot(gs[0, :2])
    ax_speed = fig.add_subplot(gs[1, :2])
    ax_table = fig.add_subplot(gs[:, 2])

    # ---------- TRACK ----------
    ax_track.set_title(
        "Spa Qualifying Lap Comparison (NOR) – 2019 vs 2025",
        fontsize=14, pad=10
    )
    ax_track.set_aspect("equal")
    ax_track.axis("off")

    ax_track.plot(tel1["X"], tel1["Y"], color=COLORS["ghost"], lw=2)
    ax_track.plot(tel2["X"], tel2["Y"], color=COLORS["track"], lw=2)

    ghost_dot, = ax_track.plot([], [], "o", color=COLORS["ghost"], ms=6)
    curr_dot, = ax_track.plot([], [], "o", color=COLORS["current"], ms=6)

    delta_text = ax_track.text(
        0.02, 0.01, "",
        transform=ax_track.transAxes,
        fontsize=12,
        weight="bold"
    )

    # ---------- SPEED ----------
    ax_speed.plot(
        tel1["Distance"], tel1["Speed"],
        color=COLORS["ghost"], label="2019 Ghost"
    )
    ax_speed.plot(
        tel2["Distance"], tel2["Speed"],
        color=COLORS["current"], label="2025"
    )
    ax_speed.set_xlabel("Distance (m)")
    ax_speed.set_ylabel("Speed (km/h)")
    ax_speed.legend(loc="lower left")

    speed_cursor = ax_speed.axvline(0, color=COLORS["text_dim"], lw=1)

    # ---------- TABLE ----------
    ax_table.axis("off")

    ax_table.text(0.25, 0.9, "2019", color=COLORS["text_dim"], fontsize=12)
    ax_table.text(0.65, 0.9, "2025", color=COLORS["current"], fontsize=12)

    rows = {}
    y0 = 0.8
    for s in ["S1", "S2", "S3"]:
        ax_table.text(0.05, y0, s)
        rows[s] = (
            ax_table.text(0.25, y0, "--"),
            ax_table.text(0.65, y0, "--", color=COLORS["current"])
        )
        y0 -= 0.08

    total_2019 = ax_table.text(0.25, y0 - 0.05, "--")
    total_2025 = ax_table.text(0.65, y0 - 0.05, "--", color=COLORS["current"])
    ax_table.text(0.05, y0 - 0.05, "Total")

    # ---------- ANIMATION ----------
    frames = min(len(tel1), len(tel2))

    def update(i):
        # --- track dots ---
        ghost_dot.set_data([tel1["X"].iloc[i]], [tel1["Y"].iloc[i]])
        curr_dot.set_data([tel2["X"].iloc[i]], [tel2["Y"].iloc[i]])

        d = tel2["Distance"].iloc[i]
        speed_cursor.set_xdata([d, d])

        # --- live sector timing ---
        total1 = total2 = 0.0

        for s, (start, end) in sectors.items():
            if d < start:
                rows[s][0].set_text("--")
                rows[s][1].set_text("--")
                continue

            t1 = tel1[tel1["Distance"] <= min(d, end)]["Time"].iloc[-1]
            t2 = tel2[tel2["Distance"] <= min(d, end)]["Time"].iloc[-1]

            dt1 = t1.total_seconds()
            dt2 = t2.total_seconds()

            rows[s][0].set_text(f"{dt1:.3f}")
            rows[s][1].set_text(f"{dt2:.3f}")

            total1 += dt1
            total2 += dt2

            if start <= d < end:
                delta = dt2 - dt1
                delta_text.set_text(f"{delta:+.2f}s in {s}")
                delta_text.set_color(
                    COLORS["delta_neg"] if delta < 0 else COLORS["delta_pos"]
                )

        total_2019.set_text(f"{total1:.3f}")
        total_2025.set_text(f"{total2:.3f}")

        return (
            ghost_dot, curr_dot,
            speed_cursor, delta_text,
            *[t for pair in rows.values() for t in pair],
            total_2019, total_2025
        )

    ani = FuncAnimation(fig, update, frames=frames, interval=40, blit=False)

    writer = FFMpegWriter(fps=25)
    ani.save("ghost_lap_comparison.mp4", writer=writer, dpi=150)