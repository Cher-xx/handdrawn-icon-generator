#!/usr/bin/env python3
"""Render a human-readable placement proof; never use it as the production PNG."""

from __future__ import annotations

import sys
from pathlib import Path

from PIL import Image, ImageDraw


def main() -> int:
    if len(sys.argv) != 4:
        print("usage: render_template_check.py <icon.png> <template.png> <check.png>", file=sys.stderr)
        return 2
    icon_path, template_path, output_path = map(Path, sys.argv[1:])
    with Image.open(icon_path) as source, Image.open(template_path) as source_template:
        icon = source.convert("RGBA")
        template = source_template.convert("RGBA")
    if icon.size != template.size:
        print("error=canvas_size_mismatch", file=sys.stderr)
        return 1

    proof = Image.new("RGBA", icon.size, "white")
    proof.alpha_composite(template)
    draw = ImageDraw.Draw(proof)
    mask_box = template.getchannel("A").getbbox()
    if mask_box:
        draw.text((mask_box[0] + 2, mask_box[1] + 2), "100×100", fill="white")
    proof.alpha_composite(icon)
    proof.convert("RGB").save(output_path, "PNG")
    print(f"placement_check={output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
