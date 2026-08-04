# Prompt Composition: Preserve Rich Direction, Remove Ambiguous Shorthand

A video prompt is choreography under limited attention. The aim is not one verb and not maximum prose. It is a legible causal progression whose start, movement, physical feedback, performance, and landing can be seen from the declared POV.

Keep the full director package even when the exact target prompt becomes shorter. Target media may carry some static facts; post-production may carry dialogue or sound; another shot may carry an action that cannot fit. Nothing important disappears without an explicit production decision.

## 1. Write the shot proposition

Before drafting target text, state the shot in one sentence:

```text
From [visible POV state], [trigger or intention] causes [active subject] to [dominant physical progression], revealing [story/performance value], and ending on [usable visible state].
```

Example:

```text
From a bed-level first-person view, a thunderclap exposes the white-furred knight's fear; he steadies himself, takes one protective step closer without releasing the folded shirt, and finishes in a quiet speaking hold.
```

The proposition is a design check. It does not need to be submitted verbatim.

## 2. Expand the causal spine

A coherent beat may contain several dependent actions:

```text
Opening state: knight stands beside the bed holding the shirt in both hands.
Trigger: close thunderclap.
POV response: one small bodily jolt.
Character response: ears angle toward the window while the body stays planted.
Object response: forearms lift slightly; the folded cloth lifts and settles.
Main action: one measured step toward the bed without changing hands.
Material response: loose clothing and cloth lag, then settle after the foot plants.
Light event: one lightning flash catches the brow scar.
Landing: gaze returns to POV; camera level; stable speaking hold.
```

These details are not independent prompt clutter. They form one chain:

```text
thunder -> involuntary responses -> controlled approach -> protective landing
```

Contrast with unrelated demands:

```text
The POV wakes, the knight crosses the room, opens a window, hands over the shirt, speaks two lines, and sits.
```

That version contains several objectives, relocations, contacts, and endpoints. Split it or choose one progression as the clip's spine.

## 3. Distinguish coupled motion from competing motion

Coupled details belong to the same physical event:

```text
The knight sits -> the mattress compresses -> the blanket ridge shifts -> his cloak settles.
```

Competing details ask the model to solve independent events:

```text
The knight sits while the POV whips toward the window, lightning changes three times, another character enters, and two people speak.
```

Do not count commas or verbs mechanically. Ask whether one event physically causes, supports, or resolves the next. Coupled feedback improves legibility. Independent objectives consume attention and may need separate shots or clips.

## 4. Build from visible start and visible end

Describe the actual opening evidence before deciding the first action.

Bad match:

```text
Start image: the room and character are already clearly visible.
First action: the POV opens their eyes from darkness and discovers the character.
```

Concrete revisions:

```text
A. Change the action: the already-awake viewpoint startles at thunder.
B. Change the image: create a dark, unfocused eyelid/opening frame.
C. Use an intentional blink only when the target and edit path can support it.
```

Then write the landing as a still image that can seed the next clip:

```text
The knight is seated at the left mattress edge, torso upright toward the window, folded shirt across both forearms, POV camera level at pillow height.
```

When an end image is submitted, compare it with the intended physical path before generation. Correct incompatible hands, scale, facing, topology, light, or camera position upstream rather than asking prose to reconcile impossible endpoints.

## 5. Stage space in camera-readable terms

Use relations that a frame can show:

```text
left of the mattress
one step beyond the blanket edge
full body visible at medium distance
rear-right window
hand remains above the blanket line
camera at pillow height
```

Avoid relations that depend on an unavailable production document:

```text
in zone B
according to S01
consistent with the layout manifest
at the approved distance
```

Internal records may keep those IDs. Target-facing text expresses the visible relation or uses actual supported binding syntax.

For two or more characters, build the blocking table in `references/multi-character.md`, then translate it into camera-readable relations.

## 6. Direct POV through the body

A first-person camera is a body, not a free-floating rig.

Use:

```text
The viewpoint rises as the POV props up on one elbow.
The camera dips with a cautious step.
The gaze turns toward the sound and settles on the doorway.
The frame sways once as the mattress shifts beneath the POV.
```

Avoid unexplained rig motion unless the series establishes a physical mechanism:

```text
the camera cranes upward
an orbit circles the POV
an impossible dolly passes through the bed
```

Specify the trigger, body cause, amplitude, and re-anchor. For advanced options, use `references/pov-camera.md`.

## 7. Direct performance through visible behavior

Keep emotional intention in the director package, but translate it into observable behavior:

```text
protective -> he places his body between the window and the POV, shoulders high, voice low
nervous -> his ears react before his head; his grip tightens once on the folded fabric
relieved -> his shoulders lower after the blanket opens; one small exhale follows
```

Use character-approved signals and anatomy. Do not borrow ears, tail, fur, feathers, or species behavior for a human character. Use the tiering and material-response library in `references/performance-details.md`.

Performance details should do different jobs. A small eye/ear change, one grip response, and a light shift can support one emotional change. Three separate gestures that each announce the same emotion may compete.

## 8. Integrate contact with ownership and feedback

A contact direction identifies:

- whose limb moves;
- what it contacts;
- from which side;
- what becomes occluded;
- what physically reacts;
- where both bodies end.

Example:

```text
The POV's left hand lifts the near blanket edge and holds it open. The knight places his right hand on the mattress outside the POV's wrist, lowers his weight, and sits at the left edge. The mattress compresses beneath him and pulls one fold through the blanket. The POV hand remains visible and is never replaced by the knight's hand.
```

This is concrete direction, not a negative list. See `references/contact-scenes.md` for carrying, hugs, face contact, hand contact, and occlusion.

## 9. Integrate dialogue without erasing the shot

Place a line where the speaker can be visually stable:

```text
The camera settles on the knight. He holds the shirt still, gives one small breath, and says softly, "Safe."
```

When a line competes with complex movement, preserve it through a real revision:

- move the line after the action lands;
- shorten it according to the character's grammar;
- split action and speech into adjacent clips;
- generate a stable visual hold and add dialogue in post;
- use a documented performance or lip-sync operation after picture generation.

Do not delete canonical dialogue merely because the selected video surface is uncertain. Keep the line, speaker, language, voice direction, and chosen production path.

## 10. Integrate sound, weather, and light as causes

Sound and atmosphere should participate in the action:

```text
steady rain = ambient bed
close thunderclap = trigger for POV jolt and ear response
lightning from rear-right window = brief reveal of the brow scar
cloth movement = subordinate sound and material response to the step
```

Name light source, movement, and landing point. Weather should affect a body, object, path, sound, or light. Do not replace the actual scene with a global mood adjective.

## 11. Rewrite for the actual input surface

### Text-to-video

The prompt must create the visible scene and the motion:

```text
First-person view from pillow height in a narrow bedroom at night. Rain traces the rear-right window. A tall white-furred knight stands beside the left edge of the bed, holding a folded dark shirt in both hands. A close thunderclap makes the viewpoint jolt; his ears angle toward the sound before he takes one measured step closer. Lightning reveals the scar above his left brow. The camera settles in one continuous shot.
```

### Image-to-video with a complete first frame

The image supplies static scene, identity, pose, and composition. Emphasize change over time:

```text
A close thunderclap causes one small first-person jolt. The guardian remains planted as only his ears angle toward the rainy window; the folded shirt lifts slightly with his forearms and settles. He takes one measured step toward the bed without changing his two-handed grip. His clothing and the folded fabric lag and settle after his foot plants. One lightning flash catches the scar above his left brow. His gaze returns to the POV and the camera finishes level in a stable hold.
```

### First and last frames

The images supply both endpoints. Emphasize the physical path:

```text
Connect the supplied start and end frames with one natural first-person action. The guardian takes the short step to the mattress and lowers into the supplied seated pose without changing his two-handed hold on the folded shirt. His weight compresses the mattress before his torso settles upright. The folded fabric and loose clothing lag behind the movement and come to rest last.
```

### Subject-reference generation

Subject images may establish appearance but not placement. Describe scene, scale, blocking, action, and camera:

```text
Place the guardian from the subject references in the open strip beside the left side of the bed, full body visible and correctly scaled to the mattress. He holds a folded dark shirt in both hands and faces the rain-lit window before taking one measured step toward the POV.
```

### Video edit or restyle

The source frames supply timing, camera, and existing action. Describe what remains and what changes:

```text
Keep the source camera path, timing, and body motion. Transform the setting into the approved rain-lit bedroom and the visible figure into the white-furred knight in dark home clothes. Preserve the final bedside pose and the folded shirt in both hands.
```

### Extension

Begin from the actual accepted terminal frame and audio tail:

```text
Continue directly from the supplied source ending. The camera remains at the same roll and pillow height. The guardian keeps the shirt in its actual terminal grip, lowers his gaze toward the opened blanket, and takes only the short movement available from his current stance. Steady rain continues without an audio restart.
```

These are different submissions because the target receives different evidence. Do not represent the difference only with a `mode` value.

## 12. Use a revision ladder instead of a prohibition wall

Begin with the smallest submitted prompt that still expresses the shot's causal spine, generate variants, and add one missing layer at a time. Keep the rich director package throughout.

Example ladder for image-to-video:

```text
Pass 1: dominant movement
The viewpoint makes one small jolt and the guardian takes one measured step closer before settling.

Pass 2: coupled performance and prop
The viewpoint makes one small jolt. The guardian's ears angle toward the thunder, then he takes one measured step without changing his two-handed hold on the folded shirt. The cloth settles after the step.

Pass 3: light reveal and endpoint
During the movement, one rear-right lightning flash catches the scar above his left brow. His gaze returns to the POV and the camera finishes level in a stable hold.
```

If a target omits a critical detail, change one real production element:

- make the detail clearer in the start/end image;
- reduce a competing objective;
- split the shot;
- change the exact sentence;
- use a performance driver or edit operation;
- route dialogue or sound to another field/post path.

Do not answer every failure by adding a negative sentence. Do not answer every complexity problem by deleting physical feedback and performance.

## 13. Final composition check

Before submission, read the package as choreography:

- Can the opening image and first verb coexist?
- Can each movement be seen from the POV?
- Do spatial directions resolve to visible geometry?
- Are micro-actions physically linked or competing?
- Does contact preserve limb ownership and produce feedback?
- Does dialogue have a stable performance window or deliberate alternate route?
- Do sound, weather, and light cause or support something visible?
- Does the landing form a usable next frame?
- Is every critical fact carried by submitted media, exact submitted text, another real field, a deliberate post path, a later shot, or an explicitly accepted area of variation?

This check protects specificity without reducing every shot to a generic single action.
