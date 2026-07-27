from pathlib import Path
import sys

import cv2
import numpy as np


ROOT = Path(__file__).resolve().parent.parent

INPUT = ROOT / "assets" / "profile.jpg"

OUTPUT_PNG = ROOT / "assets" / "profile_processed.png"
OUTPUT_PBM = ROOT / "assets" / "profile_processed.pbm"


class PortraitPreprocessor:

    def __init__(self, image_path: Path):

        self.image_path = image_path
        self.image = None
        self.gray = None
        self.binary = None

    def load(self):

        self.image = cv2.imread(str(self.image_path))

        if self.image is None:
            raise FileNotFoundError(
                f"Cannot open image:\n{self.image_path}"
            )

    def resize(self):

        h, w = self.image.shape[:2]

        target = 1200

        scale = target / max(h, w)

        if scale < 1:

            self.image = cv2.resize(
                self.image,
                None,
                fx=scale,
                fy=scale,
                interpolation=cv2.INTER_AREA,
            )

    def grayscale(self):

        self.gray = cv2.cvtColor(
            self.image,
            cv2.COLOR_BGR2GRAY,
        )

    def denoise(self):

        self.gray = cv2.bilateralFilter(
            self.gray,
            9,
            75,
            75,
        )

    def enhance(self):

        clahe = cv2.createCLAHE(
            clipLimit=2.5,
            tileGridSize=(8, 8),
        )

        self.gray = clahe.apply(self.gray)

    def threshold(self):

        self.binary = cv2.adaptiveThreshold(
            self.gray,
            255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY,
            41,
            8,
        )

    def invert(self):

        self.binary = cv2.bitwise_not(
            self.binary
        )

    def morphology(self):

        kernel = np.ones((3, 3), np.uint8)

        self.binary = cv2.morphologyEx(
            self.binary,
            cv2.MORPH_OPEN,
            kernel,
            iterations=1,
        )

        self.binary = cv2.morphologyEx(
            self.binary,
            cv2.MORPH_CLOSE,
            kernel,
            iterations=2,
        )

    def remove_small_components(self):

        num_labels, labels, stats, _ = cv2.connectedComponentsWithStats(
            self.binary,
            connectivity=8,
        )

        cleaned = np.zeros_like(self.binary)

        for i in range(1, num_labels):

            area = stats[i, cv2.CC_STAT_AREA]

            if area >= 120:

                cleaned[labels == i] = 255

        self.binary = cleaned

    def remove_border_components(self):

        num_labels, labels, stats, _ = cv2.connectedComponentsWithStats(
            self.binary,
            connectivity=8,
        )

        h, w = self.binary.shape

        cleaned = np.zeros_like(self.binary)

        for i in range(1, num_labels):

            x = stats[i, cv2.CC_STAT_LEFT]
            y = stats[i, cv2.CC_STAT_TOP]
            width = stats[i, cv2.CC_STAT_WIDTH]
            height = stats[i, cv2.CC_STAT_HEIGHT]

            touches = (
                x == 0 or
                y == 0 or
                x + width >= w or
                y + height >= h
            )

            if not touches:
                cleaned[labels == i] = 255

        self.binary = cleaned

    def final_cleanup(self):

        kernel = np.ones((2, 2), np.uint8)

        self.binary = cv2.dilate(
            self.binary,
            kernel,
            iterations=1,
        )

    def save(self):

        png = self.binary.copy()

        cv2.imwrite(
            str(OUTPUT_PNG),
            png,
        )

        cv2.imwrite(
            str(OUTPUT_PBM),
            png,
        )

    def process(self):

        self.load()
        self.resize()
        self.grayscale()
        self.denoise()
        self.enhance()
        self.threshold()
        self.invert()
        self.morphology()
        self.remove_small_components()
        self.remove_border_components()
        self.final_cleanup()
        self.save()


def main():

    if not INPUT.exists():

        print(f"Input image not found:\n{INPUT}")
        sys.exit(1)

    processor = PortraitPreprocessor(INPUT)

    processor.process()

    print("=" * 60)
    print("Preprocessing completed.")
    print(f"PNG : {OUTPUT_PNG}")
    print(f"PBM : {OUTPUT_PBM}")
    print("=" * 60)


if __name__ == "__main__":
    main()