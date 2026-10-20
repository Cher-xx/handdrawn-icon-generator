# Hand-drawn Icon Generator

A Codex skill for extending a colorful, hand-drawn PNG icon set. It uses the included reference icons to generate new 100×100 transparent-background icons with flat fills, irregular wax-crayon outlines, and optional template-aware placement.

## Use in Codex

1. Download or clone this repository.
2. Copy the `handdrawn-icon-generator` folder into your Codex skills directory:

   ```text
   ~/.codex/skills/handdrawn-icon-generator
   ```

3. Start a new Codex task and ask, for example:

   ```text
   使用 $handdrawn-icon-generator 生成一个透明背景的雪人 icon。
   ```

Codex will use `SKILL.md`, the style guide, and the bundled reference icons. If a project supplies `template.png`, the icon is placed around its reserved number area while preserving a transparent PNG output.

## Contents

- `SKILL.md` — generation workflow and visual constraints
- `assets/reference-icons/` — hand-drawn style references
- `references/style-guide.md` — compact style and quality guide
- `agents/openai.yaml` — Codex skill metadata

## License

Released under the [MIT License](LICENSE). You may use, modify, and redistribute the skill and its bundled reference assets under its terms.
