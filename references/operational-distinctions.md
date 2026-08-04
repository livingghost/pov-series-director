# Operational Distinctions: A Name Is Not the Distinction

This Skill may use short labels to keep project records readable. The label is never the instruction. A distinction is useful only when it changes the submitted media, the field that receives it, the exact wording, the post-production route, or the evidence required for the next decision.

For every named distinction, answer four questions in ordinary language:

1. What does the operator do differently?
2. What does the video model actually receive differently?
3. What sentence or shot design changes?
4. What visible or audible failure becomes likely when the two cases are confused?

If those answers cannot be shown with a paired example, keep the term as an editorial note rather than presenting it as a control.

## 1. A first frame is not a subject reference

Same story intent: a white-furred knight stands beside a bed and takes one step toward the POV.

### Submission A: the knight is already in the first frame

Operator action:

```text
bedroom-with-knight.png -> the target's start-image field
```

The image supplies the time-zero composition, the knight's location, approximate pose, room layout, light, and visible clothing. The submitted text can concentrate on movement:

```text
The viewpoint makes one small waking jolt. The white-furred knight takes one measured step from the left bedside toward the mattress while keeping the folded dark shirt in both hands. His boots stop beside the bed; the loose fabric settles after the step. One continuous first-person shot.
```

### Submission B: the knight is supplied only as a subject reference

Operator action:

```text
empty-bedroom.png -> the target's start-image field
knight-reference.png -> a documented subject-reference field
```

The room image does not place the knight in the scene. The prompt must create that spatial relation:

```text
Start from the supplied empty bedroom frame. Place the white-furred knight from the subject reference on the open strip beside the left side of the bed, full body visible and correctly scaled to the mattress. He faces the rain-lit window while holding a folded dark shirt in both hands, then takes one measured step toward the mattress. The first-person viewpoint remains at pillow height.
```

The distinction is real because the second submission contains an additional field and asks the model to solve placement and scale. If the target has no subject-reference field, calling the second image a `character reference` does nothing. Practical choices are to create a composite start image, accept text-generated identity, redesign the blocking, split the shot, or select another documented operation.

## 2. A planning image is not a submitted image

A storyboard may help the director decide where a door or character should be. It influences the video only when one of these transfer paths is completed:

- the storyboard or a derived image is actually submitted in a supported field;
- its relevant visible facts are rewritten into submitted text;
- the operator uses it to create a different start/end image, mask, source video, or composite that is submitted.

Paired consequence:

```text
Planning-only use:
The director sees a doorway on the left, but the model receives neither the image nor a sentence about the doorway. The doorway is not controlled.

Submitted use:
The start image visibly contains the left doorway, or the text says, "A narrow open doorway remains on the far-left wall as the viewpoint turns." The model receives the fact.
```

Do not delete useful planning references. Record the transfer path from planning material to model-facing evidence.

## 3. A video reference is not a video operand

Same source video: a camera walks through a narrow hall and turns right at the end.

### Reference use

The target observes the source as guidance while generating new frames.

```text
source-hall-walk.mp4 -> documented motion/reference field
new character/scene inputs -> their own fields
```

The prompt describes what to borrow and restates the new scene:

```text
Use the supplied motion reference for the walking cadence and the single right turn. Generate the new scene as a torch-lit stone corridor from first-person eye height. The white-furred knight walks one pace ahead; his dark cloak reacts to each step. The source video's walls, people, colors, and audio are not part of the intended scene.
```

The final sentence records a selective-transfer intention. Whether the surface actually isolates those dimensions must be observed.

### Operand use

The target edits, restyles, extends, or composes the actual source frames.

```text
source-hall-walk.mp4 -> documented video-edit or extension input
```

The prompt describes the delta:

```text
Retain the source video's camera path and timing. Replace the modern hallway with a torch-lit stone corridor and replace the visible guide with the approved white-furred knight. Keep each footfall and the final right turn aligned to the source motion.
```

If the source is only observed, the path may be reinterpreted. If the frames are transformed, the path may be inherited more directly. The operator action, prompt, and review are therefore different; `reference` and `operand` only index that difference.

## 4. A performance driver is neither of those by default

A driving performance video may supply timing, expression, gestures, speech, or body movement to a character asset on a dedicated performance-capture surface.

```text
driver-performance.mp4 -> documented driving-performance field
character-front.png -> documented character field
```

The production package must judge the result against the driver:

- did the gesture occur at the same point?
- did the facial expression belong to the intended character?
- did audio come from the driver or another field?
- did the operation retain or replace the original camera/environment?

Calling the driver a generic `motion reference` hides these production consequences.

## 5. Start-only and start-plus-end submissions require different writing

Same intent: the knight moves from standing beside the bed to sitting on its edge.

### Start image only

The endpoint exists only in language:

```text
The knight crosses the short gap and lowers himself onto the left edge of the mattress in one continuous motion. The mattress compresses under his weight. He finishes upright, still facing the window, with the folded shirt resting across both forearms.
```

### Start and end images

The target receives both endpoint compositions. The prompt describes the physical path between them rather than redescribing the pictures or introducing a competing endpoint:

```text
Connect the supplied start and end frames with one natural action. The knight takes the short step to the bed, turns only enough to clear the mattress, and sits without changing hands on the folded shirt. His weight depresses the mattress before his torso settles into the final upright pose. The first-person camera remains at pillow height.
```

Confusing the cases wastes prompt space and can contradict the supplied end image.

## 6. A text continuity fact is not a visual lock

Production fact:

```text
The folded shirt belongs to the knight and remains in his hands.
```

If no prop image is submitted, the model must invent its appearance from text. The fact remains useful, but its effect is different from an actual prop image or a start frame that visibly contains the prop.

Use language that states the actual evidence:

```text
The recurring prop is text-described in this generation. Ownership is required; exact folds and stitching may vary.
```

When exact appearance matters, build the prop into a submitted image or use a documented asset-reference path. Do not remove the continuity fact; distinguish narrative continuity from visual evidence.

## 7. A planned end state is not the next clip's opening evidence

Planned sentence:

```text
The knight ends seated upright at the mattress edge.
```

A rendered frame may instead show:

```text
The knight sits farther back, his left shoulder is cropped, the shirt has shifted to his lap, and the camera has rolled slightly clockwise.
```

The next clip begins from the rendered geometry or from a deliberately created corrective derivative. Repeating the planned sentence as though it described the actual frame creates a seam discontinuity.

This is why the workflow changes after a render: not because a hidden review mode switches on, but because a new source of evidence now exists and supersedes the imagined endpoint.

## 8. Same-pass dialogue and post-produced dialogue are different productions

Same canonical line: the knight says, “Safe.”

### Dialogue generated with the video

The exact surface must accept dialogue or audio instructions. The prompt coordinates speech with visible action:

```text
After the camera settles, the knight remains nearly still and says softly, "Safe." His mouth movement belongs to the visible knight; steady rain continues underneath.
```

The review checks wording, speaker, lip motion, timing, voice continuity, and mix separately.

### Dialogue added in post

The picture prompt protects a performance window:

```text
After the camera settles, the knight holds the final pose for one second with a small breath and restrained mouth movement. Steady rain continues.
```

The production record separately specifies the line, voice, timing, dubbing or lip-sync operation, and mix. Removing dialogue from one generator field is not a loss of story function when the line is deliberately preserved in another production path.

## 9. A selectable duration is not timestamp obedience

A surface may expose an eight-second duration while ignoring or loosely interpreting instructions such as `0–2 sec` and `2–5 sec`.

These are different observations:

```text
Documented control:
The operator can select an eight-second output.

Behavioral observation:
In three of four returned variants, the turn completed before the spoken line and the final hold lasted at least one visible beat.
```

Use timestamps when the exact surface documents or repeated runs support that syntax, and still treat adherence as empirical. Otherwise use ordered phases and judge the actual sequence.

## 10. A model-facing prompt is not the whole production

A concise exact prompt may omit static room details because they are visible in the submitted image. It may omit a spoken line because the line is assigned to post. Neither omission is acceptable unless the richer director package and adaptation trace show where the requirement went.

The test is not “is the prompt short?” It is:

```text
Can every important story, performance, continuity, sound, and endpoint requirement be located in submitted media, an exact target field, a deliberate post path, a later operation, or an explicitly accepted area of variation?
```

## 11. Workflow stages are evidence changes, not mental modes

Use stage names only as headings. The operative instructions are the evidence and deliverable:

```text
Before the actual start image exists:
- decide the required composition;
- write the image-generation brief;
- do not claim to have inspected geometry.

After the actual start image is attached:
- describe the visible geometry;
- revise blocking to fit it;
- produce the rich director package and exact target submission.

After generated variants exist:
- inspect every variant;
- compare the actual endpoint with the planned endpoint;
- base the next clip on the accepted frame.
```

`Phase A`, `Phase B`, and `Phase C` are navigation. The concrete change is what evidence may be used and what artifact that evidence is enough to finish.
