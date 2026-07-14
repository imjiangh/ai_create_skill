# GPT Image workflow

## Prompt pattern

Write natural production instructions:

```text
Create one [medium] environment image in [aspect ratio/orientation].
Place/function: [scene identity, era, climate, use].
Macro layout: [horizon, terrain/floor, dominant mass, circulation, landmark].
Depth: [foreground anchor, midground subject, background closure and overlap].
Camera: [height, angle, lens behavior, distance, crop].
Lighting/weather: [source, direction, elevation, softness, exposure, atmosphere].
Materials/construction: [major materials, assembly, roughness, scale, localized wear].
Finish: [focal hierarchy, clean gradients, quiet zones, restrained sharpening].
Exclude: [likely structural and material failures only].
```

## Reference roles

Declare each image separately:

```text
Use image 1 only for macro layout and camera.
Use image 2 only for architectural language and construction details.
Use image 3 only for lighting, weather, and palette.
Do not inherit image 1's materials or image 3's geometry.
```

## Editing

Use local editing for bounded defects and regeneration for global geometry failure:

```text
Preserve exactly: horizon, camera, composition, building layout, light direction, palette, and all unaffected materials.
Change only: [observable defect and desired correction].
Make the correction coherent with existing perspective, construction, scale, weather, and light.
```

## Output controls

- For API use, select explicit size and quality when the deliverable requires them; do not rely on words such as `4K` inside the prompt.
- Prefer 16:9 landscape output for general environment assets. Use 21:9 only for genuinely horizontal scene structure or motion; do not use it as a generic cinematic preset. Use portrait output for height-led scenes.
- Use high-fidelity reference/edit workflows when structural preservation matters.
- Generate one image by default; do not request multiple variants unless exploration is the goal.

## Practical behavior

- GPT Image responds well to explicit relational language and preservation/change boundaries.
- Break complex environments into macro layout, construction, light, and material clauses.
- Use references for different roles rather than asking one reference to control everything.
- Avoid too many simultaneous micro-constraints; fix global spatial errors before surface polish.
- Precise text, recurring brand elements, and repeated complex geometry may still require inspection and targeted editing.
- Add cleanup language only for an observed or likely symptom. Preserve construction edges and meaningful material texture; do not request globally low sharpness or low contrast as a generic denoise strategy.

Official basis: OpenAI Image Generation guide and OpenAI Cookbook image-generation prompting/evaluation examples, accessed July 2026.
