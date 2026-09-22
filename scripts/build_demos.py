"""Build the six web demos from privacy-reviewed MAVP footage.

Pass --media-root when the original ICRA media is stored outside the sibling
directory. Five inputs are the v19 privacy-masked masters. The conveyor clip
starts at 3 seconds, after the operator has left the frame. The dual-drawer
master was reviewed separately and contains no visible person.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
from pathlib import Path


DEMOS = [
    ("01-drawer-packing", "v19_fix/assets/drawer_safe.mp4", 0.0, 30.96, 0),
    ("02-disassemble-and-deliver", "v19_fix/assets/disassemble_safe.mp4", 0.0, 26.68, 29),
    ("03-lidded-box-packing", "v19_fix/assets/box_safe.mp4", 0.0, 28.80, 56),
    ("04-conveyor-picking", "v19_fix/assets/conveyor_safe.mp4", 3.0, 21.80, 82),
    ("05-dual-drawer-return", "v18_opencut/assets/dual_base.mp4", 0.0, 33.00, 104),
    ("06-bag-packing", "v19_fix/assets/bag_safe.mp4", 0.0, 29.72, 132),
]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--media-root",
        type=Path,
        default=Path(__file__).resolve().parents[2],
        help="ICRA directory containing output/icra2027_multimedia",
    )
    args = parser.parse_args()
    media = args.media_root / "output" / "icra2027_multimedia"
    soundtrack = media / "MAVP_original_soundtrack.wav"
    out_dir = Path(__file__).resolve().parents[1] / "assets" / "videos"
    out_dir.mkdir(parents=True, exist_ok=True)
    try:
        import imageio_ffmpeg

        ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
    except ImportError:
        ffmpeg = shutil.which("ffmpeg")
        if not ffmpeg:
            raise RuntimeError("ffmpeg or imageio_ffmpeg is required")

    for name, source, trim_start, duration, music_start in DEMOS:
        input_video = media / source
        output_video = out_dir / f"{name}.mp4"
        for file in (input_video, soundtrack):
            if not file.is_file():
                raise FileNotFoundError(file)
        fade_out = duration - 0.35
        music_fade_out = duration - 1.3
        filters = (
            "[0:v]scale=1280:720:flags=lanczos,fps=25,"
            f"fade=t=in:st=0:d=0.35,fade=t=out:st={fade_out:.2f}:d=0.35,"
            "format=yuv420p[v];"
            f"[1:a]atrim=0:{duration:.2f},asetpts=PTS-STARTPTS,"
            "loudnorm=I=-20:LRA=7:TP=-2,"
            f"afade=t=in:st=0:d=0.7,afade=t=out:st={music_fade_out:.2f}:d=1.3[a]"
        )
        command = [ffmpeg, "-hide_banner", "-nostdin", "-y", "-loglevel", "error"]
        if trim_start:
            command += ["-ss", str(trim_start)]
        command += ["-i", str(input_video), "-ss", str(music_start), "-stream_loop", "-1", "-i", str(soundtrack)]
        command += [
            "-filter_complex", filters, "-map", "[v]", "-map", "[a]",
            "-t", f"{duration:.2f}", "-c:v", "libx264", "-preset", "veryfast",
            "-crf", "25", "-maxrate", "2800k", "-bufsize", "5600k",
            "-c:a", "aac", "-b:a", "112k", "-ar", "48000",
            "-movflags", "+faststart", "-map_metadata", "-1", str(output_video),
        ]
        print(f"Building {name}", flush=True)
        subprocess.run(command, check=True)
        print(f"  {output_video.stat().st_size / 1_000_000:.1f} MB", flush=True)


if __name__ == "__main__":
    main()
