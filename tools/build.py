from pathlib import Path
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parent.parent
TOOLS = ROOT / "tools"

PIPELINE = [
    "preprocess.py",
    "trace.py",
    "optimize_svg.py",
    "animate_svg.py",
    "generate_terminal.py",
    "generate_readme.py",
]


def banner():
    print("=" * 70)
    print(" GitHub Profile Builder")
    print("=" * 70)
    print()


def run(script):

    path = TOOLS / script

    print(f"▶ Running {script}")

    start = time.perf_counter()

    result = subprocess.run(
        [sys.executable, str(path)],
        cwd=ROOT,
    )

    elapsed = time.perf_counter() - start

    if result.returncode != 0:

        print(f"\n❌ {script} failed.")
        sys.exit(result.returncode)

    print(f"✅ {script} completed ({elapsed:.2f}s)\n")


def summary():

    print("=" * 70)
    print("Build Finished Successfully")
    print("=" * 70)

    files = [
        ROOT / "README.md",
        ROOT / "assets" / "profile_processed.png",
        ROOT / "assets" / "profile_processed.pbm",
        ROOT / "assets" / "portrait.svg",
        ROOT / "assets" / "portrait_clean.svg",
        ROOT / "assets" / "portrait_animated.svg",
        ROOT / "assets" / "terminal.svg",
    ]

    print()

    for file in files:

        if file.exists():
            print(f"✔ {file.relative_to(ROOT)}")
        else:
            print(f"✘ {file.relative_to(ROOT)}")

    print()
    print("=" * 70)


def main():

    banner()

    total = time.perf_counter()

    for script in PIPELINE:
        run(script)

    summary()

    print(f"Total Time : {time.perf_counter() - total:.2f}s")


if __name__ == "__main__":
    main()