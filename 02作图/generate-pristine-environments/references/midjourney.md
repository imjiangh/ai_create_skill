# Midjourney workflow

## Prompt pattern

Use concise visual clauses and keep parameters at the end:

```text
[environment and function], [era/climate/world rules], [dominant mass and landmark], [foreground-midground-background plan], [camera height and lens behavior], [motivated light and weather], [construction and material response], [focal hierarchy and clean finish] --ar 16:9 --style raw --s [intentional value] --chaos [low for control]
```

## Control strategy

- Start with low chaos and moderate stylization when geometry and architecture matter.
- Use the aspect-ratio parameter to fit the deliverable; default environment assets to `--ar 16:9`. Use `--ar 21:9` only when coastline, skyline, terrain, architecture, or action has a genuinely horizontal span and the landmark remains large enough to inspect.
- Use Raw mode when automatic styling overwhelms structure or material truth.
- Use image prompts for broad visual influence and Style Reference for aesthetic language. Do not treat style references as geometry locks.
- Keep negative parameters sparse and noun-like; do not append long prose exclusions.
- Do not add version flags from memory. Verify current syntax when a version-specific feature matters.

## Iteration

1. Select the candidate with the best macro space, scale, and light—not the busiest texture.
2. Vary or edit only the failed region when possible.
3. For generic results, improve function, construction, landmark, camera, and environmental cause instead of adding quality adjectives.
4. For melted architecture, reduce style pressure, simplify repeated structures, and strengthen layout/reference control.
5. For muddy depth, clarify foreground-midground-background separation and atmospheric falloff.
6. For material confusion, name roughness, edge, construction, and weathering differences.

Official basis: Midjourney Prompt, Parameter List, Aspect Ratio, and Style Reference documentation, accessed July 2026.
