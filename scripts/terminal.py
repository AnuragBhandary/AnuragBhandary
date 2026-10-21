"""Draw assets/chaos-{dark,light}.svg: a terminal replaying the chaos run of my job scheduler.

The numbers are from Distributed-Job-Scheduler/docs/BENCHMARKS.md (run 1: 50,000 jobs at
2,000/min, a random worker SIGKILLed every 60 s). The command types itself, the output appears
line by line, and the whole thing loops. Run: python3 scripts/terminal.py
"""

from svgkit import MONO, THEMES, esc, font_faces, write

W, LOOP, FS, LH = 840, 20.0, 13, 22
CH = FS * 0.6  # IBM Plex Mono advance is 600/1000 em
CMD = "uv run python bench/run_benchmark.py --jobs 50000 --rate 2000 --chaos-interval 60"
# (tag, tag colour key, text, text colour key)
OUT = [
    ("[load] ", "muted", "enqueuing 50,000 jobs at 2,000/min, 5% of attempts fail on purpose", "muted"),
    ("[chaos]", "pink", "SIGKILL random worker (1/23), restarted 5 s later", "text"),
    ("[chaos]", "pink", "SIGKILL random worker (2/23), restarted 5 s later", "text"),
    ("[chaos]", "pink", "...", "dim"),
    ("[chaos]", "pink", "SIGKILL random worker (23/23), 41 leases expired, reaped, re-run", "text"),
    ("[retry]", "yellow", "2,633 transient failures retried, all recovered", "text"),
    ("[audit]", "cyan", "counting ledger rows in PostgreSQL", "muted"),
    ("       ", "muted", "50,000 succeeded · 0 dead · 0 duplicate effects · 0 missing", "cyan"),
    ("       ", "muted", "p95 enqueue latency 7.1 ms", "muted"),
    ("PASS ", "ok", "no job lost while a worker died every minute", "ok"),
]
TYPE_START, TYPE_END, FIRST_OUT, STEP, FADE = 0.8, 4.0, 4.6, 0.9, 18.6


def pct(t):
    return f"{100 * t / LOOP:.2f}%"


def render(theme):
    t = THEMES[theme]
    x0, y0 = 28, 78
    H = y0 + LH * (len(OUT) + 1) + 26
    css, body = [], []
    # title bar
    body += [f'<rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="14" fill="{t["panel"]}" stroke="{t["line"]}"/>',
             f'<path d="M1 40 H{W - 1}" stroke="{t["line"]}"/>']
    for i, c in enumerate(("#ff5f57", "#febc2e", "#28c840")):
        body.append(f'<circle cx="{24 + i * 20}" cy="20" r="6" fill="{c}"/>')
    body.append(f'<text x="{W / 2}" y="25" text-anchor="middle" font-size="12.5" fill="{t["muted"]}">'
                f'jobq · chaos run · Distributed-Job-Scheduler</text>')
    # command line: prompt, then a cover rect that slides right in character steps
    body.append(f'<text x="{x0}" y="{y0}" fill="{t["ok"]}" font-weight="600">$</text>')
    cx = x0 + 2 * CH
    body.append(f'<text x="{cx}" y="{y0}" fill="{t["text"]}">{esc(CMD)}</text>')
    span = len(CMD) * CH
    css.append(f"@keyframes type{{0%,{pct(TYPE_START)}{{transform:translateX(0)}}"
               f"{pct(TYPE_END)},100%{{transform:translateX({span:.1f}px)}}}}"
               f".type{{animation:type {LOOP}s steps(1) infinite}}")
    # steps() must cover only the typing window, so key one frame per character instead
    frames = [f"{pct(TYPE_START + (TYPE_END - TYPE_START) * k / len(CMD))}{{transform:translateX({k * CH:.1f}px)}}"
              for k in range(len(CMD) + 1)]
    css[-1] = (f"@keyframes type{{0%{{transform:translateX(0)}}{''.join(frames)}100%{{transform:translateX({span:.1f}px)}}}}"
               f".type{{animation:type {LOOP}s steps(1,end) infinite}}")
    body.append(f'<g class="type"><rect x="{cx}" y="{y0 - FS - 2}" width="{span + 20:.1f}" height="{LH}" fill="{t["panel"]}"/>'
                f'<rect x="{cx}" y="{y0 - FS + 1}" width="{CH:.1f}" height="{FS + 3}" fill="{t["cyan"]}"/></g>')
    # output lines
    for i, (tag, tag_c, text, text_c) in enumerate(OUT):
        y = y0 + LH * (i + 1) + 6
        at = FIRST_OUT + STEP * i
        css.append(f"@keyframes o{i}{{0%,{pct(at)}{{opacity:0}}{pct(at + .01)},{pct(FADE)}{{opacity:1}}{pct(FADE + .6)},100%{{opacity:0}}}}"
                   f".o{i}{{animation:o{i} {LOOP}s steps(1,end) infinite}}")
        weight = ' font-weight="600"' if tag_c == "ok" else ""
        mark = "✔ " if tag_c == "ok" else ""
        body.append(f'<text class="o{i}" x="{x0}" y="{y}"{weight}><tspan fill="{t[tag_c]}">{esc(mark + tag)}</tspan>'
                    f'<tspan fill="{t[text_c]}"> {esc(text)}</tspan></text>')
    # the command fades with the output, then the loop restarts
    css.append(f"@keyframes cmd{{0%,{pct(FADE)}{{opacity:1}}{pct(FADE + .6)},100%{{opacity:0}}}}"
               f".cmd{{animation:cmd {LOOP}s steps(1,end) infinite}}")
    body[6:] = ['<g class="cmd">'] + body[6:9] + ["</g>"] + body[9:]
    text = "$" + CMD + "".join("✔ " + a + " " + b for a, _, b, _ in OUT) + "jobq · chaos run · Distributed-Job-Scheduler…"
    style = (font_faces(text, [("IBM Plex Mono", 400), ("IBM Plex Mono", 600)]) +
             f"text{{font-family:{MONO};font-size:{FS}px;white-space:pre}}" + "".join(css) +
             "@media (prefers-reduced-motion:reduce){*{animation:none!important}.type{display:none}}")
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" '
            f'aria-label="Chaos test: 50,000 jobs with a worker killed every minute, 0 lost, 0 duplicates">'
            f'<title>Chaos run: 50,000 jobs, 23 worker kills, 0 lost, 0 duplicate effects</title>'
            f'<style>{style}</style>' + "".join(body) + "</svg>\n")


if __name__ == "__main__":
    for theme in THEMES:
        write("chaos", theme, render(theme))
    print("chaos-dark.svg, chaos-light.svg")
