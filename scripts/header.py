"""Draw assets/header-{dark,light}.svg: my name with the glitch effect from my portfolio.

The same chromatic ghosts (a cyan and a pink copy that jump out of place for a few frames) and the
occasional slice, as CSS keyframes, so GitHub plays them. Run: python3 scripts/header.py
"""

from fontTools.ttLib import TTFont

from svgkit import DISPLAY, FONTS, MONO, THEMES, esc, font_faces, write

W, H = 840, 230
WORDS = [("ANURAG", False), ("NAVIN", True), ("BHANDARY", False)]
ROLE = "BACKEND ENGINEER · SYSTEMS THAT SURVIVE FAILURE"
STATUS = "open to work · relocation worldwide"
# ghost A / ghost B timings per word, as on the portfolio (6.5/4.7, 5.9/5.3 swapped, 7.3/6.1)
TIMING = [("gA", 6.5, "gB", 4.7), ("gB", 5.9, "gA", 5.3), ("gA", 7.3, "gB", 6.1)]

KEYFRAMES = """
@keyframes gA{0%,90%,100%{opacity:0;transform:translate(0,0)}91%{opacity:.52;transform:translate(-7px,2px)}
93%{opacity:.36;transform:translate(6px,-3px)}95%{opacity:.47;transform:translate(-3px,1px)}97%{opacity:0;transform:translate(0,0)}}
@keyframes gB{0%,92%,100%{opacity:0;transform:translate(0,0)}93%{opacity:.52;transform:translate(6px,-2px)}
95%{opacity:.36;transform:translate(-5px,3px)}96.5%{opacity:.44;transform:translate(3px,-1px)}98%{opacity:0;transform:translate(0,0)}}
@keyframes slice{0%,93%,100%{clip-path:inset(0 0 0 0);transform:translate(0)}93.5%{clip-path:inset(38% 0 44% 0);transform:translate(-9px)}
94.5%{clip-path:inset(70% 0 10% 0);transform:translate(7px)}95.5%{clip-path:inset(12% 0 76% 0);transform:translate(-4px)}}
@keyframes rise{from{opacity:0;transform:translateY(14px)}to{opacity:1;transform:none}}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.25}}
@keyframes blink{50%{opacity:0}}
"""


def render(theme):
    t = THEMES[theme]
    x = 40
    font = TTFont(FONTS / "BebasNeue-Regular.ttf")
    cmap, hmtx, upm = font.getBestCmap(), font["hmtx"], font["head"].unitsPerEm

    def em(s):  # width in em, including the .02em letter-spacing
        return sum(hmtx[cmap[ord(c)]][0] / upm + .02 for c in s)

    # largest size at which the three words, the gaps (.25em) and the cursor (.3em) fit the card
    total_em = sum(em(w) for w, _ in WORDS) + .25 * (len(WORDS) - 1) + .3
    name_size = min(104, int((W - 2 * x) / total_em))
    gap = .25 * name_size

    def width(s):
        return em(s) * name_size

    words, cx = [], x
    for i, (word, accent) in enumerate(WORDS):
        a_name, a_dur, b_name, b_dur = TIMING[i]
        base = t["cyan_ink"] if accent else t["text"]
        y = 150
        words.append(
            f'<g class="w" style="animation-delay:{0.1 + i * 0.12:.2f}s">'
            f'<text class="g" x="{cx:.1f}" y="{y}" fill="{t["cyan"]}" style="animation:{a_name} {a_dur}s infinite">{word}</text>'
            f'<text class="g" x="{cx:.1f}" y="{y}" fill="{t["pink"]}" style="animation:{b_name} {b_dur}s infinite">{word}</text>'
            f'<text x="{cx:.1f}" y="{y}" fill="{base}">{word}</text></g>')
        cx += width(word) + gap
    text = "".join(w for w, _ in WORDS) + ROLE + STATUS
    css = (font_faces(text, [("Bebas Neue", 400), ("IBM Plex Mono", 400), ("IBM Plex Mono", 600)]) + KEYFRAMES +
           f"text{{font-family:{DISPLAY}}}.mono{{font-family:{MONO}}}"
           f".name{{font-size:{name_size}px;letter-spacing:.02em;animation:slice 9s steps(1) 3s infinite}}"
           f".g{{mix-blend-mode:{t['blend']};opacity:0}}"
           f".w{{animation:rise .9s cubic-bezier(.2,.7,.1,1) both}}"
           ".dot{animation:pulse 1.6s ease-in-out infinite}.cur{animation:blink 1.1s steps(1) infinite}"
           "@media (prefers-reduced-motion:reduce){*{animation:none!important}.g{opacity:0}}")
    scan = ""
    if theme == "dark":
        scan = ('<pattern id="scan" width="4" height="3" patternUnits="userSpaceOnUse">'
                f'<rect y="2" width="4" height="1" fill="{t["cyan"]}" opacity=".035"/></pattern>')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" '
            f'aria-label="Anurag Navin Bhandary, backend engineer"><title>Anurag Navin Bhandary</title>'
            f'<style>{css}</style><defs>{scan}</defs>'
            f'<rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="18" fill="{t["panel"]}" stroke="{t["line"]}"/>'
            + (f'<rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="18" fill="url(#scan)"/>' if scan else "")
            + f'<rect x="{x}" y="38" width="22" height="2" fill="{t["cyan_ink"]}"/>'
            f'<text class="mono" x="{x + 32}" y="43" font-size="13" font-weight="600" letter-spacing="1.5" fill="{t["muted"]}">{esc(ROLE)}</text>'
            f'<circle class="dot" cx="{x + 4}" cy="{H - 42}" r="4" fill="{t["ok"]}"/>'
            f'<text class="mono" x="{x + 16}" y="{H - 38}" font-size="13" fill="{t["muted"]}">{esc(STATUS)}</text>'
            f'<g class="name">{"".join(words)}</g>'
            f'<rect class="cur" x="{cx - gap + .06 * name_size:.1f}" y="{150 - .16 * name_size:.1f}" width="{.16 * name_size:.1f}" height="{.16 * name_size:.1f}" fill="{t["pink"]}"/>'
            "</svg>\n")


if __name__ == "__main__":
    for theme in THEMES:
        write("header", theme, render(theme))
    print("header-dark.svg, header-light.svg")
