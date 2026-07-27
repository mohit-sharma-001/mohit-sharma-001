from pathlib import Path
import xml.etree.ElementTree as ET

from svgpathtools import parse_path


ROOT = Path(__file__).resolve().parent.parent

INPUT = ROOT / "assets" / "portrait_clean.svg"
OUTPUT = ROOT / "assets" / "portrait_animated.svg"

SVG_NS = "http://www.w3.org/2000/svg"

ET.register_namespace("", SVG_NS)


CSS = """
<style>

path{

fill:none;

stroke:#000;

stroke-width:2;

stroke-linecap:round;

stroke-linejoin:round;

animation:draw 4s linear forwards;

}

@keyframes draw{

to{

stroke-dashoffset:0;

}

}

</style>
"""


def animate():

    tree = ET.parse(INPUT)

    root = tree.getroot()

    ns = {"svg": SVG_NS}

    style = ET.fromstring(CSS)

    root.insert(0, style)

    delay = 0.0

    for path in root.findall(".//svg:path", ns):

        d = path.attrib.get("d")

        if not d:
            continue

        try:

            length = parse_path(d).length()

        except Exception:

            continue

        path.set("fill", "none")
        path.set("stroke", "#000000")
        path.set("stroke-width", "2")

        path.set("stroke-dasharray", f"{length:.2f}")
        path.set("stroke-dashoffset", f"{length:.2f}")

        path.set(
            "style",
            f"animation-delay:{delay:.2f}s;"
        )

        delay += 0.08

    tree.write(
        OUTPUT,
        encoding="utf-8",
        xml_declaration=True,
    )

    print("=" * 60)
    print("Animation Complete")
    print(OUTPUT)
    print("=" * 60)


if __name__ == "__main__":
    animate()