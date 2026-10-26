#!/usr/bin/env python3
"""Reject an icon that overlaps the opaque alpha mask of a template."""

from __future__ import annotations

import sys
from pathlib import Path

from PIL import Image


def main() -> int:
    if len(sys.argv) != 3:
        print("usage: validate_template_placement.py <icon.png> <template.png>", file=sys.stderr)
        return 2

    icon_path, template_path = map(Path, sys.argv[1:])
    with Image.open(icon_path) as icon_source, Image.open(template_path) as template_source:
        icon = icon_source.convert("RGBA")
        template = template_source.convert("RGBA")

    if icon.size != template.size:
        print(
            f"error=canvas_size_mismatch icon={icon.size[0]}x{icon.size[1]} "
            f"template={template.size[0]}x{template.size[1]}",
            file=sys.stderr,
        )
        return 1

    icon_alpha = icon.getchannel("A")
    template_alpha = template.getchannel("A")
    overlap = sum(
        icon_value > 0 and template_value > 0
        for icon_value, template_value in zip(icon_alpha.tobytes(), template_alpha.tobytes())
    )
    print(f"overlap_pixels={overlap}")
    return 0 if overlap == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
