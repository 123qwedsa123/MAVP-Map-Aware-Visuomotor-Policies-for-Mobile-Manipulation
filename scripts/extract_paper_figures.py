"""Export unchanged crops from the compiled MAVP paper for the project page."""

from __future__ import annotations

import argparse
from pathlib import Path

import fitz
from PIL import Image


# Coordinates are PDF points in the nine-page paper compiled on 2026-09-22.
CROPS = [
    (0, "six-tasks", (52, 192, 557, 462)),
    (1, "method-overview", (55, 29, 558, 232)),
    (4, "control-variants", (34, 190, 301, 305)),
    (6, "feedback-ablation", (52, 34, 307, 205)),
    (6, "policy-families", (311, 156, 558, 280)),
]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("paper", type=Path)
    args = parser.parse_args()
    output = Path(__file__).resolve().parents[1] / "assets" / "images"
    output.mkdir(parents=True, exist_ok=True)
    document = fitz.open(args.paper)
    for page_number, name, coordinates in CROPS:
        pixmap = document[page_number].get_pixmap(
            matrix=fitz.Matrix(3.2, 3.2), clip=fitz.Rect(*coordinates), alpha=False
        )
        image = Image.frombytes("RGB", (pixmap.width, pixmap.height), pixmap.samples)
        path = output / f"{name}.webp"
        image.save(path, "WEBP", quality=92, method=6)
        print(f"{path.name}: {image.width}x{image.height}")


if __name__ == "__main__":
    main()
