#!/usr/bin/env python3
"""Generates every figure of the manual as standalone SVG into figures/svg/.
Edit data/geometry here, run `python build.py`. No dependencies."""
import math, random, pathlib, re
OUT = pathlib.Path(__file__).parent / "svg"
FG, ACC, ACC2, MUTE, FILL = "#1f2937", "#2563eb", "#dc2626", "#9ca3af", "#eff6ff"
DEFS = ('<defs><marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
        'orient="auto-start-reverse"><path d="M0,0L10,5L0,10z" fill="#1f2937"/></marker></defs>')

def svg(w, h, body, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" '
            f'font-family="Helvetica,Arial,sans-serif" font-size="12" fill="{FG}">'
            f'<title>{title}</title>{DEFS}<rect width="{w}" height="{h}" fill="#fff"/>{body}</svg>')
def T(x, y, s, a="middle", size=12, w="normal", fill=None):
    f = f' fill="{fill}"' if fill else ""
    return f'<text x="{x}" y="{y}" text-anchor="{a}" font-size="{size}" font-weight="{w}"{f}>{s}</text>'
def R(x, y, w, h, fill=FILL, stroke=FG, rx=4, sw=1.2, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>'
def L(x1, y1, x2, y2, stroke=FG, sw=1.2, arrow=False, dash=None):
    m = ' marker-end="url(#ar)"' if arrow else ""
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{sw}"{m}{d}/>'
def P(pts, stroke=ACC, sw=2, fill="none"):
    s = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    return f'<polyline points="{s}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round"/>'
def box(x, y, w, h, label, fill=FILL, size=12, dash=None):
    return R(x, y, w, h, fill=fill, dash=dash) + T(x + w / 2, y + h / 2 + size / 3, label, size=size)
def callout(x, y, n):
    return f'<circle cx="{x}" cy="{y}" r="9" fill="{ACC2}"/>' + T(x, y + 4, n, size=10, w="bold", fill="#fff")

FIGS = {}
def fig(fn): FIGS[fn.__name__] = fn; return fn

@fig
def modes_flow():
    b = R(20, 20, 200, 80) + T(120, 52, "NORMAL", w="bold", size=14) + T(120, 74, "1 patch at a time", size=11)
    b += R(280, 20, 200, 80) + T(380, 52, "COMBINATION", w="bold", size=14) + T(380, 74, "up to 4 patches (work area)", size=11)
    b += R(540, 20, 200, 80) + T(640, 52, "OPERATION MEMORY", w="bold", size=14) + T(640, 74, "64 full keyboard setups", size=11)
    b += R(280, 150, 200, 70) + T(380, 180, "MULTI CHANNEL", w="bold", size=14) + T(380, 200, "8 MIDI areas", size=11)
    b += R(20, 150, 200, 70, fill="#f3f4f6") + T(120, 180, "INTERNAL (64) / CARD", w="bold", size=13) + T(120, 200, "patch storage", size=11)
    b += L(220, 50, 280, 50, arrow=True) + T(250, 42, "combine", size=10)
    b += L(480, 50, 540, 50, arrow=True) + T(510, 42, "WRITE", size=10)
    b += L(110, 150, 110, 100, arrow=True) + L(130, 100, 130, 150, arrow=True) + T(172, 130, "WRITE / select", size=10)
    return svg(760, 235, b, "The four operating modes")

@fig
def modules_lines():
    b = ""
    for i, name in enumerate("ABCD"):
        y = 15 + i * 78
        for j in range(2):
            b += box(30, y + j * 34, 150, 28, f"M{2*i+j+1}:  DCO → DCA")
        b += f'<path d="M180,{y+14} h14 v34 h-14" fill="none" stroke="{FG}" stroke-width="1.2"/>'
        b += L(194, y + 31, 260, y + 31, arrow=True) + T(275, y + 35, f"LINE {name}", w="bold") + L(320, y + 31, 340, y + 31)
    b += L(340, 46, 340, 280) + L(340, 163, 400, 163, arrow=True) + T(450, 167, "OUTPUT", w="bold")
    return svg(520, 330, b, "8 modules grouped in 4 internal lines")

@fig
def combine_modes():
    b = ""
    for k, (title, f) in enumerate([("MIX", "A = M1 + M2"), ("RING", "A = M2 + M1×M2"), ("PHASE", "A = M2(M1)")]):
        x = 10 + k * 250
        b += T(x + 110, 16, title, w="bold", size=14) + box(x, 30, 60, 28, "M1") + box(x, 90, 60, 28, "M2")
        if title == "MIX":
            b += L(x + 60, 44, x + 130, 74) + L(x + 60, 104, x + 130, 74) + L(x + 130, 74, x + 200, 74, arrow=True) + T(x + 130, 66, "+", size=16)
        elif title == "RING":
            b += L(x + 60, 44, x + 118, 74) + L(x + 60, 104, x + 118, 74) + f'<circle cx="{x+130}" cy="74" r="12" fill="#fff" stroke="{FG}"/>' + T(x + 130, 79, "×", size=15)
            b += L(x + 142, 74, x + 200, 74, arrow=True)
        else:
            b += L(x + 30, 58, x + 30, 90, arrow=True) + T(x + 40, 78, "phase", a="start", size=10) + L(x + 60, 104, x + 200, 104, arrow=True)
        b += T(x + 100, 150, f, size=13) + T(x + 215, 70 if title != "PHASE" else 100, "A", w="bold")
    return svg(760, 165, b, "MIX, RING and PHASE")

@fig
def ext_phase():
    b = box(10, 20, 60, 28, "M1") + box(10, 60, 60, 28, "M2") + R(100, 20, 120, 68, dash="5 3")
    b += T(160, 50, "LINE A", w="bold") + T(160, 68, "(silent)", size=11, fill=MUTE) + L(70, 34, 100, 50) + L(70, 74, 100, 60)
    b += box(10, 150, 60, 28, "M3") + box(10, 190, 60, 28, "M4") + R(100, 150, 120, 68)
    b += T(160, 180, "LINE B", w="bold") + T(160, 198, "heard", size=11) + L(70, 164, 100, 180) + L(70, 204, 100, 192)
    b += L(220, 54, 250, 54) + L(250, 54, 250, 125) + L(250, 125, 40, 125) + L(40, 125, 40, 188, arrow=True)
    b += T(300, 90, "EXT PHASE = ON:", a="start", w="bold") + T(300, 110, "line A output becomes the phase input of M4;", a="start", size=11) + T(300, 126, "line A itself does not sound.", a="start", size=11)
    b += L(220, 184, 290, 184, arrow=True) + T(300, 188, "OUT", a="start", w="bold")
    return svg(560, 235, b, "External phase: line A modulates line B")

def wave_val(kind, t, rnd):
    ph = t % 1
    return {"sine": math.sin(2 * math.pi * t), "triangle": (4 * ph - 1 if ph < .5 else 3 - 4 * ph),
            "saw up": 2 * ph - 1, "saw down": 1 - 2 * ph, "square": 1 if ph < .5 else -1, "noise": rnd.uniform(-1, 1)}[kind]
@fig
def waveforms():
    b = ""
    for k, name in enumerate(["sine", "triangle", "saw up", "saw down", "square", "noise"]):
        x, y = 20 + (k % 3) * 250, 50 + (k // 3) * 110
        rnd = random.Random(k)
        b += T(x + 100, y - 30, name, w="bold") + L(x, y, x + 200, y, stroke=MUTE, sw=.8)
        b += P([(x + i / 400 * 200, y - wave_val(name, i / 400 * 2, rnd) * 28) for i in range(401)])
    return svg(780, 235, b, "Basic waveforms")

@fig
def additive():
    b = T(190, 18, "Building a saw-tooth from sine partials", w="bold")
    for r, n in enumerate([1, 2, 4, 16]):
        y = 60 + r * 62
        pts = [(20 + i / 400 * 340, y - 14 * sum(math.sin(k * i / 400 * 4 * math.pi) / k for k in range(1, n + 1))) for i in range(401)]
        b += L(20, y, 360, y, stroke=MUTE, sw=.8) + P(pts) + T(372, y + 4, f"{n} partial{'s' if n > 1 else ''}", a="start", size=11)
    b += T(600, 18, "Harmonic spectra", w="bold")
    for r, (name, amps) in enumerate([("saw-tooth", [1 / k for k in range(1, 11)]), ("square", [1 / k if k % 2 else 0 for k in range(1, 11)])]):
        y0 = 120 + r * 110
        b += L(520, y0, 700, y0) + T(610, y0 + 16, name, size=11)
        for k, a in enumerate(amps):
            b += R(524 + k * 17, y0 - a * 60, 10, a * 60, fill=ACC, stroke="none", rx=0)
    return svg(740, 300, b, "Additive synthesis and harmonic spectra")

def env_plot(steps, x0, y0, w, h, title, hold=40):
    """steps = [(rate, level, flag)]; time per step is schematic: |dLevel| / rate."""
    t, lv, segs = 0, 0, []
    for n, (rate, lev, flag) in enumerate(steps, 1):
        t += max(abs(lev - lv), 1) * 100 / (rate + 4); lv = lev; segs.append((t, lev, n, rate, flag))
    sx = w / (t + hold)
    out = T(x0 + w / 2, y0 - h - 22, title, w="bold") + L(x0, y0, x0 + w, y0) + L(x0, y0, x0, y0 - h - 4)
    pts = [(x0, y0)]
    for tt, lvl, n, rate, flag in segs:
        x, y = x0 + tt * sx, y0 - lvl / 99 * h
        pts.append((x, y))
        if flag == "SS":
            pts.append((x + hold * .9 * sx, y)); out += T(x, y0 + 14, "SS", fill=ACC2, size=11, w="bold") + L(x, y0, x, y, stroke=ACC2, dash="3 3")
        if flag == "ED":
            out += T(x, y0 + 14, "ED", fill=ACC2, size=11, w="bold")
        out += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3" fill="{ACC}"/>' + T(x, y - 8, f"R{n}={rate} L{n}={lvl}", size=9)
    return out + P(pts)
@fig
def envelopes():
    b = env_plot([(87, 50, ""), (36, 99, ""), (70, 50, ""), (40, 99, "SS"), (20, 0, "ED")], 30, 190, 440, 120, "Tutorial DCA envelope (Example B)", 60)
    b += env_plot([(99, 99, ""), (25, 40, "SS"), (70, 0, "ED")], 520, 190, 220, 120, "Piano-like (illustrative)", 40)
    b += T(390, 232, "Time axis is schematic: duration = level change ÷ rate. SS = sustain point, ED = end point.", size=10, fill=MUTE)
    return svg(780, 245, b, "8-step envelope examples")

NOTE = {"C": 0, "D": 2, "E": 4, "F": 5, "G": 7, "A": 9, "B": 11}
def key_idx(s):
    m = re.match(r"([A-G])([#b]?)(\d)", s)
    return int(m.group(3)) * 12 + NOTE[m.group(1)] + {"#": 1, "b": -1, "": 0}[m.group(2)]
def kf_panel(y0, title, keys, levs, lo, hi, unit, color=ACC):
    x0, w, h = 50, 640, 110
    o = T(x0 + w / 2, y0 - h - 14, title, w="bold") + L(x0, y0, x0 + w, y0) + L(x0, y0, x0, y0 - h)
    for c in range(10):
        x = x0 + c * 12 / 108 * w
        o += L(x, y0, x, y0 + 4) + T(x, y0 + 16, f"C{c}", size=9)
    sy = lambda v: y0 - (v - lo) / (hi - lo) * h
    pts = [(x0, sy(levs[0]))] + [(x0 + key_idx(k) / 108 * w, sy(v)) for k, v in zip(keys, levs)] + [(x0 + w, sy(levs[-1]))]
    o += P(pts, stroke=color)
    for i, (k, v) in enumerate(zip(keys, levs), 1):
        x = x0 + key_idx(k) / 108 * w
        o += f'<circle cx="{x:.1f}" cy="{sy(v):.1f}" r="3.5" fill="{color}"/>' + T(x, sy(v) - 8, f"P{i} {k}", size=9)
    return o + T(x0 - 6, y0 + 4, lo, a="end", size=9) + T(x0 - 6, y0 - h + 4, hi, a="end", size=9) + T(x0 + w + 8, y0 - h / 2, unit, a="start", size=10)
@fig
def kf_curves():
    b = kf_panel(150, "KF LEVEL (DCO) 1-05: pitch-envelope depth", ["E2", "C4", "A4", "C6", "Ab6", "F#7"], [50, 25, 63, 36, 57, 28], 0, 63, "level")
    b += kf_panel(330, "KF LEVEL (DCA) 1-11: amplitude-envelope level", ["E2", "C4", "A4", "C6", "Ab6", "F#7"], [79, 40, 99, 56, 90, 44], 0, 99, "level", ACC2)
    b += kf_panel(510, "KF RATE 1-16: envelope speed (signed)", ["C1", "A1", "E2", "C5", "Ab6", "F7"], [22, 50, 0, 22, 53, 99], -99, 99, "rate", "#059669")
    return svg(780, 545, b, "Key-follow curve examples")

@fig
def velocity_curves():
    f = {1: lambda v: v ** 3, 2: lambda v: v ** 2, 3: lambda v: v, 4: lambda v: 1 - v, 5: lambda v: v ** .4,
         6: lambda v: .5 * (1 - math.cos(math.pi * v)), 7: lambda v: 0 if v < .5 else 1, 8: lambda v: 1 if v < .5 else 0}
    b = ""
    for n in range(1, 9):
        x, y = 30 + ((n - 1) % 4) * 185, 40 + ((n - 1) // 4) * 140
        b += T(x + 65, y - 14, f"CURVE {n}", w="bold") + L(x, y + 90, x + 130, y + 90) + L(x, y + 90, x, y)
        b += P([(x + i / 100 * 130, y + 90 - f[n](i / 100) * 90) for i in range(101)])
    b += T(390, 312, "Schematic shapes redrawn from the original diagrams (x = key velocity, y = effect amount).", size=10, fill=MUTE)
    return svg(780, 322, b, "The 8 velocity curves")

@fig
def key_assign():
    cfgs = [["1+2"], ["3+4"], ["1+2+3+4"], ["1", "3"], ["1", "3+4"], ["1+2", "3"], ["1+2", "3+4"], ["1", "2", "3", "4"]]
    b = ""
    for i, c in enumerate(cfgs):
        x, y = 20 + (i % 2) * 380, 20 + (i // 2) * 48
        w = 340 / len(c)
        for j, z in enumerate(c):
            b += box(x + j * w, y, w, 30, z, fill=FILL if j % 2 == 0 else "#fef3c7")
    b += T(390, 225, "Boxes are keyboard zones, low → high. “+” = layered patches, “/” = split point.", size=10, fill=MUTE)
    return svg(780, 235, b, "The 8 key-assign configurations")

@fig
def xfade():
    X = [0, .2, .3, .45, .55, .7, .8, 1]
    shapes = [[(X[0], 1), (X[1], 1), (X[2], 0)], [(X[1], 0), (X[2], 1), (X[3], 1), (X[4], 0)],
              [(X[3], 0), (X[4], 1), (X[5], 1), (X[6], 0)], [(X[5], 0), (X[6], 1), (X[7], 1)]]
    b = L(40, 130, 700, 130) + L(40, 130, 40, 20)
    for i, s in enumerate(shapes):
        b += P([(40 + x * 660, 130 - y * 100) for x, y in s], stroke=[ACC, ACC2, "#059669", "#d97706"][i], sw=2.5)
        b += T(40 + (s[1][0] + s[-2][0]) / 2 * 660, 118, i + 1, w="bold")
    for k in range(40):
        b += R(40 + k * 16.5, 142, 14, 26, fill="#fff", rx=1, sw=.7)
    return svg(740, 195, b + T(370, 188, "Four layered patches fading into one another along the keyboard", size=11, fill=MUTE), "Positional cross-fade")

@fig
def front_panel():
    b = R(10, 10, 980, 320, fill="#f3f4f6", rx=8, sw=2)
    for i, n in enumerate([16, 17, 18]):
        b += R(25 + i * 35, 40, 24, 110, fill="#d1d5db") + callout(37 + i * 35, 36, n)
    b += R(150, 18, 110, 18, fill="#fff") + callout(205, 27, 1) + R(160, 70, 24, 70, fill="#d1d5db") + callout(172, 64, 2)
    for i, n in enumerate([3, 4, 5, 6, 7]):
        b += R(205 + i * 46, 72, 36, 16) + callout(223 + i * 46, 66, n)
    for i, n in enumerate([19, 20, 21]):
        b += R(205 + i * 46 * (1 if n == 19 else 1), 108, 36, 16)
    b += callout(260, 102, 19) + R(297, 108, 36, 16) + R(343, 108, 36, 16) + callout(343, 102, 20) + R(389, 108, 36, 16) + callout(425, 102, 21)
    b += R(480, 55, 24, 90, fill="#d1d5db") + callout(492, 49, 22) + R(520, 108, 28, 16) + R(552, 108, 28, 16) + callout(550, 102, 23)
    b += R(520, 66, 28, 16) + R(552, 66, 28, 16) + callout(550, 60, 8) + R(610, 25, 150, 105, fill="#a7f3d0") + callout(685, 20, 9) + T(685, 82, "64×96 LCD", size=11)
    for i, n in enumerate([10, 11, 12, 13, 24]):
        b += R(790 + i * 36, 70, 28, 14) + callout(804 + i * 36, 64, n)
    b += R(790, 18, 190, 28, fill="#fff") + callout(885, 14, 14)
    for r in range(2):
        for k in range(8):
            b += R(612 + k * 46, 150 + r * 28, 36, 16, fill="#fff")
    b += callout(596, 158, 26) + callout(596, 186, 25) + R(25, 175, 60, 14, fill="#fff") + callout(110, 182, 15) + R(20, 235, 960, 85, fill="#fff")
    for k in range(36):
        b += L(20 + k * 26.7, 235, 20 + k * 26.7, 320, sw=.8)
        if k % 7 not in (2, 6):
            b += R(20 + k * 26.7 + 18, 235, 16, 52, fill=FG, rx=1)
    return svg(1000, 340, b, "Front panel (schematic)")

@fig
def rear_panel():
    b = R(10, 10, 900, 100, fill="#f3f4f6", rx=6, sw=2)
    for x, n, lab in [(60, "1", "POWER"), (130, "2", "AC IN"), (400, "3", "FOOT VR"), (450, "4", "PROG NO"), (560, "5", "MIDI THRU/OUT/IN"),
                      (640, "6", "MIDI ON/OFF"), (690, "7", "FOOT VOL"), (740, "8", "SUSTAIN"), (800, "9", "LINE OUT 1 2"), (870, "10", "MIX OUT")]:
        b += R(x - 14, 50, 28, 24, fill="#fff") + callout(x, 38, n) + T(x, 92, lab, size=8)
    return svg(920, 120, b, "Rear panel (schematic)")

@fig
def midi_setups():
    dev = lambda x, y, t: box(x, y, 110, 34, t)
    b = T(165, 16, "A: master keyboard", w="bold") + dev(20, 30, "VZ-1") + dev(200, 30, "FZ-10M") + L(130, 47, 200, 47, arrow=True) + T(165, 40, "OUT→IN", size=9)
    b += T(165, 106, "B: slave", w="bold") + dev(20, 120, "VZ-1") + dev(200, 120, "Drum machine") + L(200, 137, 130, 137, arrow=True) + T(165, 130, "OUT→IN", size=9)
    b += T(540, 16, "C: chain (THRU)", w="bold") + dev(380, 30, "Sequencer") + dev(540, 30, "VZ-1") + dev(700, 30, "Drum machine")
    b += L(490, 47, 540, 47, arrow=True) + L(650, 47, 700, 47, arrow=True) + T(515, 40, "OUT→IN", size=9) + T(675, 40, "THRU→IN", size=9)
    return svg(830, 175, b, "MIDI hook-ups")

if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    for name, fn in FIGS.items():
        (OUT / f"{name}.svg").write_text(fn(), encoding="utf-8")
    print(f"{len(FIGS)} figures written to {OUT}")
