---
name: handdrawn-icon-generator
description: Generate new raster icons that match Xue Xia's colorful hand-drawn icon set. Use when asked to create, redraw, extend, or make variants of small icons in the style of the bundled 100×100 PNG references, especially for simple objects, food, animals, activities, symbols, or miniature scenes with transparent backgrounds and numbered-template placement.
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
7. Remove the chroma-key background and save the final as an actual RGBA PNG file. Make only the area outside the icon transparent; keep the icon body and intended interior regions opaque. Do not deliver the chroma-key source, a flattened preview, or a screenshot.
8. Validate the delivered file itself, not the chat preview: confirm PNG/RGBA format, alpha value 0 at all four corners, no opaque background rectangle, no green/white fringe, and a nonempty opaque subject. Never rasterize a white background or a gray checkerboard transparency preview into the final image. Preserve intentional transparent holes only when the subject requires them.
9. Resize a copy to exactly 100×100 using high-quality Lanczos resampling while preserving alpha. Keep the larger transparent PNG when useful.
10. Use `assets/template.png` as the default numbered-template layout. When a workspace `template.png` is supplied, use that current file instead of the bundled default. Follow the template-composition workflow below before delivery.

## Template Composition

Use this workflow for every icon unless the user explicitly asks not to use a template.

1. Read the active template file on every run: prefer the workspace `template.png` when supplied; otherwise use `assets/template.png`. This image is the **only** authority for placement. Do not derive, state, or use numerical coordinates or a rectangular substitute.
2. Define `reserved_mask` as every pixel whose template alpha is greater than zero. Treat only that exact pixel shape as reserved; its bounding box, surrounding transparent pixels, and any imagined rectangle are not reserved.
3. If the host cannot access the active template image, state that it cannot perform template placement. Do not invent a coordinate substitute, approximate layout, or centered fallback.
4. Keep `reserved_mask` transparent in the final production PNG. Use the template only as an invisible placement mask: never copy its black guide, checkerboard, digits, or background into the output.
5. Place the complete icon at the upper-right by default. Scale and position the whole icon to the largest practical no-collision placement; never crop, erase, split, or mechanically over-shrink the subject or related marks such as raindrops.
6. Compute collision at final output resolution using both alpha channels: an overlap is any pixel where `icon_alpha > 0` and `template_alpha > 0`. Do not test rectangular bounding boxes. Transparent portions of the icon's bounding box may occupy transparent portions of the template's bounding box.
7. Before delivery, make the icon canvas exactly the active template's dimensions and run `scripts/validate_template_placement.py <icon.png> <template.png>`. Deliver only when it reports `overlap_pixels=0`.
8. If the user asks to inspect number legibility, make a separate preview by placing a dark, readable sample numeral over the reserved region. Keep the delivered production PNG free of the numeral unless requested.

## Prompt Pattern

Use this structure, adapting the subject-specific details:

> Draw one [subject] icon in the same personal hand-drawn visual language as the supplied reference icons. Apply wax-crayon character only to the outlines: vary line width organically with hand pressure, use occasional non-repeating skips and localized retracing, and avoid any fixed-width or procedural texture. Keep interior color regions solid, opaque, and clean. Preserve simplified rounded forms, cheerful saturated palette, sparse detail, and friendly handmade character. Show [essential identifying details]. Use a centered, compact silhouette with generous transparent padding. No text, lettering, border, frame, drop shadow, photorealism, 3D rendering, glossy vector finish, or background scene. Transparent PNG. It must read clearly at 100×100 pixels. Treat the references as style guidance only; create an original drawing.

## Output Rules

- Generate one icon per file unless the user explicitly requests a set.
- Deliver PNG only. The icon exterior must be transparent like the bundled references; the icon itself must remain opaque. Never deliver a white background, chroma-key background, JPEG, or flattened RGB image.
- If the host cannot provide a verifiable transparent RGBA PNG download, state that limitation instead of substituting a non-transparent image.
- If the host cannot read the template image or cannot run the required collision validation, state that template placement is unavailable; never silently revert to a centered icon.
- Keep subjects recognizable with roughly 1–4 main color regions and only a few interior marks.
- Add a few restrained, widely recognized semantic details when they are integral to the subject's conventional reading (for example, a Christmas tree may have a star, light snow, and a few ornaments). Do not add arbitrary narrative elements; honor an explicit request for a plain or undecorated subject.
- Choose conventional subject colors at moderate or low saturation unless the user specifies otherwise; avoid novelty palettes that contradict common visual meaning.
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
- Use `assets/template.png` as the bundled default numbered-template layout; a user-supplied workspace `template.png` overrides it.
