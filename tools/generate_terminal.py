from pathlib import Path
import html

ROOT = Path(__file__).resolve().parent.parent

OUTPUT = ROOT / "assets" / "terminal.svg"

WIDTH = 900
HEIGHT = 420

LINES = [
    "$ git status",
    "On branch main",
    "Your branch is up to date with 'origin/main'.",
    "",
    "$ python tools/build.py",
    "[1/6] preprocess.py      ✓",
    "[2/6] trace.py           ✓",
    "[3/6] optimize_svg.py    ✓",
    "[4/6] animate_svg.py     ✓",
    "[5/6] generate_readme.py ✓",
    "[6/6] README.md          ✓",
    "",
    "Build completed successfully.",
    "$ _"
]


def make_svg():

    y = 55

    text = []

    for line in LINES:

        safe = html.escape(line)

        text.append(
            f'<text x="20" y="{y}" '
            f'font-family="Consolas,monospace" '
            f'font-size="20" '
            f'fill="#d4d4d4">{safe}</text>'
        )

        y += 28

    svg = f'''<?xml version="1.0" encoding="UTF-8"?>

<svg xmlns="http://www.w3.org/2000/svg"
     width="{WIDTH}"
     height="{HEIGHT}"
     viewBox="0 0 {WIDTH} {HEIGHT}">

<rect width="100%" height="100%" rx="14" fill="#1e1e1e"/>

<circle cx="24" cy="22" r="7" fill="#ff5f56"/>
<circle cx="46" cy="22" r="7" fill="#ffbd2e"/>
<circle cx="68" cy="22" r="7" fill="#27c93f"/>

{chr(10).join(text)}

</svg>
'''

    OUTPUT.write_text(svg, encoding="utf-8")


if __name__ == "__main__":

    make_svg()

    print(f"Generated: {OUTPUT}")