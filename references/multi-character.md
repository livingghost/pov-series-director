# Multi-Character POV Blocking and Scene-Reference Workflows

## 1. Blocking rules

1. **POV-centered fan.** Place characters in left-front, front, or right-front positions and near or far depth rings, anchored to landmarks directly observed in the relevant inspected frame or planning layout.
2. **One active subject per beat.** Everyone else holds a readable idle pose or reacts minimally.
3. **Gaze controls coverage.** A turn needs a trigger. Looking at a speaker is the default; watching the listener while the speaker remains off-frame is an advanced reaction shot.
4. **Name every actor.** Avoid collective pronouns when limb ownership or movement order matters.

Three visible recurring characters is a conservative editorial starting point for a short POV episode. More characters require simpler motion, fewer lines, and stronger landmark anchoring.

## 2. Blocking table

Use a table before the prompt when two or more characters are visible:

```text
C01 = left-front, near, beside the chair arm
C02 = front, far, aligned with the window
C03 = right-front, near, hand resting on the table edge
POV = doorway threshold, facing the table
```

Update it after a deliberate camera turn or major relocation.

## 3. Zero-simile blocking

Visual similes add literary noise and may contaminate generation. Delete the comparison and write pose, speed, amplitude, and end state.

- Instead of `like delivering a report`: back straight, chin tucked, words clipped one by one.
- Instead of `like receiving a relic`: takes it with both hands level, fingertips together, breath lowered.

Dialogue similes remain allowed when character-specific.

## 4. Eliminate explanatory shots

Every look needs a character motive.

- reveal the room while the POV performs a necessary action
- introduce a prop when a character hears, sees, offers, or reaches for it
- show a setting through its physical consequence
- never restate what the approved image already establishes
- ask `why is the POV looking here now?`; the answer cannot be `so the audience knows`

## 5. Scene-reference workflows

These names are optional headings. The distinction exists only when the created/submitted media, exact text, or operator action changes.

### Literal start-frame workflow

The approved image is exactly what the POV sees at time zero. Submit it to the actual start-image control when available. The first verb must follow its visible camera, pose, prop, light, and character state.

Concrete record:

```text
S02-v1 -> Start image control
Visible opening: POV at doorway threshold; sofa arm near left; C01 seated beyond it.
Prompt consequence: do not re-establish the room; direct the gaze turn and C01's action.
```

### Planning-layout workflow

The image is a spatial dictionary seen by the director, not necessarily by the video target.

1. Declare the POV's position and facing inside the layout.
2. Translate image-absolute landmarks into POV-relative directions.
3. Carry those relations into a submitted start/end image, source video, mask, or exact text.
4. Record whether the planning image itself was submitted.

Example:

```text
Planning image: S01-v2, submitted: no
POV position: doorway threshold
POV facing: sofa
Transfer to exact prompt: "The sofa arm is near on the left; the seated character remains beyond it with the rear window behind him."
```

Without the transfer line or derived submitted media, the layout does not control the target.

### Composite start-frame workflow

Use when one visual input must carry scene, cast, outfit, scale, pose, prop, and opening composition. Generate the actual opening frame with all visible main characters already placed. Identity images may be used upstream to create the composite even when the motion target cannot receive them separately.

The submission sheet must map the composite to the real start-image control, and the prompt should concentrate on the subsequent action rather than reintroducing characters already visible.

### Text-led workflow

Use when the motion target receives no scene image. Inspect a planning image, translate only camera-readable geometry into the exact text, and accept that composition remains generated rather than visually bound. Reduce fragile simultaneous blocking or choose another operation when precision is essential.

Do not call this a visual reference. The target receives text.

## 6. Coordinate translation table

```text
Image landmark | image-absolute location | POV-relative location | allowed motion path
sofa            | image left              | POV front-left        | doorway to sofa edge
window          | rear wall                | behind C01             | no crossing path
```

Every directional phrase in the exact prompt must be explainable from this table, a submitted literal frame, or another concrete source that the target actually receives.
