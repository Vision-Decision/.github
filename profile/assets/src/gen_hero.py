"""Generate the Vision-Decision org hero banner (light + dark) as SVG.

v4: transparent canvas (sits on GitHub's page colour), headline + definition on
top, the Glance mechanism in the middle, and a full-width "typical VLM" row at
the bottom so the contrast is drawn, not asserted. Minimum text 18px at 1200px
(~12.4px at GitHub's ~830px README width).
"""
import sys

OUT = sys.argv[1]

T = {
    "light": dict(line="#d9d8d1", ink="#0b0b0b", ink2="#52514e", muted="#6f6e69", panel="#f6f6f3",
                  pill="#ffffff", blue="#2a78d6", blue_t="#e3eefb", onblue="#ffffff",
                  orange="#d9622b", orange_t="#fde9e0",
                  mark="#16213A", dot="#E8743B", win="#ffffff", winbar="#efeeea", ghost="#c3c2b7"),
    "dark": dict(line="#30363d", ink="#f0f6fc", ink2="#c3c2b7", muted="#9198a1", panel="#161b22",
                 pill="#161b22", blue="#3987e5", blue_t="#14263d", onblue="#ffffff",
                 orange="#f08a4b", orange_t="#3a1d12",
                 mark="#EEF0F4", dot="#F08A4B", win="#161b22", winbar="#21262d", ghost="#5d6670"),
}

FONT = "Avenir Next, Helvetica Neue, Helvetica, Arial, sans-serif"
W, H = 1200, 696
ROWS = [222, 290, 358, 426]
PH = 54
QS = ["Where is Save?", "Dialog open?", "Which tab is on?", "Where is Export?"]


def corners(x, y, w, h, L, c, sw):
    """Viewfinder corners (the logo motif) around a rect."""
    d = (f"M{x} {y+L}V{y}H{x+L}" f"M{x+w-L} {y}H{x+w}V{y+L}"
         f"M{x+w} {y+h-L}V{y+h}H{x+w-L}" f"M{x+L} {y+h}H{x}V{y+h-L}")
    return f'<path d="{d}" fill="none" stroke="{c}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"/>'


def text(x, y, s, size, fill, weight=400, anchor="start", ls=0):
    return (f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" font-weight="{weight}" '
            f'fill="{fill}" text-anchor="{anchor}" letter-spacing="{ls}">{s}</text>')


def build(t):
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" '
         'aria-label="Glance answers many questions about one image in one forward pass, returning typed decisions: '
         'a box, yes or no, a choice, or a calibrated not there. A typical VLM decodes free text token by token for every question; Glance stops after prefill and reads every answer from heads.">']

    # ---- header -------------------------------------------------------------
    s = 64 / 128
    o.append(f'<g transform="translate(12 18) scale({s})">'
             f'<g fill="none" stroke="{t["mark"]}" stroke-width="9" stroke-linecap="round" stroke-linejoin="round">'
             '<path d="M18 46V28a10 10 0 0 1 10-10h18"/><path d="M82 18h18a10 10 0 0 1 10 10v18"/>'
             '<path d="M110 82v18a10 10 0 0 1-10 10H82"/><path d="M46 110H28a10 10 0 0 1-10-10V82"/></g>'
             f'<circle cx="64" cy="64" r="14" fill="{t["dot"]}"/></g>')
    o.append(text(96, 56, "Ask an image many questions. Get typed decisions in one pass.", 34, t["ink"], 700, ls=-0.4))
    o.append(text(96, 94, "Vision-Decision builds Glance: a 4B VLM for agents that look at screens, photos and video.",
                  21, t["ink2"], 500))
    o.append(f'<line x1="12" y1="120" x2="1188" y2="120" stroke="{t["line"]}" stroke-width="1.5"/>')

    # ---- column headers -----------------------------------------------------
    hy = 160
    o.append(text(336, hy, "ONE IMAGE + MANY QUESTIONS", 20, t["muted"], 600, "middle", 1.4))
    o.append(text(762, hy, "ONE PASS", 20, t["muted"], 600, "middle", 1.4))
    o.append(text(1030, hy, "TYPED DECISIONS", 20, t["muted"], 600, "middle", 1.4))

    o.append(f'<rect x="12" y="184" width="638" height="280" rx="20" fill="none" stroke="{t["line"]}" stroke-width="1.5"/>')

    # ---- the image: a small app window --------------------------------------
    wx, wy, ww, wh = 32, 208, 296, 232
    o.append(f'<rect x="{wx}" y="{wy}" width="{ww}" height="{wh}" rx="12" fill="{t["win"]}" stroke="{t["line"]}" stroke-width="1.5"/>')
    o.append(f'<path d="M{wx} {wy+32}V{wy+12}a12 12 0 0 1 12-12h{ww-24}a12 12 0 0 1 12 12v20z" fill="{t["winbar"]}"/>')
    for i in range(3):
        o.append(f'<circle cx="{wx+18+i*15}" cy="{wy+16}" r="4.5" fill="{t["ghost"]}"/>')
    tx = wx + 20
    for name, act in [("Home", 0), ("Edit", 1), ("View", 0)]:
        o.append(text(tx, wy + 66, name, 19, t["ink"] if act else t["muted"], 600 if act else 500))
        if act:
            o.append(f'<rect x="{tx}" y="{wy+74}" width="38" height="4" rx="2" fill="{t["ink2"]}"/>')
        tx += 82
    o.append(f'<line x1="{wx}" y1="{wy+86}" x2="{wx+ww}" y2="{wy+86}" stroke="{t["line"]}" stroke-width="1.2"/>')
    bx = wx + 20
    for name, w in [("Save", 72), ("Open", 74), ("Share", 82)]:
        o.append(f'<rect x="{bx}" y="{wy+106}" width="{w}" height="36" rx="8" fill="none" stroke="{t["ghost"]}" stroke-width="1.6"/>')
        o.append(text(bx + w / 2, wy + 131, name, 18, t["ink2"], 500, "middle"))
        if name == "Save":
            o.append(corners(bx - 9, wy + 97, w + 18, 54, 13, t["blue"], 3.8))
        bx += w + 12
    for i, w in enumerate([254, 200, 226]):
        o.append(f'<rect x="{wx+20}" y="{wy+170+i*17}" width="{w}" height="7" rx="3.5" fill="{t["ghost"]}" opacity="0.7"/>')

    o.append(text(352, 336, "+", 34, t["muted"], 500, "middle"))

    # ---- questions ----------------------------------------------------------
    qx, qw = 374, 258
    for y, q in zip(ROWS, QS):
        o.append(f'<rect x="{qx}" y="{y-PH/2}" width="{qw}" height="{PH}" rx="{PH/2}" fill="{t["pill"]}" stroke="{t["line"]}" stroke-width="1.5"/>')
        o.append(text(qx + 22, y + 8, q, 22, t["ink"], 500))
        o.append(f'<line x1="{qx+qw}" y1="{y}" x2="700" y2="{y}" stroke="{t["ink2"]}" stroke-width="2.2"/>')

    # ---- one pass -----------------------------------------------------------
    px, pw = 700, 124
    o.append(f'<rect x="{px}" y="184" width="{pw}" height="280" rx="20" fill="{t["blue"]}"/>')
    o.append(corners(px + 31, 250, pw - 62, 64, 14, t["onblue"], 3.8))
    o.append(f'<circle cx="{px+pw/2}" cy="282" r="8" fill="{t["onblue"]}"/>')
    o.append(text(px + pw / 2, 364, "1 forward", 22, t["onblue"], 700, "middle"))
    o.append(text(px + pw / 2, 391, "pass", 22, t["onblue"], 700, "middle"))

    # ---- typed decisions ----------------------------------------------------
    ax, aw = 872, 316
    answers = [("BOX", "[40, 96, 120, 150]", "box"), ("YES / NO", "no", None), ("CHOICE", "Edit", None),
               ("NOT THERE", "none", "absent")]
    for y, (tag, val, kind) in zip(ROWS, answers):
        c, ct = (t["orange"], t["orange_t"]) if kind == "absent" else (t["blue"], t["blue_t"])
        o.append(f'<line x1="{px+pw}" y1="{y}" x2="{ax-8}" y2="{y}" stroke="{c}" stroke-width="2.4"/>')
        o.append(f'<path d="M{ax-16} {y-7}L{ax-4} {y}L{ax-16} {y+7}z" fill="{c}"/>')
        dash = ' stroke-dasharray="7 6"' if kind == "absent" else ""
        o.append(f'<rect x="{ax}" y="{y-PH/2}" width="{aw}" height="{PH}" rx="12" fill="{ct}" stroke="{c if kind == "absent" else ct}" stroke-width="2"{dash}/>')
        o.append(text(ax + 20, y + 7, tag, 18, c, 700, ls=1))
        o.append(text(ax + aw - 20, y + 8, val, 22, t["ink"], 600, "end"))

    # ---- timeline: typical VLM vs Glance ------------------------------------
    y0 = 488
    o.append(f'<rect x="12" y="{y0}" width="1176" height="{H-y0-8}" rx="20" fill="{t["panel"]}"/>')
    bx0, bw = 404, 124
    # typical VLM lane
    o.append(text(40, y0 + 52, "Typical VLM", 24, t["ink"], 700))
    o.append(text(40, y0 + 82, "writes free text, then parses it", 22, t["ink2"], 500))
    o.append(f'<rect x="{bx0}" y="{y0+22}" width="{bw}" height="68" rx="8" fill="none" stroke="{t["ghost"]}" stroke-width="2"/>')
    o.append(text(bx0 + bw / 2, y0 + 63, "prefill", 20, t["ink2"], 600, "middle"))
    widths = [20, 40, 16, 34, 16, 40, 16, 40, 20]
    for r in range(4):
        x = bx0 + bw + 10
        for w in widths:
            o.append(f'<rect x="{x}" y="{y0+22+r*18}" width="{w}" height="14" rx="3.5" fill="none" stroke="{t["ghost"]}" stroke-width="1.6"/>')
            x += w + 5
    ex = x + 18
    o.append(text(ex, y0 + 52, "+ one step per token,", 22, t["ink2"], 600))
    o.append(text(ex, y0 + 82, "for every question", 22, t["ink2"], 600))
    # Glance lane
    gy = y0 + 116
    o.append(text(40, gy + 30, "Glance", 24, t["blue"], 700))
    o.append(f'<rect x="{bx0}" y="{gy}" width="{bw}" height="44" rx="8" fill="{t["blue"]}"/>')
    o.append(text(bx0 + bw / 2, gy + 29, "prefill", 20, t["onblue"], 700, "middle"))
    o.append(text(bx0 + bw + 20, gy + 30, "done. Every answer is read from heads.", 22, t["ink"], 700))
    # time axis
    ay = y0 + 182
    o.append(f'<line x1="{bx0}" y1="{ay}" x2="1150" y2="{ay}" stroke="{t["ghost"]}" stroke-width="2"/>')
    o.append(f'<path d="M1146 {ay-6}L1158 {ay}L1146 {ay+6}z" fill="{t["ghost"]}"/>')
    o.append(text(1158, ay - 12, "time", 21, t["ink2"], 600, "end"))
    o.append('</svg>')
    return "\n".join(o)


for mode, t in T.items():
    with open(f"{OUT}/hero-{mode}.svg", "w") as f:
        f.write(build(t))
