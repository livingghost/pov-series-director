# Target Adaptation as Editorial Rewriting

Target adaptation is not a keyword swap, a parameter toggle, or a command to “enter” a mode. The same story beat must be **re-authored around the evidence and operations the selected surface actually receives**.

Keep the complete director package. Then produce a different submission when the input evidence changes.

## 1. Begin with the irreducible shot

Before choosing a target operation, write:

```text
Opening image:
Dominant visible change:
Physical and emotional cause:
Required performance detail:
Contact or prop continuity:
Landing image:
Dialogue and sound:
What must be exact:
What may vary:
```

Example:

```text
Opening image: pillow-height POV; white-furred guardian stands beside the left bed edge holding a folded dark shirt; rain-lit rear-right window.
Dominant visible change: he approaches and sits at the mattress edge without losing the shirt.
Cause: close thunder startles the POV and draws his ears before his gaze.
Performance: alertness softens into reassurance after he sits.
Contact/prop: two-handed shirt grip remains; his weight visibly compresses the mattress.
Landing: seated upright at the left edge, shirt across both forearms, gaze returned to POV.
Dialogue/sound: rain bed, thunder trigger, then “Safe.”
Exact: POV relation, shirt ownership, stand-to-sit order, readable landing.
Variable: exact step count, precise lightning shape, minor cloth folds.
```

This remains the creative truth across targets.

## 2. Choose the operation that carries the hardest evidence

Choose by what must be preserved, not by a fashionable product name.

### Text-to-video

Use when no submitted visual must be preserved and the target can create the scene. The prompt must establish both the visible world and the action. Character identity is more exposed to variation unless another documented subject path exists.

### Image-to-video from one start image

Use when the opening composition and visible identity matter most. The start image carries the initial scene. The prompt directs change. The target must invent everything outside the visible frame and every later pose that is not otherwise supplied.

### First-and-last-frame generation

Use when both endpoints matter and the target exposes distinct start and end inputs. The prompt directs a physically plausible path between images. Incompatible endpoints cannot be repaired by prose.

### Subject- or ingredient-reference generation

Use when recurring subject appearance must be supplied separately and the target documents such inputs. Subject images do not automatically specify room placement, scale, facing, camera, or interaction. The text or another image must establish those.

### Video edit or restyle

Use when timing, motion, camera path, or performance already exists in source footage and should remain. Describe what stays and what changes. The source video is an operand, not merely inspiration.

### Extension

Use when continuation from an accepted source ending is critical. Inspect the actual terminal frame and audio tail. The first verb must be possible from that exact state.

### Performance transfer or lip-sync

Use when body, face, gesture, timing, or exact speech is more important than generating them incidentally in the picture pass. Record the driving performance, character media, and audio relationship explicitly.

### Conventional edit or composite

Use when the desired join, dialogue, sound, typography, or continuity cannot be obtained reliably in one generation. This is a legitimate production decision, not a failure to prompt.

## 3. Same beat, genuinely different submissions

The following are not “modes.” They are different because the generator receives different evidence.

### A. Text-to-video submission

Submitted media: none.

```text
First-person view from pillow height in a narrow bedroom at night. Rain traces a rear-right window. A tall white-furred guardian in dark home clothes stands beside the left edge of the bed, holding a folded dark shirt in both hands. A close thunderclap makes the viewpoint jolt once. His ears angle toward the window before his head follows; then he takes one measured step to the bed and lowers onto the left mattress edge without losing the shirt. His weight compresses the mattress and the fabric settles last. He looks back to the POV in one continuous shot.
```

Why this text is fuller: no image supplies the room, character, placement, prop, or opening composition.

### B. Start-image submission

Submitted media: a complete first frame showing the room, guardian, prop, and POV relation.

```text
A close thunderclap causes one small first-person jolt. His ears angle toward the rainy window before his head follows. Keeping the folded shirt in both hands, he takes one measured step to the left mattress edge and lowers into a seated position. The mattress compresses beneath his weight; his loose sleeve and the folded fabric settle after his torso. He returns his gaze to the POV and the camera finishes level in one continuous hold.
```

Why this text changes: the image carries the initial visual facts, so the text spends its capacity on choreography and response.

### C. Start-and-end submission

Submitted media: standing start image and seated end image.

```text
Connect the supplied frames with one natural first-person action. After the thunder, his ears turn toward the window before his head. He takes the short step to the mattress and lowers into the supplied seated pose without changing his two-handed hold on the folded shirt. His weight compresses the mattress before his torso settles; the folded fabric and loose clothing come to rest last.
```

Why this text changes: both endpoints are visual. The prompt specifies order, mechanics, and causality between them.

### D. Subject-reference submission without a start image

Submitted media: documented subject references only.

```text
First-person view at pillow height in a rain-lit bedroom. Place the referenced white-furred guardian in the open strip beside the left edge of the bed, full body visible and correctly scaled to the mattress. He holds a folded dark shirt in both hands. A thunderclap makes the viewpoint jolt once; his ears turn toward the rear-right window before he takes one measured step closer and settles.
```

Why this text changes: subject references may carry appearance, but scene, placement, scale, camera, and action still require construction.

### E. Video edit/restyle submission

Submitted media: source video already containing the desired performance and camera.

```text
Keep the source timing, first-person camera path, stand-to-sit action, two-handed prop grip, and final bedside pose. Transform the visible figure into the approved white-furred guardian in dark home clothes, transform the room into the rain-lit bedroom, and preserve the source mattress response and cloth timing.
```

Why this text changes: motion and timing come from the operand. Re-describing them as new generation instructions risks changing what should remain.

### F. Extension submission

Submitted media: accepted source video whose actual ending has been inspected.

```text
Continue directly from the supplied ending. Keep the camera at its actual pillow height and roll. The guardian maintains the shirt in its current terminal grip, lowers his gaze toward the opened blanket, shifts only the short distance available from his stance, and settles beside the POV. The rain ambience continues without restarting.
```

Why this text changes: the extension begins from actual rendered state, not from the planned endpoint.

## 4. Treat target facts as dated evidence

For each operation, record facts that have direct packaging consequences:

```text
Evidence date and source:
Exact product/editor/API surface:
Controls or request keys visible/documented:
Accepted media types and counts:
Allowed durations/aspects/settings used:
Which controls can coexist:
Prompt and separate-field behavior:
Prompt rewriting or hidden transformation that is documented:
Output retrieval path:
Unknowns that remain:
```

Do not turn uncertain behavioral impressions into universal properties. “This variant ignored the left hand” is a run observation. It does not prove that the target cannot represent left hands.

## 5. Dated worked distinctions from official documentation

These examples are dated worked packages. Each submission sheet records the official sources and check date that justify its concrete controls; none of those facts should be treated as timeless assumptions.

### Runway Gen-4.5 image-to-video example

The dated official documentation used by this release describes image-to-video as accepting an image and text, with the input image acting as the first frame; it recommends focusing the text on motion and temporal development. The repository package therefore uses a complete start image and a choreography-focused prompt. It does not claim that a private `character_reference` label binds a separate identity unless the actual surface exposes such a control.

See `examples/storm-watch/runway-gen45-i2v/`.

### Veo 3.1 first-and-last-frame example

The dated official documentation used by this release exposes separate start and last-frame image fields/keys and a primary prompt, with a documented REST negative-prompt parameter. The repository package therefore supplies two concrete endpoint images, a path-focused primary prompt, and a separate exclusion file for the REST example. It does not paste the exclusion list into a console field that the documented console procedure does not expose.

See `examples/storm-watch/veo31-first-last/`.

### Seedance 2.0 first-and-last-frame example

The surface documented by this release is OpenRouter's video endpoint, checked and directly observed on 2026-08-04: both endpoint images travel as `frame_images` entries distinguished by `frame_type` values `first_frame` and `last_frame`, base64 data URLs are accepted, no separate exclusion parameter exists, and an audio-generation flag is documented. The package therefore writes every exclusion into the primary text, one negation per artifact, ships no exclusion file, and attempts rain and thunder in the picture pass as a hypothesis with the post stems as authority.

The same model reached through BytePlus ModelArk documents a different request shape entirely: one `content` array with `role` values, URL-reachable media, and a `camera_fixed` parameter. Same model name, different surface, different submission, which is this reference's point at its sharpest. The branch also performs the same operation on the same two files as the Veo example and still needs a different submission, primary prompt, and requirement-transfer table.

See `examples/storm-watch/seedance20-first-last/`.

The Runway and Veo packages are explicitly marked `not run`; their value is operational specificity, not claimed output fidelity. The Seedance branch additionally carries preserved run evidence in its result log.

## 6. Prompt rewriting is part of the real surface

When official documentation states that a service rewrites prompts, preserve the exact text you submitted and note that the model may receive transformed text. If the rewritten prompt is returned, preserve it as run evidence. Do not call the pre-rewrite text a deterministic instruction program.

The editorial response is not to create a `rewrite_behavior` label and assume the problem is solved. It is to:

- keep exact submitted text;
- preserve returned rewritten text when available;
- compare outcomes across concise and detailed submissions;
- move visually critical facts into submitted media when text transformation makes them fragile;
- avoid attributing a result to wording alone when the actual rewritten prompt is unknown.

## 7. Negative and exclusion language must follow the actual surface

A director package may contain important constraints. Transfer them based on real controls:

- strengthen desired framing or state in the submitted image;
- write constructive positive action in the main prompt;
- use a documented separate negative field when available;
- correct through edit/crop/composite when generation cannot guarantee it;
- record accepted variation.

Do not convert every constraint into `Do not ...` sentences, but do not delete the constraint either.

Example:

```text
Director requirement: POV face never appears.
Start image: camera at eye/pillow height with no reflective surface or reverse angle.
Primary prompt: camera turns only toward the bedside and finishes level; continuous first-person viewpoint.
Separate exclusion field, when documented: selfie view, visible camera wearer, mirror reflection.
Review: inspect every variant for face/reflection; crop or reject on violation.
```

## 8. Adaptation is complete only when something observable changes

A target distinction earns a place in the workflow when it changes at least one of:

- the asset created;
- the file submitted;
- the actual target control used;
- the exact primary or auxiliary field text;
- the clip split;
- the post-production path;
- the review criteria.

If two named strategies produce the same files, same controls, same text, and same review, they are not operationally distinct. Remove the duplicate label, not the directing knowledge.
