"""Shared bits for the README's SVGs: my portfolio's two colour themes and its fonts.

GitHub shows README SVGs as images, which can't load web fonts, so each SVG carries a subset of
the fonts it uses (only the characters it needs) as base64 WOFF2. Fonts are OFL, see fonts/.
"""

import base64
import io
import logging
from pathlib import Path

from fontTools import subset
from fontTools.ttLib import TTFont

logging.getLogger("fontTools").setLevel(logging.ERROR)
FONTS = Path(__file__).resolve().parent / "fonts"
ASSETS = Path(__file__).resolve().parent.parent / "assets"
EASE = "cubic-bezier(.2,.7,.1,1)"

THEMES = {
    "dark": dict(bg="#07090d", panel="#0f141c", line="#1c2533", line2="#2a3548", text="#e7ebf2",
                 muted="#8c96aa", dim="#5a6477", cyan="#00e5ff", cyan_ink="#00e5ff", pink="#ff3c6e",
                 yellow="#ffe600", easy="#1cbbba", med="#ffb800", hard="#f63737", blend="screen", ok="#3ddc84"),
    "light": dict(bg="#eef1f4", panel="#ffffff", line="#d6dce4", line2="#c1c9d4", text="#0b0f16",
                  muted="#4e586a", dim="#7c8697", cyan="#00c8e0", cyan_ink="#007a8c", pink="#e8285e",
                  yellow="#c9a800", easy="#0e9f9e", med="#d99a00", hard="#e02424", blend="multiply", ok="#1a9e55"),
}

DISPLAY = "'Bebas Neue',Impact,sans-serif"
MONO = "'IBM Plex Mono',ui-monospace,Menlo,monospace"
_FILES = {("Bebas Neue", 400): "BebasNeue-Regular.ttf",
          ("IBM Plex Mono", 400): "IBMPlexMono-Regular.ttf",
          ("IBM Plex Mono", 600): "IBMPlexMono-SemiBold.ttf"}


def font_faces(text, faces):
    """@font-face rules for `faces` [(family, weight)], each subset to the characters in `text`."""
    rules = []
    for family, weight in faces:
        font = TTFont(FONTS / _FILES[(family, weight)])
        sub = subset.Subsetter(subset.Options(flavor="woff2", layout_features=["kern"], name_IDs=[], hinting=False))
        sub.populate(text=text + " ")
        sub.subset(font)
        font.flavor = "woff2"
        buf = io.BytesIO()
        font.save(buf)
        b64 = base64.b64encode(buf.getvalue()).decode()
        rules.append(f"@font-face{{font-family:'{family}';font-weight:{weight};"
                     f"src:url(data:font/woff2;base64,{b64}) format('woff2')}}")
    return "".join(rules)


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def write(name, theme, svg):
    ASSETS.mkdir(exist_ok=True)
    (ASSETS / f"{name}-{theme}.svg").write_text(svg)
