---
name: generate-pristine-environments
description: Generate, prompt, art-direct, critique, and repair high-fidelity environment images with coherent spatial structure, believable architecture, motivated lighting, readable materials, controlled atmosphere, and clean native-looking finish. Use for landscapes, architecture, interiors, exterior establishing shots, ancient or fantasy environments, science-fiction spaces, urban scenes, environment concept art, GPT Image or Midjourney prompt conversion, reference reconstruction, and targeted scene regeneration. Do not use for person-only portraits, character asset sheets, video prompts, maps, diagrams, or narrative breakdowns.
---

# Generate Pristine Environments

Create professional environment imagery by solving space before decoration: purpose, scale, layout, camera, light, materials, atmosphere, then finish. Treat fidelity as structural credibility and controlled information—not keyword density.

## Pipeline handoff

When invoked by `visual-asset-pipeline`, act only on the assigned `E###` asset IDs. Treat `P01`, `S01`, `A01`, approved references, spatial geometry, era, material system, entrance/exit, scale, main-light direction, and aspect ratio as authoritative inputs. Return asset paths, prompt version, inspection result, and unresolved spatial risks to A03. Do not rename assets, change story facts, or declare the S2 stage locked.

## Core standard

Require all relevant qualities:

- legible foreground, midground, background, focal destination, and path of attention;
- coherent horizon, vanishing behavior, scale cues, gravity, access, support, and construction;
- one motivated lighting system with consistent direction, shadow, bounce, and exposure;
- materials distinguished by roughness, reflectivity, edge wear, scale, and environmental response;
- atmosphere that creates depth without veiling the focal structure;
- detail concentrated in one primary zone and at most one secondary zone;
- clean gradients, readable darks, intact silhouettes, restrained sharpening, and no AI residue.

Never equate quality with `8K`, `masterpiece`, maximum sharpness, excessive fog, bloom, particles, or adjective chains.

Default environment assets to one 16:9 landscape frame because it preserves usable subject scale, vertical depth, inspectable materials, and broad delivery compatibility. Use 21:9 only when the scene's primary spatial structure or visual movement genuinely extends horizontally, such as a long coastline, mountain range, city skyline, procession, defensive wall, or cinematic establishing shot. Do not choose 21:9 merely to signal “cinematic”; reject it when it would only add empty side space, shrink the landmark, flatten vertical depth, or reduce inspectable detail. Use 9:16 for vertical mobile scenes or strong height-driven compositions, 1:1 for square studies, and another ratio only when the deliverable requires it. People may appear only as scale cues unless the user asks for a combined person-and-environment image.

## Route the request

1. Identify the operation: create, reference-based create, prompt extraction, critique, repair, or GPT/Midjourney conversion.
2. Identify purpose: reusable environment asset, establishing shot, concept exploration, architectural visualization, game environment, editorial backdrop, or narrative still.
3. Identify medium: photographic realism, architectural visualization, production concept art, matte painting, painterly illustration, 3D render, or hybrid.
4. Identify scene family: natural, rural, urban, interior, architectural exterior, historical, fantasy, science fiction, industrial, or surreal.
5. Ask only for missing information that materially changes geometry, era, function, weather, camera, or medium. Otherwise make compact assumptions and proceed.
6. Read [references/environment-craft.md](references/environment-craft.md) for spatial, architectural, material, and atmosphere rules.
7. Read [references/gpt-image.md](references/gpt-image.md) for GPT Image generation or editing.
8. Read [references/midjourney.md](references/midjourney.md) for Midjourney prompts and parameters.
9. For critique or any repair pass, read [references/review-rubric.md](references/review-rubric.md).
10. For every environment generation, critique, or repair, read [references/quality-benchmarks.md](references/quality-benchmarks.md) and compare against the relevant bundled benchmark images. Treat them only as image-quality references, never as required subject matter, architecture, composition, palette, or style.

## Build the scene brief

Resolve these layers in order:

1. **Function and world rules:** what the place is for, who built or shaped it, era, climate, maintenance, and physical constraints.
2. **Macro layout:** horizon, terrain or floor plane, dominant mass, circulation, entrances, voids, and landmark.
3. **Depth plan:** named foreground anchor, midground subject, background closure, overlap, size falloff, and atmospheric falloff.
4. **Camera:** viewpoint height, angle, lens behavior, distance, crop, and whether verticals converge.
5. **Lighting:** source, time, direction, elevation, softness, exposure range, bounce color, and shadow continuity.
6. **Materials:** substrate, construction, scale, roughness, moisture, age, contact, and localized wear.
7. **Life and weathering:** drainage, dirt paths, vegetation logic, accumulated debris, repairs, water flow, or occupancy traces.
8. **Finish:** focal sharpness, quiet zones, color separation, clean edges, and exclusions.

Answer four geometry questions before prompting: Where is the horizon? What is the dominant vanishing behavior? What is the largest readable mass? How does a viewer or occupant move through the space?

Answer four light questions: What emits or reflects the dominant light? From what direction and height? Which planes are lit or shadowed? What atmospheric condition modifies visibility?

For low-key scenes, separate darkness from obscurity. Permit a genuinely dark global exposure without lifting all shadows. Build readable darks from a small deepest-black anchor, chromatic shadow masses, continuous tonal gradients, and selective local contrast on structure-bearing edges. Preserve the information that explains form, scale, construction, material, and depth; suppress meaningless high-frequency noise. Never solve a dark scene by globally flattening contrast, raising black levels into gray, whitening atmosphere, or sharpening every shadow texture.

Use scale evidence rather than saying “epic”: doors, stairs, trees, furniture, railings, vehicles, windows, people, masonry modules, or known landforms. Do not add all of them; select the ones natural to the scene.

## Write the prompt

Use positive, observable instructions in this order:

`deliverable + place/function + world rules + macro layout + depth plan + camera + lighting/weather + materials/construction + controlled detail + finish + exclusions`

Preserve priority tiers:

- **Immutable:** scene type, era, required structures, geography, view, subject count, aspect ratio.
- **Directed:** layout, camera, light, weather, palette, material response, focal hierarchy.
- **Flexible:** minor props, distant silhouettes, incidental vegetation, and nonessential accents.

State spatial relationships explicitly: left/right, foreground/midground/background, inside/outside, above/below, behind/in front, distance, orientation, and relative scale. Replace vague style labels with visible design evidence.

When the user asks for a prompt, return one clean model-ready prompt, reference roles if applicable, useful model parameters, and a short exclusion block only when it adds control. Do not pad with theory unless requested.

## Generate

Use the available image tool when the user asks for an image. Include all required references. Generate without reconfirmation unless a necessary reference is missing.

For candidate 1, lock macro geometry, focal hierarchy, camera, and light before microscopic texture. Do not ask one frame to be simultaneously a vast establishing shot and a close material inspection. If both are needed, propose separate wide and detail views.

Do not append a universal “denoise” or “clean image” paragraph to every prompt. Use symptom-specific cleanup only when the requested style or an inspected result shows a concrete problem:

- **dirty digital noise:** smooth broken tonal transitions and suppress meaningless high-frequency grain while preserving structural edges;
- **crunchy sharpening or HDR:** soften halos and brittle local contrast without flattening the focal hierarchy;
- **global grime:** confine wear, oxidation, moisture, and dirt to physically motivated locations;
- **surface overload:** remove uniform microtexture and ornament outside the named primary and secondary detail zones.

Never translate cleanup into globally low contrast, low sharpness, flat color, erased shadow information, or plastic smoothing.

Treat each reference as one or more declared roles: layout, architecture, material, light, palette, weather, vegetation, or style. Never silently let a style reference override required geometry.

## Inspect and conditionally repair

Inspect actual pixels at full-frame and local-detail scale. Default to one generation. Generate candidate 2 only for a hard failure:

- collapsed perspective, contradictory horizon, impossible scale, floating structures, broken access, or unusable architecture;
- missing or incorrect required landmark, era, geography, view, aspect ratio, or core scene type;
- conflicting light directions, severe exposure clipping, unreadable focal subject, or major focus failure;
- melted geometry, repeated structural artifacts, implausible materials, severe texture tiling, or obvious AI residue;
- atmosphere, clutter, or stylization so strong that the scene is unusable for its stated purpose.

For a dark scene, do not classify low average brightness itself as a failure. Reject it only when the focal subject, depth planes, construction, or important material boundaries collapse into indistinguishable black; or when lifted gray shadows, noise, halos, and uniform sharpening replace real tonal structure.

Do not regenerate for mild softness, slightly imperfect distant detail, small prop errors, a color preference, or optional polish.

If a hard failure exists:

1. Rank failures by impact.
2. Select only the top one or two root causes.
3. Preserve all correct geometry, composition, lighting, and design.
4. Perform exactly one targeted edit or regeneration.
5. Compare both candidates against the same criteria; deliver the stronger one.
6. Stop automatic iteration. If the defect persists, state the remaining gap and recommend a changed camera, crop, reference role, simplified geometry, or separate pass.

Repair the smallest causal layer. Do not redesign an entire scene to fix a local material or prop failure. Never use a blind retry.

## Deliver

For generation, return only the generated image as required by the image tool. For prompt or critique work, lead with the usable result and keep production notes concise.

Do not introduce characters, story events, text, logos, borders, panels, film grain, fog, glow, particles, lens flare, or cinematic grading unless requested or physically justified.
