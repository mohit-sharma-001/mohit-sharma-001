from pathlib import Path
import shutil
import subprocess
import sys


ROOT = Path(__file__).resolve().parent.parent

INPUT = ROOT / "assets" / "profile_processed.pbm"
OUTPUT = ROOT / "assets" / "portrait.svg"


POTRACE_CANDIDATES = [
    shutil.which("potrace"),
    r"D:\potrace-1.16.win64\potrace.exe",
]


def find_potrace():

    for exe in POTRACE_CANDIDATES:

        if exe and Path(exe).exists():
            return exe

    raise FileNotFoundError(
        "Potrace executable not found."
    )


def validate():

    if not INPUT.exists():
        raise FileNotFoundError(INPUT)


def build_command(potrace):

    return [

        potrace,

        str(INPUT),

        "-s",

        "-o",

        str(OUTPUT),

        "--invert",

        "--turdsize",
        "12",

        "--alphamax",
        "0.85",

        "--opttolerance",
        "0.25",

        "--unit",
        "8",
    ]
def run():

    validate()

    potrace = find_potrace()

    command = build_command(potrace)

    print()
    print("=" * 60)
    print("Running Potrace...")
    print("=" * 60)
    print(" ".join(command))
    print()

    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:

        print(result.stdout)
        print(result.stderr)

        raise RuntimeError(
            "Potrace failed."
        )

    if not OUTPUT.exists():

        raise RuntimeError(
            "portrait.svg was not created."
        )

    size = OUTPUT.stat().st_size

    if size == 0:

        raise RuntimeError(
            "Generated SVG is empty."
        )

    print()
    print("=" * 60)
    print("SVG generated successfully.")
    print(f"Output : {OUTPUT}")
    print(f"Size   : {size / 1024:.2f} KB")
    print("=" * 60)


def main():

    try:

        run()

    except Exception as e:

        print()
        print("=" * 60)
        print("ERROR")
        print("=" * 60)
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    main()