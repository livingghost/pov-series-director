# Runtime Target Evidence, Operations, and Clip Packing

The exact generation target is a runtime dependency. Product names, editors, APIs, accounts, regions, and model revisions can expose different operations. Resolve only the facts needed for the current submission, and record their concrete consequences.

A capability label is an index, not a promise. `first-frame input available` matters only when it is followed by the real control, the real file placed there, and the prompt rewrite that results.

## 1. Separate three kinds of statement

### Documented or observed surface fact

A control, request key, accepted media type, duration choice, or operation is visible on the exact surface or stated in current authoritative documentation.

```text
The current editor exposes separate Start and End image controls.
The API example places the first image in `instances[0].image` and the last in `instances[0].lastFrame`.
The duration selector currently offers 4, 6, and 8 seconds.
```

### Production decision

A decision made for this shot because of those facts.

```text
Use the standing frame as Start and the seated frame as End.
Ask the prompt only for the causal path and material response between them.
Route the spoken line to post so picture generation can remain a stable stand-to-sit action.
```

### Observed run behavior

Something directly seen or heard in preserved returned output.

```text
Variant 2 began close to the supplied Start image but changed the two-handed grip before sitting.
All four variants compressed the mattress; none preserved the exact brow scar.
```

Do not promote a run symptom into a permanent product limit. Do not present a documented input as proof of output fidelity.

## 2. Evidence priority and freshness

Use, in order:

1. current controls visible on the exact surface being used;
2. current official documentation for that exact product/API/model;
3. inspectable material supplied by the user for the current workspace;
4. same-workspace run records with exact submission provenance;
5. older notes, marked for recheck.

Record the date and exact surface. Recheck when:

- the editor, API version, model selector, tier, account, or region changes;
- current controls contradict the stored record;
- packaging is rejected;
- documentation marks the operation deprecated or changed;
- the user asks for a different surface.

Unknown remains unknown. A filename or note that says `verified` does not authenticate itself.

## 3. Operation proof card

Complete one card for every actual generation or edit operation.

```text
Operation name used by the surface:
Exact product/editor/API/model shown:
Evidence date and source:

Actual controls or request keys used:
- [control/key] <- [exact file or text]

Settings selected:
- duration:
- aspect ratio/resolution:
- result count/seed/quality, when exposed:

What submitted media visibly supplies:
- opening composition:
- subject appearance:
- endpoint:
- source timing/camera/performance:
- masks or regions:
- audio/performance driver:

What exact text must still establish:
- scene facts absent from media:
- action and order:
- physical response:
- performance:
- landing:
- dialogue/audio instructions:

What is not carried by this operation:
- [requirement] -> [alternate generation/edit/audio/post route or accepted variation]

Known prompt transformation:
- none documented | documented rewrite | unknown

Run evidence available:
- not run | exact run record path
```

This card replaces the false certainty of a large table filled with `yes`, `no`, and `approximate` values.

## 4. Asset type, actual use, and intended influence

### Asset type

Use stable bookkeeping IDs:

- `C`: recurring character identity media;
- `S`: still frame, scene, layout, composite, boundary, or keyframe media;
- `P`: recurring prop media;
- `V`: video media;
- `A`: audio or performance media.

Type does not determine what a target does with the file.

### Actual use in one operation

Record the concrete operator action:

```text
S03-v2 -> uploaded to Start image control
S04-v1 -> uploaded to End image control
C01-v3 -> uploaded to Subject reference slot 1
V09-r1 -> selected as source clip for Edit Video
A02-v4 -> selected as driving performance audio/video
P01-v2 -> not submitted; descriptive continuity note only
```

Words such as `anchor`, `reference`, and `operand` may summarize these lines in internal tables. The line above is the real distinction.

### Intended influence

A source may be intended to contribute identity, opening geometry, endpoint, motion, timing, lighting, voice, or another dimension. Record this as a production hypothesis, not a contract imposed on the model:

```text
Intended influence: use C01-v3 for face, fur pattern, and clothing; do not assume it establishes bedroom placement or camera height.
Review consequence: score identity separately from placement.
Fallback: if placement drifts, build a composite start image rather than adding another identity adjective.
```

## 5. Operation-specific continuity evidence

### Fresh generation without submitted visual evidence

No image “locks” the opening. Write the scene and accept that composition is generated. Use approved references only through controls the surface actually exposes.

### Start-image generation

Inspect the actual image to be submitted. Record only visible geometry. Anything outside the frame remains unconstrained unless supplied elsewhere. The first verb must be compatible with the visible starting state.

### Start-and-end generation

Inspect both images. Verify the same identities, topology, prop ownership, light logic, camera relation, and physically connectable poses. The prompt describes the path; it should not ask the target to finish somewhere incompatible with the end image.

### Subject-reference generation

Inspect the subject images for identity and costume. Do not infer scene placement from portrait references. Establish scale, blocking, contact, and camera elsewhere.

### Video edit or restyle

Inspect source frames across the clip, not only the first frame. Identify what source timing, action, camera, occlusion, and contact must survive, and what is being transformed.

### Extension

Inspect the accepted source video's actual final seconds, final frame, and audio tail. The continuation begins from the rendered state, including accidental but visible pose changes that the next clip must either accept or repair.

### Transition generation

Inspect both outgoing and incoming boundary frames. If the target cannot accept both boundaries or the images are topologically incompatible, use a conventional edit, intermediate bridge asset, or redesigned shot rather than claiming a generated transition is solved.

### Performance transfer

Inspect both the driving performance and character media. Identify which source supplies body movement, facial movement, speech, framing, and character appearance. Preserve the driving material in the run package.

## 6. Input-combination proof

Do not infer that separately documented controls can be used together. For the current surface, preserve evidence or mark unknown for combinations such as:

- start image + subject references;
- start image + end image + subject references;
- source video + subject reference + audio driver;
- source video + first/last keyframes;
- multiple subjects + a scene reference;
- native audio + negative field + prompt rewrite.

When a desired combination is unavailable or unverified, change the production package:

- composite identity and scene into a start image;
- split the shot at the reveal;
- generate a clean performance first and restyle it;
- create picture first, then dialogue/audio;
- use edit/composite rather than one-pass generation.

Do not merely change a field from `yes` to `no`.

## 7. Binding syntax

A target binding is real only when the exact surface documents or exposes it.

Examples of real binding evidence:

```text
File dropped in Start control
File selected as source video operand
Subject image assigned to a named slot shown by the editor
API request key containing the media URI
Documented prompt tag created by the surface itself
```

Internal tokens such as `{{OPENING_ANCHOR:S01}}` remain useful in the director package. They are removed from exact submitted text unless converted to an actual documented target tag. Full editorial rewriting is required; textual substitution alone cannot decide which scene facts the media already carries.

## 8. Clip packing is delivery arithmetic, not feasibility proof

Given a required story duration `T` and allowed clip durations `D`, choose a sequence whose sum covers `T` with:

1. minimum overrun;
2. fewest clips;
3. later-clip slack when possible.

A dynamic-programming implementation may help calculate the sequence. The result proves only that the selected durations can cover the planned story time.

It does **not** prove that:

- every beat will happen at the assigned second;
- the target will obey timestamp ranges;
- a dense action can be generated coherently;
- dialogue will fit or occur at the intended time;
- transitions will be natural.

Before packing, pass the shot-feasibility questions in `references/prompt-composition.md`:

```text
Can the start be drawn as one frame?
Can the end be drawn as one frame?
Can the dominant visible change be said in one sentence?
Are the micro-actions coupled to that change or competing with it?
Can the camera and body physically perform the path?
Does contact have ownership, occlusion, response, and landing?
```

Then use duration options to decide clip boundaries.

### Packing example

Target story duration: 15 seconds. Allowed durations: 4, 6, 8 seconds.

```text
8 + 8 = 16 seconds
```

That may be the arithmetic choice. Editorially, the 1-second slack must be placed where a hold, breath, reaction, or bridge is useful. Do not fill it with another independent event merely because time remains.

## 9. Timing language

Use exact time ranges only when they serve the operator and have evidence on the selected surface. Even then, treat them as desired timing, not an edit-timeline guarantee.

Prefer causal or ordered timing when exact adherence is unknown:

```text
At the thunder, the viewpoint jolts once.
After his ears turn toward the window, his head follows.
Once his weight settles on the mattress, he looks back and speaks.
```

A post-production timeline may still use precise seconds. Keep that timing in the director/edit package even when the generator prompt is written causally.

## 10. Dialogue, sound, text, and subtitles

A surface that can produce sound does not thereby guarantee:

- exact dialogue wording;
- correct speaker ownership;
- voice identity;
- lip synchronization;
- timing;
- mix clarity;
- multilingual accuracy.

For every critical line, preserve the line, speaker, language, voice direction, performance window, and chosen route:

```text
same-pass native generation
separate dialogue generation
performance/lip-sync operation
audio post with stable visual hold
subtitle or caption track
```

Likewise, a target that accepts a prompt does not guarantee reliable on-screen typography. Sidecar subtitles and post typography remain preferred when text accuracy matters.

## 11. Soft heuristics from runs

Run-derived tactics are scoped notes, not hard capabilities.

Record:

```text
Symptom:
Exact submission and variants inspected:
Observed evidence:
Smallest plausible mitigation:
Scope: exact surface/model/operation/shot family
Counterexample or uncertainty:
Re-test condition:
```

Example:

```text
Symptom: the two-handed shirt grip changed during a combined turn-and-sit prompt.
Evidence: three of four variants from run R017.
Mitigation: keep the guardian facing the bed in the start image and remove the simultaneous head turn from the sit pass; restore the look-back after landing.
Scope: current start-image operation and this contact geometry.
Uncertainty: not evidence of a global prop-continuity limit.
```

## 12. Packaging gate

Before calling a clip ready for submission, verify:

- the exact operation and current surface are identified;
- every submitted file exists and has been inspected;
- boundary media are conformed to the delivery resolution, and continuation anchors derive from extracted real frames;
- each file is mapped to a real control or request key;
- exact primary and auxiliary field contents are preserved;
- the prompt's first verb can follow the submitted opening state;
- the endpoint and continuity requirements are carried by media, text, another pass, or an explicit accepted variation;
- input combinations are documented or visibly available;
- clip arithmetic and shot feasibility are both addressed;
- unsupported requirements have concrete alternate routes;
- the result log does not claim observations before a run exists.
