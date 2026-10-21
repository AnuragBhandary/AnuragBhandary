"""Draw assets/leetcode-{dark,light}.svg: an animated copy of the LeetCode card on my portfolio.

GitHub strips JavaScript from READMEs but plays CSS animations inside an SVG image, so the
ring, bars and heatmap animate here too. Stats come from the JSON my portfolio already
refreshes every 6 hours. Run by .github/workflows/leetcode-card.yml, or by hand:
python3 scripts/leetcode_card.py
"""

import json
import math
import time
import urllib.request
from datetime import datetime, timezone

from svgkit import DISPLAY, EASE, MONO, THEMES, font_faces, write

SRC = "https://anuragbhandary.github.io/assets/data/leetcode.json"
DIFFS = [("Easy", "Easy", "easy"), ("Medium", "Med.", "med"), ("Hard", "Hard", "hard")]
W, H = 840, 450


def ring(d, css, t):
    """Three arcs sized by each difficulty's share of all questions, filled by the share solved."""
    cx, cy, r, start, sweep, gap = 130, 168, 84, 135, 270, 7
    total = sum(d["total"][k] for k, _, _ in DIFFS)
    usable = sweep - gap * (len(DIFFS) - 1)

    def pt(a):
        t = math.radians(a)
        return cx + r * math.cos(t), cy + r * math.sin(t)

    out, a0 = [], start
    for i, (key, _, ck) in enumerate(DIFFS):
        color = t[ck]
        span = usable * d["total"][key] / total
        a1 = a0 + span
        (x0, y0), (x1, y1) = pt(a0), pt(a1)
        path = f"M{x0:.2f} {y0:.2f} A{r} {r} 0 {1 if span > 180 else 0} 1 {x1:.2f} {y1:.2f}"
        length = r * math.radians(span)
        frac = min(1, d["solved"][key] / max(1, d["total"][key]))
        css.append(f"@keyframes arc{i}{{from{{stroke-dashoffset:{length:.2f}}}to{{stroke-dashoffset:{length * (1 - frac):.2f}}}}}"
                   f".arc{i}{{stroke-dasharray:{length:.2f} {length + 10:.2f};stroke-dashoffset:{length * (1 - frac):.2f};"
                   f"animation:arc{i} 1.8s {EASE} {0.2 + i * 0.15:.2f}s both}}")
        out.append(f'<path d="{path}" fill="none" stroke="{t["line"]}" stroke-width="9" stroke-linecap="round"/>')
        out.append(f'<path class="arc{i}" d="{path}" fill="none" stroke="{color}" stroke-width="9" '
                   f'stroke-linecap="round" color="{color}" filter="url(#glow)"/>')
        a0 = a1 + gap
    out.append(f'<text class="fade" x="{cx}" y="{cy + 12}" text-anchor="middle" font-family="{DISPLAY}" '
               f'font-size="60" fill="{t["text"]}">{d["solved"]["All"]}</text>')
    out.append(f'<text class="fade" x="{cx}" y="{cy + 34}" text-anchor="middle" font-family="{MONO}" '
               f'font-size="13" fill="{t["muted"]}">/{d["total"]["All"]}</text>')
    out.append(f'<text class="fade" x="{cx}" y="{cy + 54}" text-anchor="middle" font-family="{MONO}" '
               f'font-size="12" fill="{t["cyan_ink"]}">✓ Solved</text>')
    return out


def bars(d, css, t):
    x, w, h, y0 = 270, 540, 56, 92
    out = []
    for i, (key, label, ck) in enumerate(DIFFS):
        color = t[ck]
        y = y0 + i * (h + 10)
        frac = min(1, d["solved"][key] / max(1, d["total"][key]))
        bw = max(5, (w - 28) * frac)
        css.append(f".bar{i}{{transform-box:fill-box;transform-origin:left;animation:grow 1.6s {EASE} {0.3 + i * 0.15:.2f}s both}}")
        out += [
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{t["bg"]}" stroke="{t["line"]}"/>',
            f'<text x="{x + 14}" y="{y + 24}" font-family="{MONO}" font-size="13" font-weight="600" fill="{color}">{label}</text>',
            f'<text x="{x + w - 14}" y="{y + 24}" text-anchor="end" font-family="{MONO}" font-size="15" fill="{t["text"]}">'
            f'{d["solved"][key]}<tspan fill="{t["muted"]}" font-size="12" dx="3">/{d["total"][key]}</tspan></text>',
            f'<rect x="{x + 14}" y="{y + 38}" width="{w - 28}" height="5" rx="2.5" fill="{t["line"]}"/>',
            f'<rect class="bar{i}" x="{x + 14}" y="{y + 38}" width="{bw:.1f}" height="5" rx="2.5" fill="{color}"/>',
        ]
    return out


def heatmap(d, t):
    """52 weeks, columns are weeks and rows Sun..Sat, same levels as the portfolio."""
    weeks, cell, gap, x0, y0 = 52, 12, 3, 31, 300
    easy, line = t["easy"], t["line"]
    shades = [line, mix(easy, line, .35), mix(easy, line, .60), mix(easy, line, .82), easy]
    now = datetime.now(timezone.utc)
    today = int(datetime(now.year, now.month, now.day, tzinfo=timezone.utc).timestamp())
    dow = (datetime.fromtimestamp(today, timezone.utc).weekday() + 1) % 7  # Sunday = 0
    first = today - ((weeks - 1) * 7 + dow) * 86400
    out = []
    for c in range(weeks):
        for r in range(7):
            ts = first + (c * 7 + r) * 86400
            if ts > today:
                continue
            n = d["calendar"].get(str(ts), 0)
            lvl = 0 if n == 0 else 1 if n <= 2 else 2 if n <= 5 else 3 if n <= 9 else 4
            out.append(f'<rect class="hc" style="animation-delay:{c * 18}ms" x="{x0 + c * (cell + gap)}" '
                       f'y="{y0 + r * (cell + gap)}" width="{cell}" height="{cell}" rx="2.5" fill="{shades[lvl]}"/>')
    return out


def mix(a, b, t):
    pa, pb = (int(a[i:i + 2], 16) for i in (1, 3, 5)), (int(b[i:i + 2], 16) for i in (1, 3, 5))
    return "#" + "".join(f"{round(x * t + y * (1 - t)):02x}" for x, y in zip(pa, pb))


def render(d, theme):
    t = THEMES[theme]
    css = [f"@keyframes grow{{from{{transform:scaleX(0)}}to{{transform:scaleX(1)}}}}",
           "@keyframes fade{from{opacity:0}to{opacity:1}}",
           f"@keyframes pop{{from{{opacity:0;transform:scale(.4)}}to{{opacity:1;transform:none}}}}",
           f".fade{{animation:fade 1s {EASE} .4s both}}",
           f".hc{{transform-box:fill-box;transform-origin:center;animation:pop .5s {EASE} both}}"]
    body = ring(d, css, t) + bars(d, css, t) + heatmap(d, t)
    meta_y = H - 20
    rank = f'{d["ranking"]:,}'
    body += [
        f'<text x="30" y="44" font-family="{MONO}" font-size="13" letter-spacing="1.5" fill="{t["muted"]}">'
        f'<tspan fill="{t["cyan_ink"]}" font-weight="600">LC</tspan>  PROBLEM SOLVING</text>',
        f'<text x="{W - 30}" y="44" text-anchor="end" font-family="{MONO}" font-size="13" fill="{t["cyan_ink"]}">@{d["username"]} ↗</text>',
        f'<text x="30" y="{meta_y}" font-family="{MONO}" font-size="12.5" fill="{t["muted"]}">'
        f'<tspan fill="{t["text"]}">{d["streak"]}</tspan> day streak    '
        f'<tspan fill="{t["text"]}">{d["activeDays"]}</tspan> active days    '
        f'rank <tspan fill="{t["text"]}">{rank}</tspan></text>',
    ]
    css.append("@media (prefers-reduced-motion:reduce){*{animation:none!important}}")
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
            f'role="img" aria-label="LeetCode: {d["solved"]["All"]} problems solved">'
            f'<title>LeetCode: {d["solved"]["All"]} solved ({d["solved"]["Easy"]} easy, '
            f'{d["solved"]["Medium"]} medium, {d["solved"]["Hard"]} hard)</title>'
            f'<style>{fonts(d)}{"".join(css)}</style>'
            '<defs><filter id="glow" x="-20%" y="-20%" width="140%" height="140%">'
            '<feDropShadow dx="0" dy="0" stdDeviation="3" flood-opacity=".6" flood-color="currentColor"/></filter></defs>'
            f'<rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="18" fill="{t["panel"]}" stroke="{t["line"]}"/>'
            + "".join(body) + "</svg>\n")


def fonts(d):
    digits = "0123456789,/@.↗✓ " + d["username"]
    words = "LC PROBLEM SOLVING Solved Easy Med. Hard day streak active days rank"
    return font_faces(digits + words, [("Bebas Neue", 400), ("IBM Plex Mono", 400), ("IBM Plex Mono", 600)])


def main():
    req = urllib.request.Request(f"{SRC}?t={int(time.time())}", headers={"User-Agent": "profile-readme"})
    with urllib.request.urlopen(req, timeout=30) as r:
        d = json.load(r)
    for theme in THEMES:
        write("leetcode", theme, render(d, theme))
    print("solved", d["solved"], "-> leetcode-dark.svg, leetcode-light.svg")


if __name__ == "__main__":
    main()
