# Core Production Rules

These are editorial and production defaults. Exact target operations come from current evidence recorded in `production-state.md` and an operation card. Do not replace concrete direction with labels, but keep useful internal IDs for continuity and lineage.

## 1. Record actual asset use

For each asset used in a generation, record:

```text
asset ID/version
actual file
actual target control or request key
actual operator action
what visible/audible evidence the file supplies
what the prompt must still establish
what remains unsupported or deferred
```

Internal shorthand may accompany this record:

- `reference`: the target observes the file without directly transforming its frames;
- `operand`: the target edits, restyles, extends, composes, or transforms the source frames;
- `anchor`: inspected visual boundary evidence, whether submitted or used only by production;
- `planning-only`: useful to the director but not sent to the target.

The shorthand is not the decision. These two uses of the same V file are different:

```text
V04-r1 -> uploaded as source video in Edit Video; preserve timing/camera/action; transform setting and character appearance.
V04-r1 -> viewed by the director only to design a new text-to-video camera path; not submitted.
```

Use semantic tokens such as `S01`, `C01`, or `V04` in production records when they improve lineage. Exact target text must either translate them into self-contained visual language or use actual documented target tags.

## 2. Describe intended influence as a hypothesis and review plan

It is useful to say which aspects an input should contribute, but the model has not signed a dimension contract.

Write:

```text
Intended use of C01-v3:
- carry face shape, fur pattern, brow scar, and dark home clothing;
- it does not establish bedroom placement, camera height, or two-handed shirt grip.

Submission:
- upload C01-v3 to the documented subject-reference input.

Prompt consequence:
- still describe the rain-lit bedroom, full-body scale beside the mattress, facing, prop, and action.

Review:
- score identity separately from placement and prop continuity.

Fallback:
- if placement or grip drifts, make a composite start frame or use an edit/restyle path.
```

For a video operand, identify what source evidence should remain and what must change:

```text
Preserve from source V04-r1: camera path, stand-to-sit timing, two-handed grip, mattress compression.
Transform: character appearance, room design, clothing, rain lighting.
Review: compare timing/contact against source and identity/environment against approved assets.
```

This description changes the actual submission and review. A bare list of dimensions does not.

## 3. Identity, style, and location continuity

- Bind every visible recurring character to approved media or explicitly accept text-only regeneration risk.
- Use one or two distinctive approved visible anchors when they can appear in the frame; do not invent features to compensate for missing identity evidence.
- Select the series style from approved media and canon. Do not impose photorealism, illustration, or another style family by default.
- Reuse or derive returning locations from accepted scene media when continuity matters. Intentional redesign uses explicit derivation, scope, and supersession.
- Character portraits establish only what they visibly show. They do not establish room scale, ground contact, placement, facing, or interaction.
- Planning layouts guide the director. They affect the generator only when translated into submitted media, prompt text, source operands, or edit instructions.

## 4. Inspect operation-specific evidence

### Fresh text-to-video

No literal visual boundary is supplied. The prompt must establish the visible opening and action. Record compositional variation as expected risk.

### Start-image or image-to-video

Inspect the exact image submitted. Write the first verb from its visible pose, gaze, prop, light, and camera state. Do not treat out-of-frame space as fixed.

### Start-and-end frames

Inspect both images. Check identity, topology, scale, camera relation, prop ownership, light logic, and physically connectable poses. Rewrite or regenerate incompatible endpoints before submission.

### Subject references

Inspect the identity evidence and describe missing scene/blocking/action facts elsewhere. Verify that the actual surface accepts the subject files in the same operation.

### Edit/restyle

Inspect the source across the relevant time range. State what source timing, motion, contact, and occlusion remain, and what is transformed.

### Extension

Inspect the accepted source's actual final seconds, terminal frame, and audio tail. Continue from that state, not the planned state.

### Composition/transition

Inspect every source boundary. A generated transition is appropriate only when the surface accepts the required source operands or boundary controls and the images can connect physically. Otherwise design a conventional cut, match action, insert, or intermediate bridge.

### Performance transfer/lip-sync

Inspect the driving performance, character media, and audio. State which source supplies movement, facial performance, speech, timing, and appearance.

## 5. Use a semantic density budget without erasing coupled detail

Do not enforce one English word count. Judge the number of independent objectives.

A short clip can contain several micro-actions when they belong to one causal chain:

```text
thunder -> ears turn -> head follows -> one step -> sit -> mattress compresses -> cloth settles -> gaze returns
```

These are not eight unrelated beats. They describe the readable mechanics of one response and one relocation.

Competing objectives overload the clip:

```text
wake, inspect three objects, turn, introduce a character, cross the room, open a window, exchange dialogue, reveal a clue, change weather, and end in a new location
```

When overloaded, preserve the director package and make a real editorial change:

- split the shot;
- remove or move an independent event;
- keep a stable performance hold for dialogue;
- move exact speech/audio to another pass;
- create an endpoint image;
- use an edit or performance-transfer source;
- simplify camera motion while retaining body and material feedback.

Do not solve overload by stripping the remaining action to “moves cinematically.”

## 6. One beat, one dominant causal change

A beat normally has:

- one active objective;
- one initiating cause or continuing condition;
- one dominant visible change;
- linked preparation, response, and settling motions;
- one readable end state.

Valid:

```text
The POV lifts the near blanket edge and holds it open. The knight places his right hand outside the POV wrist, lowers his weight onto the left mattress edge, and lets the mattress pull one fold through the blanket before both bodies settle.
```

The hand action, contact, compression, and cloth response are parts of one invitation-and-sit event.

Overloaded:

```text
The POV opens the blanket, stands, crosses the room, opens the window, laughs, answers the knight, and discovers a hidden object.
```

Dialogue may accompany a stable hold or small linked action. Avoid intricate hand work, large relocation, and rapid camera movement during an important line unless a source performance or tested workflow carries it.

## 7. Design transitions and endings as production assets

- Prefer one continuous location per short clip unless the story requires a cut.
- Every camera turn has a visible/audible trigger and a re-anchor.
- Every accepted clip produces an inspectable terminal frame and audio tail.
- The landing describes character pose, gaze, prop ownership, contact, camera height/roll/direction, and light state.
- A weather/light change inside one location is not automatically a scene transition.
- A segment's endpoint must physically permit the next first verb.
- When the next clip needs a more precise endpoint than free generation can provide, create and submit an end frame where supported, use an edit, or redesign the boundary.

A label such as `bridge` is useful only when the package states the actual bridge:

```text
visual: camera settles on seated guardian at pillow height;
audio: rain continues across the cut; thunder tail decays before the next line;
action: folded shirt remains across both forearms;
edit: cut on the end of mattress compression.
```

## 8. Dialogue, sound, subtitles, and text are separate deliverables

Preserve for every critical line:

- exact text;
- speaker;
- language and speech stage;
- voice and breath direction;
- visual performance window;
- selected production route;
- subtitle/caption requirement.

Possible routes include same-pass generation, a separate dialogue pass, performance/lip-sync, audio post, or subtitles/captions. Uncertain native speech does not justify deleting the line.

Use an ambient bed plus functional effects:

```text
steady rain = continuous bed;
close thunder = trigger for POV jolt and ear response;
mattress/cloth = subordinate contact sounds;
spoken “Safe.” = after the body lands and camera stabilizes.
```

Subtitles default to off. When requested:

- `sidecar`: timed caption file outside picture generation;
- `metadata`: translated/caption text for later production;
- `burned in`: deliberately generated on-screen text only with user intent and current evidence;
- multiple tracks: separate language-labelled deliverables.

Never assume English and never paste subtitles into the visual prompt by default.

## 9. Replace taboo walls with constructive fixes

Find and repair:

- contradictory camera paths;
- several independent active objectives;
- impossible first verbs relative to the submitted frame;
- off-frame geometry treated as already fixed;
- ambiguous limb ownership or contact;
- identity/reference assumptions unsupported by actual controls;
- static image description crowding out temporal action;
- empty quality praise replacing visible facts;
- omniscient information the POV cannot see or hear.

Write the desired construction:

```text
Weak prohibition: Do not show the POV face.
Constructive package: start image has no mirror or reverse angle; the gaze turns only toward the bedside; camera ends level at pillow height; inspect every variant for reflection/selfie drift.
```

```text
Weak prohibition: No duplicated hands.
Constructive package: POV left hand holds the near blanket edge throughout; knight right hand lands on the mattress outside that wrist; contact stays visible until both settle.
```

Use a documented negative/exclusion field as an additional channel when available, not as the whole design.

## 10. Diagnose rejected submissions by controlled comparison

Treat submission rejection as surface-specific evidence.

1. Preserve exact target, operation, files, text, settings, date, and error.
2. Keep required media and minimum valid structure fixed.
3. Change one editable part at a time or bisect the text to isolate the smallest reproducible trigger span.
4. Test the isolated token, phrase, and sentence; context may matter.
5. Record exact successful and rejected submissions.
6. Scope the finding to the exact surface/date and mark uncertainty.
7. Rewrite with the shortest concrete language that preserves the intended visible action.

Do not turn a trigger note into a universal forbidden-word list.

## 11. Creative-requirement transfer replaces the old constraint block

Before submission, ensure each critical requirement has a real carrier:

| Requirement | Media/control/text/post carrier | Exact implementation | Review | Fallback |
|---|---|---|---|---|

Typical requirements include:

- POV identity and body visibility;
- recurring character identity/clothing;
- opening and landing geometry;
- action order and causal mechanics;
- contact point, limb ownership, occlusion, and feedback;
- prop identity and ownership;
- dialogue/speaker/language/voice;
- sound, weather, light, and music;
- visual-quality and style continuity;
- transition and audio tail.

The transfer table prevents two opposite failures: hiding everything in a production document the target never sees, and deleting rich direction simply because one prompt field cannot carry it all.
