# Style Guide

## Visual Signature

- Format: square RGBA PNG, designed to remain clear at 100×100 pixels.
- Background: fully transparent outside the icon, matching the bundled references. Keep the icon body opaque. Never deliver a white/colored background rectangle or the intermediate chroma-key image.
- Composition: one centered subject or a tiny, extremely simplified scene; generous empty space; no container shape.
- Drawing: informal wax-crayon feel with visibly granular, mildly uneven edges, rounded corners, and organic asymmetry.
- Detail: minimal. Use the fewest marks needed to identify the subject; omit realistic texture and lighting.
- Color: bright, warm, cheerful fills. Recurring families include sunny yellow, orange, coral/pink, sky blue, purple, warm brown, muted teal, cream, and occasional green.
- Outline: favor dry wax-crayon strokes in dark warm brown or a subject color. Vary width organically along each stroke according to imagined hand pressure: use thinner fast passages, heavier turns and pauses, occasional tiny pigment gaps, and localized imperfect retracing. Make neighboring lines and mirrored sides differ. Avoid fixed-width paths, smooth vector strokes, or evenly distributed procedural speckles.
- Fill: keep interior color regions solid, opaque, and clean. Do not apply crayon grain, paper tooth, scribbles, speckles, or pinholes to fills.
- Shading: use none by default. When the user explicitly requests depth, add a restrained deep-color airbrush shadow inside the subject on the viewer-right side. Keep it darkest against the right inner edge and diffuse it softly toward the center across about 25–30% of the form. Do not cover or smooth the outline, shade unrelated parts, add a cast/contact shadow, or introduce airbrush texture elsewhere.
- Mood: playful, approachable, casual, cute without becoming highly detailed kawaii art.

## Shape and Scale

- Let the main subject occupy about 60–80% of the canvas in its dominant dimension.
- Preserve clear padding around all sides; do not crop the drawing.
- Prefer a strong outer silhouette over interior detail.
- Keep thin marks thick enough to survive reduction to 100×100.
- Allow small imperfections such as slightly wobbly contours and imperfect bilateral symmetry.

## Palette Anchors

Treat these as approximate families, not mandatory exact swatches:

- Yellow: `#FFD000` to `#FFC020`
- Orange/coral: `#FF9130` to `#FF6030`
- Pink: `#FF5080`
- Sky blue: `#60A0E0`
- Purple: `#8730D0`
- Warm brown: `#603010` to `#605050`
- Muted teal: `#609080`
- Cream: `#F0E0D0`

Use a limited subset for each icon. Maintain contrast without outlining every region.

## Failure Checks

Reject or revise the output when any answer is yes:

- Does it look like stock vector clip art rather than a personal doodle?
- Are edges too geometric, perfectly mirrored, or mechanically uniform?
- Are the outlines too smooth, continuous, and digitally clean to read as wax crayon?
- Is line width too consistent, or is the roughness evenly distributed like a software filter?
- Do any interior fills contain unwanted crayon grain, scribbles, speckles, or pinholes?
- If shading was requested, is it confined to the right interior edge with a soft inward fade and no cast shadow?
- Is the subject hard to identify at thumbnail size?
- Are there too many tiny details, textures, reflections, or gradients?
- Is the subject cropped or pressed against the canvas edge?
- Is there a white/colored rectangle instead of transparency?
- Are all four corner alpha values 0, with no green/white fringe around the icon?
- Is the file a true RGBA PNG rather than JPEG, RGB PNG, or a flattened preview?
- Did the model copy a reference subject instead of drawing the requested one?
- Did it introduce text, a logo, a border, a watermark, or a complex scene?

## Choosing References

Choose 3–5 files from the manifest:

1. Always include `style_outline_pressure.png` for the approved non-uniform crayon outline.
2. Include `style_airbrush_shadow.png` only when shading or depth is requested.
3. Pick 1–3 semantically adjacent subjects to guide structure, reduction, and padding.
4. Keep reference selection varied enough to communicate the visual language without encouraging copied content.
