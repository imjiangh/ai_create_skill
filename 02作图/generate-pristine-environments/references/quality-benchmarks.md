# Environment quality benchmarks

Use the bundled images only to judge physical and perceptual image quality. Never copy their subjects, people, buildings, creatures, layout, palette, or story unless the user explicitly assigns that reference role.

## Benchmark roles

### 01 — Low-key atmosphere

File: `assets/quality-benchmarks/benchmark-01-low-key-atmosphere.jpeg`

Tests a dark exterior with restrained atmospheric separation and one small warm focal light. Require readable subject silhouette, water response, depth falloff, and selective color contrast without globally raising black levels.

### 02 — Dark complex interior

File: `assets/quality-benchmarks/benchmark-02-dark-complex-interior.jpeg`

Tests extremely dark, information-dense space. Require architecture, circulation, crowd masses, debris, and focal pathways to remain distinguishable through organized local contrast and overhead light—not uniform brightness or global sharpening.

### 03 — Large-scale complexity

File: `assets/quality-benchmarks/benchmark-03-large-scale-complexity.jpeg`

Tests aerial scale, repeated urban structure, traffic and crowd density, smoke, and perspective. Require strong macro geometry and legible districts before microdetail. Dense information must remain grouped rather than dissolve into procedural noise.

### 04 — Material microdetail

File: `assets/quality-benchmarks/benchmark-04-material-microdetail.jpeg`

Tests close material rendering: stone thickness, joints, carving, fractures, dust, chipped edges, and directional wear. Require texture at plausible scale and localized damage while preserving broad solid planes and construction logic.

### 05 — Near-black silhouette

File: `assets/quality-benchmarks/benchmark-05-near-black-silhouette.jpeg`

Tests monochrome or near-black environments. Require a clear silhouette, selective rim or grazing light, separated foreground occlusion, readable ground or seabed, and atmospheric particles confined by light. Large black areas may remain black when they have a compositional purpose.

## Low-key readability gate

Judge dark images by these conditions:

1. Global exposure may remain low; do not demand a brighter remake merely because the histogram is dark.
2. Preserve four functional value bands when the scene supports them: limited deepest black, chromatic structural shadows, readable mid-dark surfaces, and sparse highlight anchors.
3. Reserve the clearest local contrast for the focal structure or path of attention.
4. Let detail decay with distance and atmosphere; do not blur all distant structure or sharpen all shadow texture.
5. Keep shadow noise, compression-like residue, halos, and repeated microtexture subordinate to real construction and material cues.
6. Reject raised gray blacks, milk-white fog, crushed focal geometry, and uniform HDR-like local contrast.

Do not require one output to satisfy every benchmark. Select the benchmark matching the scene's exposure, scale, density, and material distance.
