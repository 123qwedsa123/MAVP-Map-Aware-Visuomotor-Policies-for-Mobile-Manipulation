"""Prepare web images from the standalone figures in the Overleaf source.

This script reads figure1_tasks.png and mavp_overview_release.pdf directly.
It never crops or screenshots a page of the paper.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import subprocess
from tempfile import TemporaryDirectory

from PIL import Image, ImageOps


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("paper_source", type=Path, help="Local Overleaf project directory")
    args = parser.parse_args()

    output = Path(__file__).resolve().parents[1] / "assets" / "images"
    output.mkdir(parents=True, exist_ok=True)

    task_figure = args.paper_source / "figures" / "figure1_tasks.png"
    with Image.open(task_figure) as original:
        image = ImageOps.exif_transpose(original).convert("RGB")
        image.thumbnail((2160, 2160), Image.Resampling.LANCZOS)
        image.save(output / "task-overview.webp", "WEBP", quality=88, method=6)
        print("task-overview.webp", image.size)

    method_figure = args.paper_source / "figures" / "mavp_overview_release.pdf"
    with TemporaryDirectory() as directory:
        render_prefix = Path(directory) / "method"
        subprocess.run(
            ["pdftoppm", "-f", "1", "-l", "1", "-singlefile", "-scale-to-x", "1988", "-scale-to-y", "-1", "-png", str(method_figure), str(render_prefix)],
            check=True,
        )
        with Image.open(render_prefix.with_suffix(".png")) as rendered:
            image = rendered.convert("RGB")
            image.save(output / "method-overview.webp", "WEBP", quality=90, method=6)
            print("method-overview.webp", image.size)


if __name__ == "__main__":
    main()
