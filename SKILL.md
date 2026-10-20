---
name: handdrawn-icon-generator
description: Generate new raster icons that match Xue Xia's colorful hand-drawn icon set. Use when asked to create, redraw, extend, or make variants of small icons in the style of the bundled 100×100 PNG references, especially for simple objects, food, animals, activities, symbols, or miniature scenes with transparent backgrounds.
---

# Hand-drawn Icon Generator

Create one icon at a time with the image generation tool, using the bundled drawings as visual references.

## Workflow

1. Read [references/style-guide.md](references/style-guide.md).
2. Inspect `assets/reference-icons/manifest.md` and select 3–5 references. Always include `style_outline_pressure.png` for the approved outline treatment. Include `style_airbrush_shadow.png` only when the user requests depth or shading. Add 1–3 subject-adjacent examples; do not use all references at once.
3. Ask for clarification only when the requested subject, output count, or essential visual meaning is genuinely ambiguous. Otherwise generate directly.
4. Call the image generation tool with the selected local reference paths. State that the references define the visual language, not content to copy.
5. Request a single centered icon, no frame, no text, no watermark, square canvas, and ample breathing room. For built-in image generation, use a perfectly uniform removable chroma-key background that does not occur in the subject; remove it locally after generation.
6. Inspect the result. Regenerate if it has a photographic look, complex texture, excessive detail, generic vector polish, hard geometry, unwanted text, or weak small-size readability.
7. Remove the chroma-key background and save the final as RGBA PNG. Make only the area outside the icon transparent; keep the icon body and intended interior regions opaque. Do not deliver the chroma-key source.
8. Validate transparency before delivery: confirm PNG/RGBA format, alpha value 0 at all four corners, no opaque background rectangle, no green/white fringe, and a nonempty opaque subject. Preserve intentional transparent holes only when the subject requires them.
9. Resize a copy to exactly 100×100 using high-quality Lanczos resampling while preserving alpha. Keep the larger transparent PNG when useful.

## Prompt Pattern

Use this structure, adapting the subject-specific details:

> Draw one [subject] icon in the same personal hand-drawn visual language as the supplied reference icons. Apply wax-crayon character only to the outlines: vary line width organically with hand pressure, use occasional non-repeating skips and localized retracing, and avoid any fixed-width or procedural texture. Keep interior color regions solid, opaque, and clean. Preserve simplified rounded forms, cheerful saturated palette, sparse detail, and friendly handmade character. Show [essential identifying details]. Use a centered, compact silhouette with generous transparent padding. No text, lettering, border, frame, drop shadow, photorealism, 3D rendering, glossy vector finish, or background scene. Transparent PNG. It must read clearly at 100×100 pixels. Treat the references as style guidance only; create an original drawing.

## Output Rules

- Generate one icon per file unless the user explicitly requests a set.
- Deliver PNG only. The icon exterior must be transparent like the bundled references; the icon itself must remain opaque. Never deliver a white background, chroma-key background, JPEG, or flattened RGB image.
- Keep subjects recognizable with roughly 1–4 main color regions and only a few interior marks.
- Match the reference set's handmade inconsistencies; avoid sterile symmetry and pixel-perfect vector edges.
- Apply dry wax-crayon texture only to outlines. Keep interior fills completely solid, opaque, flat, and texture-free.
- Make outline width vary visibly with natural hand pressure: thinner during quick passages, heavier at turns and pauses, with asymmetric non-repeating variation. Reject constant-width strokes and uniformly distributed texture.
- Keep shading off by default. When the user requests more depth, add one restrained deep-color airbrush shadow inside the subject on the viewer-right side: darkest near the inner edge, softly diffusing toward the center over roughly the rightmost 25–30%. Preserve the crayon outline and do not add a cast shadow.
- Use text only when it is semantically indispensable and explicitly requested. Prefer symbols over words.
- For a multi-icon set, reuse one prompt scaffold, canvas treatment, scale, and palette logic across every icon, then visually compare the set before delivery.
- Name files with lowercase ASCII words and underscores, for example `rain_boots.png`.

## Resources

- Read `references/style-guide.md` for visual constraints and quality checks.
- Use `assets/reference-icons/*.png` as image-generation references.
- Use `assets/reference-icons/manifest.md` to choose references by subject family.
- Use `assets/reference-icons/style_outline_pressure.png` as the primary approved outline reference.
- Use `assets/reference-icons/style_airbrush_shadow.png` as the approved optional depth/shading reference.
