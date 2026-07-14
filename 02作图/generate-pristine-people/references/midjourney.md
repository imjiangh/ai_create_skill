# Midjourney workflow

## Prompt behavior

- Put subject, composition, medium, lighting, and material evidence in the prompt; keep parameters separate at the end.
- Prefer concise visual clauses. Repetition and adjective stacking reduce control.
- Use image prompts for broad visual influence, Style Reference for aesthetic language, and the current identity/object reference mechanism supported by the selected model version.
- Confirm current parameter syntax from official Midjourney documentation when version-sensitive behavior matters.

## Base prompt pattern

```text
[one-person deliverable], [identity and facial geometry], [hair and body build], [wardrobe construction and materials], [pose and expression], vertical full-body casting image, actor fills the frame, [background], one shaped off-axis key light, controlled fill, negative fill on far cheek, small soft-edged skin highlights, natural local skin color variation, anatomically scaled pores and sparse vellus hair, credible hair and fabric response, clean tonal transitions, restrained sharpening --ar 9:16 --style raw --s [intentional value]
```

## Control strategy

- Start with moderate stylization when identity, garment accuracy, or anatomy matters.
- Default single-person assets to `--ar 9:16`; use another ratio only by request.
- Use Raw mode to reduce automatic aesthetic styling when photographic control matters.
- Increase stylization only after structure is stable.
- Do not rely on seed as an identity lock.
- Separate style and identity references; do not ask one image to control every dimension.
- Use lower chaos for a controlled production image and higher chaos only for exploration.
- Use negative parameters sparingly for nouns or motifs, not long prose lists.

## Iteration

1. Select the candidate with the best structure, not the most surface detail.
2. Vary region or reprompt only the faulty layer when possible.
3. If identity drifts, reduce conflicting style pressure and strengthen the identity reference.
4. If surfaces look crunchy, reduce stylization/detail language and request softer tonal transitions and realistic texture scale.
5. If skin looks oily, reduce frontal fill and global gloss language; request small shaped highlights, matte-to-satin variation, and preserved far-cheek shadow.
6. If the image looks generic, improve concrete casting, tailoring, pose, background design, and light motivation instead of adding quality tags.

## Deliverable notes

- Provide one clean copy-paste prompt.
- Explain reference placement or parameter choices in no more than a few lines unless the user requests teaching.
- Do not append obsolete version flags or undocumented parameters from memory; verify unstable syntax.
