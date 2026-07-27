from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent.parent

INPUT = ROOT / "assets" / "portrait.svg"
OUTPUT = ROOT / "assets" / "portrait_clean.svg"

SVG_NS = "http://www.w3.org/2000/svg"
ET.register_namespace("", SVG_NS)


def path_length(d: str) -> int:
    return len(d.strip())


def optimize():

    tree = ET.parse(INPUT)
    root = tree.getroot()

    ns = {"svg": SVG_NS}

    # remove metadata
    for meta in root.findall("svg:metadata", ns):
        root.remove(meta)

    removed = 0

    for group in root.findall(".//svg:g", ns):

        for path in list(group.findall("svg:path", ns)):

            d = path.attrib.get("d", "").strip()

            # remove tiny paths
            if len(d) < 120:
                group.remove(path)
                removed += 1
                continue

            path.set("fill", "#000000")
            path.attrib.pop("stroke", None)

    tree.write(
        OUTPUT,
        encoding="utf-8",
        xml_declaration=True,
    )

    print("=" * 50)
    print("Optimization Complete")
    print("Removed :", removed, "small paths")
    print("Saved    :", OUTPUT)
    print("=" * 50)


if __name__ == "__main__":
    optimize()