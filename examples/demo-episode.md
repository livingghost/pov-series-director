# Storm Watch: Generated Canonical Worked Example
This file is assembled from the canonical artifacts under `examples/storm-watch/` by `scripts/build_demo.py`. It demonstrates the artifact set the current natural-language procedure is expected to produce; it is not a deterministic language-model transcript and it does not claim a video-generation run.
The approved production media live under `examples/storm-watch/media/` with lineage in its media log; the planning diagrams are kept separate and are never submitted.

---

<!-- Canonical artifact: examples/storm-watch/README.md -->

# Storm Watch: canonical worked example, mid-rebuild

This directory is the canonical artifact set for applying the current `SKILL.md` procedure to `source-brief.md`. On 2026-08-04 the brief was rewritten and the example's first real execution exposed three defects at once; the artifact chain is being rebuilt against real evidence, and this README states exactly how far that rebuild has progressed.

What the field studies established, with records under [`../field-study/`](../field-study/):

- submitting a schematic layout diagram as endpoint media returns the diagram style in motion, under both image parameters, against explicit exclusions (runs 1-3);
- a complete written description fixes a character's species, build, and markings within one run but does not return the same individual twice; prose fixes the category, the reference sheet fixes the individual (outcome P);
- a layout fact the text does not state is a layout fact the model chooses;
- anchoring two widely separated endpoints produced a visible switch at the contact (run 4), so endpoint pairs are designed pose-close.

## Current derivation chain

```text
source-brief.md                      current: rewritten 2026-08-04, evidence-scoped
    ↓ current Phase A procedure
phase-a-plan.md                      current: two-clip packing, media plan
media-briefs/character-reference-brief.md   current
media-briefs/clip1-start-frame-brief.md     current
media-briefs/clip1-end-frame-brief.md       current
media-briefs/clip2-end-frame-brief.md       current
planning-diagrams/                   reclassified: layout only, never submitted
    ↓ media generation                AWAITING: sheet + three boundary frames
frame-inspection.md                  awaiting media
    ↓ current Phase B procedure, once per target operation
runway-gen45-i2v/                    SUPERSEDED, awaiting rebuild
veo31-first-last/                    SUPERSEDED, awaiting rebuild
seedance20-first-last/               SUPERSEDED, awaiting rebuild on the OpenRouter surface
target-contrast.md                   SUPERSEDED, awaiting rebuild
    ↓ planned real run
Seedance 2.0 via OpenRouter          the one branch to be executed, per the field-study surface
```

`../demo-episode.md` and the validator marker set still describe the superseded chain; they are regenerated in the release step after the rebuild completes.

## Evidence state

- Story/directing artifacts: Phase A is current for the rewritten beat. The line 「大丈夫」 and the English sidecar language are proposed canon awaiting owner approval.
- Media: none approved. The character reference sheet and three boundary frames do not exist yet; the two schematic diagrams are planning-only and depict the superseded beat.
- Target facts: each superseded submission sheet retains its evidence-dated surface documentation; the OpenRouter Seedance surface additionally has same-day direct observations (request shape, $1.2096 per-run billing, 21.5 and 60.5 minute queue times).
- Generated video for this example's packages: not run. The field-study runs are controlled experiments, recorded separately, and none of their outputs enters canon.
- Output quality/adherence for the rebuilt packages: not evaluated, and not claimed.

---

<!-- Canonical artifact: examples/storm-watch/source-brief.md -->

# Source Brief Supplied to the Skill

## Series facts

- Series: `Parallel Home`
- Episode: `Storm Watch`
- Format: short serialized character-centered POV scene.
- POV belongs to the person lying in bed. No reverse or selfie view. Nothing of the POV appears beyond their hands and the near edge of the bedding.
- Visual direction: grounded clean realism, natural color, crisp practical light.
- Dialogue language: Japanese.
- Subtitles: off by default. A sidecar track is prepared because the dialogue is not in the viewer's language, and it is not burned into the picture.

## Recurring character

Iven is an adult male anthropomorphic wolf who stands upright on digitigrade legs. He is about two metres tall and heavily built, with visible shoulder and chest mass under short white fur that runs to cream at the throat. He has a long muzzle, upright ears that move independently, yellow eyes, and a full plumed tail. A narrow scar crosses the ridge above his left brow. At home he wears an open dark robe with loose sleeves over dark trousers, and goes barefoot.

He arrived with no memory of who he had been, and the POV took him in. What survived the memory loss is the posture of a guard: when he is unsettled he stations himself where he can watch the way in, and he stands rather than sits.

His separation anxiety reads as vigilance rather than clinging. Alertness appears first in the ears and shoulders, never in broad gestures.

His speech is at a single-word stage. He says one word at a time and does not build sentences. The restraint is the character, not a limitation to write around.

Recurring object relation: during night checks he carries the POV's old folded sleepwear in both hands. It holds the POV's scent, which is why he carries it and why he will not set it down while he is standing watch.

## Location

A small bedroom at night. The bed fills the lower foreground from a pillow-height POV. An open strip of floor runs beside the near mattress edge. A warm practical lamp stands on a dresser at left and is the stable light source. A rainy window sits rear-right and can give a brief cold lightning pulse. The lamp holds; the lightning does not.

## Requested episode beat

A close thunderclap wakes the POV.

Iven is already standing at the bedside, facing the window with his back to the POV, standing straight, ears turning to each roll of thunder, the folded sleepwear held in both hands. He is on watch.

Another flash outlines him. Without turning, he says one word, low.

The POV lifts a corner of the blanket and pats the mattress.

He hesitates, then comes over and sits on the near mattress edge, still facing the window and still upright, and sets the folded sleepwear beside the POV's pillow.

The episode ends on the compromise: he sits guarding, ears still toward the window, and his tail comes to rest across the POV's blanket.

The ending must provide a stable continuity frame for the next episode.

## Requested comparison

Prepare the same beat for three documented target operations:

1. Runway Gen-4.5 Image to Video from one start image.
2. Veo 3.1 generation from separate first and last frames.
3. Seedance 2.0 generation from separate first and last frames.

Do not claim any target has generated the result. Preserve dialogue and sound through a concrete additional operation or post-production path when they are not carried in the selected picture pass.

## Media initially available

No approved visual media are supplied. The Skill must first specify and create the concrete media, then inspect the actual files before completing target-specific Phase B packages.

At minimum this episode needs a character reference sheet that fixes Iven's species, build, fur, muzzle, ears, tail, scar, and home clothing, plus the concrete start and end frames for the clip being submitted.

A written description has been tested at both ends. One that named height, fur colour, and a scar, but no species, returned an unrelated animal. A complete description, submitted twice with identical text, fixed species, build, and markings within each run but did not return the same individual twice: the scar placement moved and the build shifted between runs. Prose fixes the category; the reference sheet is what fixes the individual across generations. Any frame that is submitted must also already look the way the finished shot should look, because a schematic layout diagram submitted as an endpoint returns a schematic layout diagram in motion. These results are recorded in `../field-study/2026-08-04-seedance20-openrouter/run-record.md` and `../field-study/2026-08-04-seedance20-openrouter-prose-identity/run-record.md`.

---

<!-- Canonical artifact: examples/storm-watch/phase-a-plan.md -->

# Parallel Home · Storm Watch · Phase A
Status: awaiting the character reference sheet and the three boundary frames; no final target submission exists
Continuity: story continuity taken from the supplied series brief; visual continuity unverifiable until approved media exist

This plan follows the 2026-08-04 rewrite of `source-brief.md` and carries the field-study findings recorded in `../field-study/2026-08-04-seedance20-openrouter/run-record.md` and `../field-study/2026-08-04-seedance20-openrouter-prose-identity/run-record.md`: a complete written description fixes the character's category but not the individual, a submitted frame's style is inherited literally, and a layout fact the text does not state is a layout fact the model chooses.

## Episode purpose

- timeline position: a nighttime beat within the recurring home setting, after Iven's arrival and adoption are established;
- segment purpose: turn storm alarm into a negotiated compromise between his guard posture and the POV's invitation;
- visible cast: Iven and the POV's hands plus near bedding edge, nothing more of the POV;
- reused or new location: recurring small bedroom, unchanged geometry;
- dramatic/informational change: Iven moves from standing watch, back to the POV, to sitting on the bed while still facing the window, tail across the blanket;
- one-line retell: thunder wakes the POV; Iven is already on watch; one low word; the POV pats the mattress; he hesitates, then sits guarding, and his tail settles on the blanket;
- final image needed for the next episode: Iven seated upright on the left mattress edge facing the rain window, the folded sleepwear beside the POV's pillow, his tail resting across the blanket, warm lamp stable.

## Clip packing

The beat contains two causal spines, not one: the invitation (his watch is interrupted by the POV's request) and the compromise (he yields distance without yielding vigilance). They are packed as two clips.

- Clip 1, the invitation: thunderclap, his ears track the roll, one low word without turning, the POV lifts the blanket corner and pats the mattress, his head turns a few degrees and one ear swings back toward the bed. Start and end frames are deliberately close in pose: the field study's run 4 showed that widely separated endpoint anchors produced a visible switch at the contact, so the clip whose endpoints we anchor is the one with small pose distance.
- Clip 2, the compromise: the hesitation resolves; he crosses the strip, turns, sits on the left mattress edge still facing the window, sets the sleepwear beside the pillow, and his tail sweeps in and settles across the blanket. Clip 2 contains the contact events and the largest pose change, so its opening is not finalized from a planned image: it starts from Clip 1's accepted terminal frame, extracted and inspected after a real run.

The three-target comparison requested by the brief is prepared for Clip 1. Clip 2 keeps full provisional direction and finalizes sequentially.

## Story and retention design

- opening condition or hook: a close thunderclap wakes the POV into an already-guarded room; the hook is that the guardian is already there, standing between the bed and the storm;
- setup: Iven at the bedside, back to the POV, sleepwear held in both hands, ears turning with each roll;
- build: another flash outlines him; without turning he says one word, low;
- turn/critical change: the POV lifts a corner of the blanket and pats the mattress, converting his watch into a choice;
- payoff/reaction (Clip 2): he comes over and sits, still upright, still facing the window;
- settle/bridge: the sleepwear is set beside the pillow and the tail comes to rest across the blanket, the compromise image that ends the episode;
- emotional or informational peak: guarding and belonging resolved in one seated posture;
- unnecessary beats removed or moved: no waking shot of eyes opening, because the literal start image already shows the room; the spoken word is carried by audio, not by on-screen mouth performance, because his back stays to the camera.

## POV and physical design

- camera belongs to: the person lying in bed; pillow-height, landscape;
- opening body position: lying supported, level view across the bed toward the strip and window;
- gaze trigger and path: the thunderclap produces one small camera-body jolt and recovery; no orbit, no reverse;
- POV as actor: in Clip 1 the POV's own hand lifts the near blanket corner and pats the mattress twice; hands and near bedding are the only visible POV anatomy;
- dominant visible action: Clip 1, ear and small head rotation on a standing figure; Clip 2, the walk-turn-sit with sleepwear placement and tail settle;
- body mechanics and material response: digitigrade steps on the wooden strip; hip/knee flexion into the sit; local mattress dip; the tail's weight visibly presses the blanket where it rests;
- contact/occlusion risks: the sleepwear is partially occluded by his body while his back is to the camera, so both hands' grip must read at his sides; during Clip 2's sit, the placement beside the pillow happens close to the lens and must not collide with the POV's visible hand;
- landing body/camera state: seated upright on the left edge, face toward the window, tail across the blanket, camera level at pillow height.

## Performance and dialogue

- character objective: keep the way in guarded while accepting the POV's invitation;
- visible behavior before the change: standing straight, ears turning independently with the thunder, grip on the sleepwear steady; vigilance, not fear;
- visible behavior after the change: hesitation reads in a held beat and a small head turn before the feet move; after sitting, shoulders stay upright and ears stay mostly on the window; comfort is granted through the tail, not the posture;
- signature or species/anatomy-specific detail: ears move independently, one swinging back toward the bed while the other holds on the window; the plumed tail is the emotional release channel;
- line, speaker, language, speech stage, voice direction: Iven speaks once, one word, Japanese, low, almost under the thunder. PROPOSED CANON, awaiting owner approval: the word is 「大丈夫」. His speech stays at the single-word stage; no sentence is written around it;
- subtitle route: off by default; a sidecar track is prepared because the dialogue is not in the viewer's language. PROPOSED, awaiting owner approval: the sidecar language is English. Nothing is burned into the picture;
- stable performance window or alternate dialogue route: his back is to the camera when he speaks, so no on-screen lip performance exists to conflict with; the exact word is laid in post over the standing hold in Clip 1.

## Sound, atmosphere, and music

- ambient bed: steady rain throughout both clips;
- action trigger sound: one close thunderclap at the top of Clip 1, aligned with the POV jolt;
- subordinate material sounds: blanket lift and two soft mattress pats (Clip 1); footfalls on wood, mattress compression, cloth settle, and the faint slide of the tail across the blanket (Clip 2);
- weather/light source and what each changes: the warm dresser lamp at left is the stable source and holds; the rear-right window gives brief cold lightning pulses that outline Iven's back and do not persist;
- music cue or no music: none; thunder, rain, and the single word carry the scene;
- bridge/tail needed for continuity: rain continues under the final compromise hold and into the next episode's opening.

## Intended operation

- actual operation sought, per the brief's comparison: Clip 1 prepared three ways: Runway Gen-4.5 Image to Video from the start frame alone; Veo 3.1 first/last-frame generation; Seedance 2.0 first/last-frame generation on the OpenRouter surface, whose request shape, costs, and queue behavior were directly observed on 2026-08-04;
- hardest continuity evidence it must carry: Iven's individual identity (sheet-derived, not prose-derived), the room's stated geometry including the bed's side, two-handed sleepwear ownership, ear performance, and a terminal frame from which Clip 2 can start;
- target controls/evidence already known: recorded per branch in each `submission-sheet.md` with source and check date;
- unresolved surface facts: real prompt adherence, endpoint fidelity, and identity retention for the rebuilt media remain unobserved until the planned real run of the Seedance branch;
- alternate route if a combination is unavailable: split further, carry the invitation in audio over a longer hold, or finish the compromise in an edit/extension pass.

## Existing approved media

| Asset | What is visibly supported | Intended real use | What it cannot establish |
|---|---|---|---|
| none | no approved visual asset exists for the rewritten character | none | identity, design integration, and all boundary geometry |
| `planning-diagrams/layout-standing.png`, `layout-seated.png` | blocking geometry of the superseded beat | planning reference only; never submitted | style, identity, or any submittable content; submitting a diagram returns a diagram in motion (field study, runs 1-3) |

## Media to create or extract

| Deliverable | Exact visible content | Why required | Source/derivation | Acceptance check |
|---|---|---|---|---|
| character reference sheet | Iven full-body front, side, and back, plus head detail: two-metre heavy build, white fur to cream throat, long muzzle, independent upright ears, yellow eyes, narrow scar above his left brow, full plumed tail, open dark robe with loose sleeves, dark trousers, barefoot digitigrade legs, drawn as one integrated anthropomorphic body | the field study's outcome P: prose fixed the category, not the individual; and run A produced a wolf head joined to a human body, so the sheet must fix the integration | `media-briefs/character-reference-brief.md` | one consistent individual across all views; neck/shoulder integration reads as one body; scar side explicit |
| Clip 1 start frame | pillow-height POV; Iven standing on the left floor strip, back three-quarter to camera, facing the rear-right rain window; sleepwear in both hands at waist; lamp left; POV hands at the near bedding only | literal Runway start, Veo start, Seedance `first_frame` | `media-briefs/clip1-start-frame-brief.md`, derived from the approved sheet | production-look realism; bed side and strip geometry match this plan; identity matches the sheet |
| Clip 1 end frame | same stance and room; the near blanket corner lifted with the POV's hand resting on the mattress; Iven's head turned a few degrees toward the bed, one ear swung back | Veo end, Seedance `last_frame`; small pose distance from the start by design | `media-briefs/clip1-end-frame-brief.md`, derived from the sheet and the start frame | differences from the start are exactly the ear/head/blanket changes and nothing else |
| Clip 2 end frame | Iven seated upright on the left mattress edge facing the window; sleepwear folded beside the POV's pillow; tail across the blanket; same lamp and rain | the episode's continuity landing; Veo/Seedance end for Clip 2 once its start exists | `media-briefs/clip2-end-frame-brief.md`, derived from the sheet | contact, prop placement, and tail rest all read; camera relation unchanged |
| frame inspection | direct observations of the actual generated files | required before any final choreography or target mapping | inspect the created files; record in `frame-inspection.md` | observations separate visible facts from uncertainty |
| Clip 2 start frame | not created in advance | Clip 2 starts from Clip 1's accepted terminal frame | extracted after the Clip 1 run is accepted | real geometry, not planned geometry |

## Shot proposition, Clip 1

Opening image: already-awake pillow-height POV; Iven stands on the left floor strip with his back three-quarter to the camera, facing the rain window, sleepwear in both hands; rain moves at the window.

Dominant visible change: his ears track a thunder roll; a flash outlines him; the POV's hand lifts the near blanket corner and pats the mattress twice; his head turns a few degrees toward the bed and one ear swings back.

Cause: the storm holds his watch; the POV's invitation interrupts it.

Physical path: ear rotation, small head turn, no step, no reposition; the POV hand's blanket lift and two pats are the largest displacements in the frame.

Performance change: unbroken vigilance acquires a single point of attention toward the bed.

Landing image: same stance, head slightly turned, one ear back, blanket corner lifted with the POV's hand at rest.

Required dialogue/sound: one low Japanese word (proposed 「大丈夫」) laid in post over the standing hold; steady rain; one close thunderclap; blanket and pat sounds.

Exact requirements: sheet-matched identity, stated room geometry, two-handed sleepwear grip, ears-before-head order, POV hand ownership of the blanket action, no turn of the torso.

Accepted variation: lightning contour, exact ear timing, fold shapes, rain texture.

## Shot proposition, Clip 2 (provisional; opening not finalized)

Opening image: Clip 1's accepted terminal frame, inspected after the run.

Dominant visible change: the hesitation resolves; he crosses the strip, turns, and sits on the left mattress edge still facing the window; the sleepwear is set beside the pillow; the tail sweeps in and settles across the blanket.

Cause: the invitation is accepted on his terms.

Physical path: two digitigrade steps, quarter turn, hip/knee flexion to the edge, local mattress dip, sleepwear placed with both hands beside the pillow, tail settle last.

Performance change: guarding continues seated; release is expressed by the tail alone.

Landing image: the episode's compromise frame, matching `media-briefs/clip2-end-frame-brief.md`.

Required dialogue/sound: no further dialogue; rain continues; footfalls, mattress, cloth, tail slide.

Exact requirements: same individual as Clip 1's output, seat on the mattress edge and not in front of it, sleepwear ends beside the pillow and not in his hands, tail contact visible on the blanket, no cut.

Accepted variation: step count within two-to-three, exact tail curve, fold shapes.

The air-chair failure in the prose-identity study's run A is the named risk for this clip: the seat must be anchored by inspected endpoint media, not by prose alone.

## Provisional creative-requirement transfer

| Requirement | Intended carrier | Concrete implementation | Fallback if unavailable |
|---|---|---|---|
| individual identity and design integration | approved character sheet, then sheet-derived boundary frames | create sheet first; derive every frame from it | do not proceed on prose alone; outcome P is the recorded reason |
| room geometry including bed side | boundary frames, restated in every primary prompt | left strip, lamp left, window rear-right written explicitly | if a frame carrier is absent, the text states every load-bearing layout fact |
| invitation beat (ears, word, blanket, pats) | Clip 1 prompt plus post audio | ear/head choreography in text; word in post over the facing-away hold | longer hold with audio-only invitation |
| compromise beat (walk, sit, placement, tail) | Clip 2 prompt anchored by real terminal frame and created end frame | sequential finalization | split placement into an extension pass |
| one low word, speaker, language | post-production in all branches | approved voice over the hold; back-to-camera removes lip-sync risk | none needed beyond timing choice |
| rain, thunder, contact sounds | post stems in all branches; Seedance may additionally attempt ambience in-pass | stems remain the authority; generated audio is a candidate | mute candidate, keep stems |
| sidecar subtitles | delivery metadata, outside every visual prompt | one English sidecar track, off by default | none; never burned in |
| next-episode continuity | Clip 2's accepted final composite | extract after picture/audio finishing | corrective derivative with lineage |

Evidence statement: awaiting media. The character reference sheet and the three boundary frames do not yet exist, so no frame has been inspected, no final choreography is locked, and no exact target text has been written. The three target branches retain their evidence-dated surface facts and are otherwise superseded until rebuilt on the new media.

STOP CONDITIONS
- Do not claim an inspected sheet or frame before the actual media exists.
- Do not finalize Clip 2's opening before Clip 1's accepted terminal frame is extracted and inspected.
- Do not promote the proposed line or subtitle language to canon without owner approval.
- Return the media briefs and the missing-evidence list.

---

<!-- Canonical artifact: examples/storm-watch/media-briefs/character-reference-brief.md -->

# Character Reference Sheet Brief: Iven

Create the approved identity asset for the recurring lead. This sheet is the derivation source for every boundary frame; no identity-bearing generation proceeds from prose alone.

Why this asset exists: the 2026-08-04 field study (`../../field-study/2026-08-04-seedance20-openrouter-prose-identity/run-record.md`) showed that a complete written description fixes species, build, and markings within one run but does not return the same individual twice, and that a text-only run rendered a literal wolf's head joined to a fur-covered human body. The sheet fixes the individual and the integration.

## Format

- one landscape sheet or a small set of images, whichever the image tool handles better;
- required views: full-body front, full-body side, full-body back, and a head close-up;
- style anchor: grounded clean realism, natural color, crisp practical light; the same finish the episode frames must have, because a submitted frame's style is inherited literally;
- neutral, even lighting; no dramatic color cast that would contaminate identity reading.

## Identity facts the sheet must fix

- adult male anthropomorphic wolf standing upright on digitigrade legs, about two metres tall;
- heavily built: visible shoulder and chest mass; not slender;
- short white fur running to cream at the throat;
- long muzzle; upright ears drawn so they visibly can move independently; yellow eyes;
- a narrow scar crossing the ridge above his left brow. The head close-up must make the side unambiguous: his left, which appears on the viewer's right when he faces the camera;
- full plumed tail, visible in side and back views;
- home clothing: open dark robe with loose sleeves over dark trousers; barefoot, digitigrade feet visible.

## Integration requirement

The head, neck, shoulders, and body must read as one continuous anthropomorphic anatomy. Reject any view in which the result reads as a realistic wolf's head attached to a human body: fur flow, neck thickness, and shoulder transition must belong to the same creature.

## Acceptance check

- all views show the same individual: same build class, same fur pattern, same face, same clothing;
- the scar is present in front and head views, on his left;
- the tail, ears, muzzle, and feet match across views;
- the finish is photographic-realistic, not schematic, not illustration-flat.

## Sheet role

The sheet is a C asset for the registry. It is never submitted to a video surface in this episode's packages; its job is to be the visual authority from which the boundary frames are generated and against which every returned variant's identity is judged.

---

<!-- Canonical artifact: examples/storm-watch/media-briefs/clip1-start-frame-brief.md -->

# Clip 1 Start Frame Brief

Create the literal opening frame for the `Storm Watch` invitation clip. Derive Iven from the approved character reference sheet; do not restate identity from prose alone.

## Camera and POV

- first-person camera from a person lying in bed at pillow height;
- landscape 16:9, 1280×720 or the target's documented equivalent;
- the bed and blanket fill the lower-right foreground; only the POV's hands and the near bedding edge may appear, at the lower frame edge;
- no reverse, selfie, mirror, or visible camera wearer.

## Space

State every load-bearing layout fact; an unstated fact is a fact the generator chooses (field-study run A put the bed on the wrong side for exactly this reason):

- small bedroom at night;
- bed lower-right foreground from the POV;
- open strip of wooden floor along the left mattress edge;
- dresser with the warm practical lamp at frame left; the lamp is the stable light source;
- rainy four-pane window rear-right; one cold lightning shape may be present but must not overpower the lamp.

## Visible character and prop

- Iven, matching the approved sheet: two-metre heavy build, white fur, open dark robe with loose sleeves, dark trousers, barefoot digitigrade legs, full plumed tail;
- standing on the floor strip beside the left mattress edge, fully on the floor, not on the mattress;
- back three-quarter to the camera, face toward the rear-right window; the muzzle's profile edge may show, the face largely does not;
- both ears upright, turned toward the window;
- the POV's old folded sleepwear held in both hands at waist height in front of him; his body partially occludes it, so both gripping hands must read at his sides;
- tail relaxed behind him, visible against the floor strip.

## Light and atmosphere

- stable warm lamp light from the left as the dominant source;
- cool rain and window light rear-right; lightning, if present, outlines his back and shoulders;
- clean readable interior, photographic realism; not schematic, not illustration.

## Frame role

The frame is the literal Runway start image, Veo start image, and Seedance `first_frame`. It establishes the room's stated geometry, the sheet-matched identity from behind, the two-handed sleepwear ownership, the watch posture, and the POV relation. Its finish is inherited by the output, so it must already look the way the finished shot should look.

---

<!-- Canonical artifact: examples/storm-watch/media-briefs/clip1-end-frame-brief.md -->

# Clip 1 End Frame Brief

Create the matched endpoint for the invitation clip. Start from the approved Clip 1 start frame and change only what the beat changes; the pose distance between the two frames is deliberately small, because the field study's run 4 showed a visible switch when widely separated endpoints were both anchored.

## Preserve from the start frame

- camera height, level, and framing;
- room geometry: bed lower-right, floor strip left, lamp left, rainy window rear-right;
- Iven's standing position on the strip and his overall stance;
- both hands holding the folded sleepwear at waist height;
- lamp-dominant lighting.

## Change exactly this

- the near blanket corner is lifted, and the POV's visible hand rests on the mattress where it has just patted;
- Iven's head is turned a few degrees toward the bed, not his torso;
- one ear is swung back toward the bed while the other stays on the window;
- the tail has lifted slightly, the smallest readable sign of attention.

## Light and atmosphere

- unchanged from the start frame; no new lightning is required in this frame.

## Frame role

The frame is the Veo end image and Seedance `last_frame` for Clip 1, and the review target for the Runway branch. The differences from the start frame are exactly the ear, head, tail, blanket, and POV-hand changes and nothing else; any other difference between the two files is an error in the media, not direction for the generator.

---

<!-- Canonical artifact: examples/storm-watch/media-briefs/clip2-end-frame-brief.md -->

# Clip 2 End Frame Brief

Create the episode's compromise landing: the continuity frame the next episode opens from. Derive Iven from the approved character reference sheet. Clip 2's start frame is not created in advance; it will be Clip 1's accepted terminal frame.

## Camera and POV

- unchanged pillow-height first-person camera, landscape, level;
- the POV's hand may remain visible at the near bedding edge; nothing more of the POV.

## Space

- same room, same stated geometry: bed lower-right, floor strip left, dresser lamp left, rainy window rear-right;
- no furniture relocation, no new objects beyond the placed sleepwear.

## Visible character, prop, and contact

- Iven seated upright on the left mattress edge, weight unambiguously on the mattress: a local dip under him and one bedding fold pulled toward the contact point. He is not floating in front of the edge and not standing on the bed. The air-chair result in the field study's run A is the named failure this frame exists to prevent;
- his torso and face remain toward the rear-right window; the camera sees his back and right side; ears toward the window;
- feet on the floor below the edge, digitigrade profile readable;
- the folded sleepwear lies beside the POV's pillow, lower-left near the camera, clearly placed and no longer in his hands;
- both his hands rest on his own knees or thighs;
- his full plumed tail crosses the blanket over the POV's covered legs and rests there, its weight pressing the fabric where it lies.

## Light and atmosphere

- warm lamp stable from the left; rain continues at the window; no lightning required;
- photographic realism matching the sheet and the Clip 1 frames.

## Frame role

The frame supplies the Clip 2 endpoint for a first-and-last-frame operation and the episode's planned continuity landing: seated guard, sleepwear beside the pillow, tail on the blanket. It is a planned image, not a generated terminal frame; after a real run, the actual accepted final composite supersedes it for continuation.

---

<!-- Canonical artifact: examples/storm-watch/planning-diagrams/README.md -->

# Planning Diagrams: layout only, never submit

`layout-standing.png` and `layout-seated.png` are 1280×720 schematic layout diagrams of the superseded pre-2026-08-04 beat. They exist to make blocking geometry discussable: camera height, the floor strip, the lamp and window sides, the path to the mattress.

They are planning-tier artifacts in the sense of the Skill's first invariant: a planning image that is not submitted remains useful production material, but it does not control the generator.

Until 2026-08-04 these same files sat in the target branches' `inputs/` directories as submittable endpoint media. The first real execution showed why that was wrong: submitted as endpoints on Seedance 2.0 via OpenRouter, they returned the diagram style in motion, in all three attempts, under both image parameters, against five explicit style exclusions. The full record is `../../field-study/2026-08-04-seedance20-openrouter/run-record.md`, runs 1-3.

Rules for this directory:

- nothing in it is ever placed in a generation control;
- submitted boundary frames are created separately, look the way the finished shot should look, and derive identity from the approved character reference sheet;
- new-beat diagrams may be added here when they help planning, under the same rules.

---

<!-- Canonical artifact: examples/storm-watch/media/media-log.md -->

# Approved Media Log

Generator: `google/gemini-3-pro-image` via OpenRouter `POST /api/v1/chat/completions` with image output, 2026-08-04. Every generation's exact prompt is preserved under `prompts/`; rejected iterations are preserved outside the repository under `production-media/storm-watch/`.

Approval state: the owner delegated intermediate approvals on 2026-08-04 ("proceed through video generation without approval"), so acceptance below is the assistant's inspection against the media briefs, recorded as provisional until the owner's final review. The sleepwear colour, dark teal, is a design decision carried over from the pre-rewrite prop colour and shares that provisional status.

## Iterations

| # | File | Derived from | Generation id | Cost | Verdict |
|---|---|---|---|---|---|
| 1 | sheet-v1 | text only | `gen-1785848525-qf5EpEe99LrQ2oyzb7sw` | $0.1385 | rejected: plantigrade legs; scar side inconsistent between views; build too light; robe brown rather than dark |
| 2 | sheet-v2 | edit of v1 | `gen-1785848643-qf4I6H6kKIaM92aLoHu9` | $0.1415 | accepted → `character-sheet.png` |
| 3 | clip1-start-v1 | character sheet | `gen-1785848751-PgJrNlAVQHr3DgTFn1bT` | $0.1410 | rejected: sleepwear unfolded and dangling from one hand |
| 4 | clip1-start-v2 | edit of v1 | `gen-1785848823-rsjZczAGC0DwkUhRYrBa` | $0.1368 | accepted → `clip1-start.jpg` |
| 5 | clip1-end-v1 | edit of accepted start | `gen-1785848920-sCTvIaiPVRq8KpgcCJid` | $0.1378 | accepted → `clip1-end.jpg` |
| 6 | clip2-end-v1 | accepted start + sheet | `gen-1785849014-Hh1B5ZzxD1yGhBdbyBCZ` | $0.1422 | accepted, later superseded: generated before the terminal frame existed, its free framing caused the take 1 stretch and the take 2 join-visible zoom |
| 7 | clip2-end-v2 | edit of the real terminal frame | `gen-1785857331-2GBo8VxkyOyuBOAZl9n9` | $0.1378 | rejected: the edit removed his robe and hunched the pose |
| 8 | clip2-end-v3 | edit of the real terminal frame, clothing and posture constrained | `gen-1785857402-pX6yGj4tHAWTyzvl4o4P` | $0.1383 | accepted → `clip2-end.png` |

Total image cost: $0.8378 of the $5.00 cap. Costs are the `usage.cost` values returned per generation; unlike the video surface, the listed accounting matched the returned charge mechanism directly.

## Accepted files

| File | Format | Pixels | sha256 (first 16) | Bytes |
|---|---|---|---|---|
| `character-sheet.png` | png | 1376×768 | `be0db21958b36c3b` | 1,411,320 |
| `clip1-start.jpg` | jpeg | 1376×768 | `949cdc8b6acff07d` | 653,709 |
| `clip1-end.jpg` | jpeg | 1376×768 | `3d21c3b0e335a955` | 673,637 |
| `clip2-end.png` | png | 1280×720 | `7b90d46f3552e057` | 1,127,180 |
| `clip2-start.png` | png | 1280×720 | `7fb8dd33518ba731` | 931,638 |

`clip2-end.png` is the v3 derivation: an edit of the real terminal frame `clip2-start.png`, so camera and field of view are inherited rather than re-invented, conformed from 1365×768 by direct Lanczos scale to 1280×720 (aspect difference 0.024 percent, no crop, no zoom introduced). Two standing rules came out of the Clip 2 takes: every boundary image is conformed to the delivery resolution before submission, and a continuation clip's end anchor is derived from the extracted terminal frame itself, not from pre-render planning media. Earlier `clip2-end.png` states (`b23955c4ec3a8284` original, `376d3fa0aae506c0` crop-conformed) are preserved in git history.

`clip2-start.png` is not a generation: it is the terminal frame of the accepted Clip 1 take 1 (job `b00ddyOO3QfCL6UGKFTK`), extracted locally with ffmpeg 9.0 at 0.1 s before end of stream, after the operator accepted the take. It is the real geometry Clip 2 starts from.

| `episode-continuity-frame.png` | png | 1280×720 | `7a73f726f2af4b16` | see file |

`episode-continuity-frame.png` is the final frame of the finished episode master (`production-media/storm-watch-episode/episode-master.mp4`), extracted after the join, flash masking, and audio assembly were complete. It is the continuity landing the next episode opens from: Iven seated guard on the left mattress edge facing the window, the sleepwear beside the pillow, his tail across the blanket.

The generator returns 1376×768 rather than exactly 1280×720; the aspect deviation from 16:9 is under one percent. Submission mime types must match the container formats above, not the file extensions' historical assumptions.

---

<!-- Canonical artifact: examples/storm-watch/frame-inspection.md -->

# Boundary Frame Inspection: Storm Watch

Status: the character reference sheet and the three planned boundary frames exist and were directly inspected on 2026-08-04. Files, hashes, and generation lineage are in `media/media-log.md`. Clip 2's start frame does not exist by design; it will be Clip 1's accepted terminal frame.

The previous version of this file inspected two schematic layout diagrams that then sat in the target branches as submittable media; those are reclassified under `planning-diagrams/` and are never submitted (`../field-study/2026-08-04-seedance20-openrouter/run-record.md`, runs 1-3).

## Character reference sheet (`media/character-sheet.png`)

### Direct visual observations

- 1376×768 landscape; full-body front, side, and back views plus a head close-up inset; plain light-grey background; photographic finish;
- integration: fur flows continuously from muzzle through the thick neck into the chest; the head, shoulders, and torso read as one anatomy, not a wolf head joined to a human body;
- digitigrade legs in all full-body views; the side view shows the raised hock and ball-of-foot stance explicitly;
- one narrow scar crossing the ridge above his left brow, appearing on the viewer's right in the front view and in the inset; no scar over the other eye;
- short white fur running to cream at the throat; yellow eyes in the inset; long muzzle; upright ears;
- open charcoal robe with loose three-quarter sleeves over black cuffed trousers; barefoot paw feet; full plumed tail visible in the side and back views;
- the same individual, proportions, fur pattern, and clothing across all views.

### Uncertainty and limitation

- a faint warm patch on the chest fur in the front view is either shading or skin showing through; recorded as accepted variation, not a marking;
- the scar cannot be resolved in the small side-view head; the inset is the authority for the scar;
- the sheet proves the design, not any target's ability to animate it.

## Clip 1 start frame (`media/clip1-start.jpg`)

### Direct visual observations

- room as stated in `phase-a-plan.md`: bed and blanket fill the lower-right foreground; open wooden floor strip along the left mattress edge; dresser with the lit warm lamp at frame left as the dominant source; rainy four-pane window rear-right with visible rain streaks;
- Iven stands on the floor strip fully on the floor, back three-quarter to the camera, face turned toward the window with only the muzzle's profile edge visible; both ears upright and aimed windowward;
- the folded dark teal sleepwear is a flat neat bundle held horizontally at waist height in front of his body; the near hand's grip is directly visible;
- charcoal robe, black cuffed trousers, digitigrade paw feet, relaxed plumed tail, all matching the sheet;
- the viewer's hand rests on the near bedding at the lower frame edge; nothing else of the viewer is visible.

### Uncertainty and limitation

- the far hand's grip on the bundle is implied by posture and occluded by his body; the primary prompt must still state the two-handed carry;
- some wrist is visible with the POV hand; recorded, within the hands-and-bedding limit;
- the camera reads as a propped pillow-height view; exact lens height is not measurable.

## Clip 1 end frame (`media/clip1-end.jpg`)

### Direct visual observations

Compared side by side with the start frame, the differences are:

- the blanket's near corner is folded back about a hand's width, exposing pale sheet, and the viewer's hand now rests flat on that exposed area;
- his head is rotated a few degrees toward the bed, showing more muzzle profile; torso, shoulders, and feet unchanged;
- the near ear is swiveled back toward the bed; the far ear remains toward the window;
- the plumed tail is lifted, no longer fully relaxed.

Room, lighting, robe, trousers, stance, and the folded sleepwear carry are unchanged from the start frame.

### Uncertainty and limitation

- the far ear is partially occluded, so its exact aim is inferred;
- the pose distance between the two frames is deliberately small; nothing here proves the target will keep the intermediate motion continuous.

## Clip 2 end frame (`media/clip2-end.png`)

Re-derived after the first two Clip 2 takes: an anchor generated before the terminal frame existed could not agree with it in framing, and the mismatch surfaced as a horizontal stretch in take 1 and a join-visible zoom offset in take 2. The current anchor is an edit of the real terminal frame `media/clip2-start.png`, so camera and field of view are inherited; only the staged change is new. The first re-derivation attempt removed his robe and hunched the pose and was rejected; the accepted version keeps the input clothing.

### Direct visual observations

- Iven sits upright on the left mattress edge facing the rainy window, robed back and right side to the camera, charcoal robe and black cuffed trousers as in the terminal frame;
- both feet on the floor below the edge, digitigrade, heels raised; the near hand rests on his thigh;
- the folded dark teal sleepwear lies flat on the bedding beside the viewer's pillow, out of his hands;
- his plumed tail sweeps to his side and rests across the bedding over the viewer's covered legs; the bedding compresses under his seat;
- dresser, lamp, window, rain, the viewer's hand, and the framing all match the terminal frame; no lightning.

### Uncertainty and limitation

- conformed from 1365×768 by direct scale to 1280×720, aspect difference 0.024 percent, no crop, so no zoom is introduced;
- the far hand and far leg are occluded;
- this is a planned endpoint; after a real Clip 2 run, the accepted rendered frame supersedes it for continuation.

## Clip 2 start frame (`media/clip2-start.png`)

Extracted from the accepted Clip 1 take 1, not created in advance. 1280×720, the delivery resolution.

### Direct visual observations

- Iven stands at the bedside on the floor strip, back three-quarter to the camera, head turned a few degrees toward the bed with the muzzle profile clearly visible; ears up;
- the folded dark teal sleepwear remains a flat bundle supported in both hands at waist height;
- the tail is lifted in a raised curve, not relaxed;
- the POV hand rests flat on the bed surface at the lower edge; the blanket near it is pushed aside toward the right rather than folded back in the neat corner the planned end frame showed;
- dresser, lamp, window, rain, and the warm-dominant lighting all match the submitted frames.

### Uncertainty and limitation

- the blanket geometry deviates mildly from the planned end anchor; Clip 2's choreography starts from this real geometry, not from the planned frame;
- the head angle is slightly more bedward than the planned end frame; recorded, accepted;
- single extracted frame; motion into and out of this pose is judged from the video, not from this file.

## Consequence for target packages

- Clip 1 can be packaged for all three targets: Runway from the start frame alone; Veo and Seedance from the matched start and end frames. Identity travels in the media; the prompts remain responsible for the causal order, the POV hand action, the ear performance, sound, and exclusions.
- The submitted files are 1376×768 jpeg/png as recorded in `media/media-log.md`; request mime types must match the actual container formats.
- Clip 2 remains provisional until the Clip 1 run returns an accepted terminal frame.

---

<!-- Canonical artifact: examples/storm-watch/target-contrast.md -->

> **SUPERSEDED (2026-08-04).** This comparison describes the pre-rewrite beat and its schematic media. It will be rebuilt for Clip 1 of the rewritten beat, with the Seedance branch on the OpenRouter surface. The comparison logic it demonstrates remains the intended shape. See `phase-a-plan.md`.

# Same Beat, Three Complete Phase B Outputs

## Observable submission difference

The Runway branch submits **one start image** and asks text plus review/fallback to carry the landing. The Veo branch submits **two endpoint images**, a Start and an End, and asks the text to carry the physically plausible path between them. The Seedance branch submits the same two endpoint images but reaches them by a different route: the files travel as URLs inside one `content` array under `first_frame` and `last_frame` roles, and the same pass is also asked to produce the storm audio. These are observable differences in files, controls, and routed requirements, not abstract mode labels.

| Concrete consequence | Runway Gen-4.5 Image to Video | Veo 3.1 first/last frame | Seedance 2.0 first/last frame |
|---|---|---|---|
| submitted visual files | one complete opening PNG | matched start and end PNGs | the same matched start and end PNGs |
| how media reaches the target | uploaded in the web workflow | request keys `instances[0].image` and `instances[0].lastFrame` | `content[]` entries of type `image_url` carrying public URLs, with `role` values `first_frame` and `last_frame` |
| endpoint evidence | requested in prompt and judged after generation | planned endpoint supplied in an End/`lastFrame` control, then still judged after generation | planned endpoint supplied in the `last_frame` role, then still judged after generation |
| primary text job | direct the entire stand-to-sit motion and landing from one opening image | direct the causal, physically plausible path between two supplied states | direct that same path, and additionally carry the requested sound and every exclusion |
| separate exclusion field | none assumed for the web package | documented REST `negativePrompt` parameter used by the request template | none documented, so exclusions are written into the primary text as one negation per artifact |
| rain, thunder, contact sound | routed to post-production stems | routed to post-production stems | requested in the picture pass through `generate_audio`, with the post stems kept as the fallback |
| exact dialogue | preserved in post-production plan | preserved in post-production plan | preserved in post-production plan; the prompt additionally excludes speech so generated audio cannot collide with the approved voice |
| continuation evidence | actual accepted final composite frame | actual accepted final composite frame, not automatically the supplied End image | actual accepted final composite frame; the returned `last_frame_url` is a candidate only |

## What the third branch shows that two did not

Veo and Seedance perform the same operation on the same two files, so a role label alone would make them look interchangeable. They are not. One names the endpoints in separate request keys; the other names them by a `role` string inside a shared array and requires the files to be publicly reachable first. One offers a documented exclusion field; the other has none, which moves those requirements into the primary text and changes what that text has to do. One leaves the storm to post; the other can attempt it in the pass, which changes the requirement-transfer table rather than the story.

The exact line “Safe.”, rain, thunder, mattress response, cloth settling, and continuity landing remain present in all three full director packages. Target adaptation changes their carrier; it does not delete them.

Evidence state: all three packages are documentation-grounded and not run.

---

<!-- Canonical artifact: examples/storm-watch/runway-gen45-i2v/director-package.md -->

> **SUPERSEDED (2026-08-04).** This file describes the pre-rewrite beat (folded teal shirt, the English line "Safe.", a single stand-to-sit clip) and schematic input media since reclassified under `../planning-diagrams/`. The evidence-dated target-surface facts remain valid reference; everything beat-specific awaits the rebuild against the rewritten `source-brief.md` (Clip 1 of two), which starts only after the character sheet and boundary frames exist and are inspected. See `../phase-a-plan.md`.

# Parallel Home · Storm Watch · Clip 1 · Director Package
Status: prepared for Runway Gen-4.5 Image to Video; not submitted

## Story and continuity

- episode purpose: convert the POV's nighttime alarm into Iven's quiet bedside reassurance;
- clip function: one continuous approach-and-sit action followed by a stable performance window;
- previous accepted endpoint: none; this is a fresh clip using a newly created literal start image;
- intended visible/audible change: standing vigilance becomes seated reassurance while the shirt remains in both hands;
- next bridge/landing: finished composite ends on Iven seated upright at the left mattress edge, gaze to POV, rain continuing.

## Inspected evidence

| Media | Submitted/planning/source | Direct observations | Uncertainty |
|---|---|---|---|
| `inputs/opening-frame.png` | submitted start image | pillow-height schematic POV; guardian on floor beside left mattress edge; both hands support folded shirt; lamp left; rainy window rear-right; feet and path are visible | later motion, seated pose, realistic identity, fabric, contact, and target adherence are untested |
| planned seated teaching frame in the Veo branch | planning only for this Runway operation | shows the intended seated relation and local mattress dip | it is not submitted to Runway and therefore does not directly control this operation |

## Shot proposition

Opening image: already-awake first-person bed view; guardian stands beside the left mattress edge with the folded shirt in both hands.

Dominant visible change: thunder produces a small camera jolt; the guardian reacts ears-first, steps once, and lowers to sit.

Cause: the close thunderclap startles the POV and triggers the guardian's protective move closer.

Ordered physical path: ears turn, head follows, one measured step, hips/knees flex, body reaches mattress, mattress compresses, torso settles, sleeves and shirt settle last, gaze returns.

Performance change: high-shouldered alertness softens after contact into restrained reassurance.

Landing image: seated upright at the left edge, shirt across both forearms, camera level at pillow height, stable facial hold.

Dialogue/sound: exact line “Safe.”, rain, thunder, and contact sounds are completed through `post-production.md` after a usable picture variant exists.

Must be exact: first-person relation, same guardian/clothing, shirt owned and supported by both hands, ears-before-head order, readable stand-to-sit mechanics, bed response, stable landing.

May vary: exact step length, cloth folds, lightning contour, and minor timing differences that preserve the action.

## Beat and causal spine

1. Rain and the bedside composition hold long enough to read.
2. A close thunderclap causes one small camera-body jolt.
3. The guardian's ears turn toward the rear-right window before his head.
4. He keeps the shirt supported in both hands, takes one measured step, bends through hips and knees, and lowers to the mattress.
5. The mattress locally compresses; sleeves and folded fabric settle after the torso.
6. His shoulders lower, gaze returns, and the camera stabilizes for the dialogue/post window.

The ear/head response expresses alertness; the step, lowering, mattress response, and cloth lag are physically coupled parts of one approach-and-sit action. The final hold is subordinate to that action and provides the required performance window.

## Blocking table

| Subject | Start position/facing | Path/action | Contact/occlusion | End position/facing |
|---|---|---|---|---|
| POV camera/body | lying at pillow height, level toward guardian/window | one short jolt and recovery; no detached orbit | foreground bed remains visible | level on seated guardian |
| guardian | full body on floor beside left mattress edge; torso slightly toward window | ears, head, one step, hip/knee lowering | rear body contacts mattress; lower hips partly obscured only after contact | seated upright at edge, gaze to POV |
| folded shirt | between both hands at waist | travels with both forearms; slight inertial lag | never transfers to POV or mattress | still across both forearms |
| mattress/bedding | uncompressed beside guardian | receives body weight | local dip and one fold pull toward contact | remains compressed under seated body |

## POV camera-body choreography

- body support and camera height: head/pillow support at bed height;
- gaze trigger: thunder causes one small jolt, after which the view recovers on the guardian;
- movement path/amplitude: restrained body-linked displacement only; no crane, orbit, reverse, or unexplained dolly;
- stabilization/re-anchor: camera returns level on the seated guardian for the final hold;
- forbidden physical impossibility and constructive alternative: do not ask the already-visible room to appear through an eye-opening action; begin already awake and use the thunder jolt as the first visible change.

## Contact and prop continuity

- moving limb owner: guardian's legs/hips perform the lowering; both guardian hands retain the shirt;
- contacted body/object and side: guardian's rear body contacts the left mattress edge;
- visible contact point: left edge near the guardian's final pelvis position;
- occlusion order: legs and contact path remain readable until the body reaches the bed; hands and shirt stay visible throughout;
- physical feedback: mattress edge depresses and a bedding fold pulls inward; sleeves and shirt settle after torso;
- prop ownership throughout: guardian supports the folded shirt with both hands;
- final readable state: seated guardian, shirt across forearms, feet below edge, level POV.

## Performance direction

- character objective/subtext: reassure while remaining alert to the storm;
- opening behavior: shoulders slightly high, ears alert, grip steady;
- trigger response: ears orient before head; no broad fear recoil;
- body/gaze/hand/anatomy detail: one measured step, controlled lowering, secure two-handed support, gaze returns only after settling;
- change after action: shoulders lower a small amount and the face holds steady for the line;
- idle behavior during holds: quiet breathing and minimal ear life, not arbitrary camera motion;
- OOC risks: rushing, exaggerated panic, ornamental gesture, dropping the shirt, or broadly smiling.

## Dialogue and voice

- exact line: “Safe.”;
- speaker: Iven / the visible guardian;
- language/speech stage: English for this teaching example; canonical final dialogue;
- delivery and breath: low, clipped, protective; one quiet preparatory breath;
- visual window: after body, mattress, sleeves, and shirt settle;
- same-pass, separate operation, or post route: separate voice/lip-sync or deliberate dubbing described in `post-production.md`;
- subtitle/caption route: off.

## Sound, atmosphere, light, and music

- ambient bed: steady rain;
- trigger effect: one close thunderclap aligned with the camera jolt;
- contact/material sounds: restrained mattress compression and cloth movement;
- named light/weather cause and visible effect: warm lamp stays stable; cool rain/lightning remains rear-right and may catch the brow scar without bleaching the room;
- music cue/stem/edit point: no music under thunder or the line;
- audio bridge/tail: rain continues through the final hold.

## Clip structure and duration

- target story time: about 8 seconds for picture action and stable hold;
- selected output duration: 8 seconds;
- slack and how it is used: final near-still hold for dialogue/post and continuity extraction;
- causal ordering or requested timing: ordered phases, not edit-timeline precision;
- split decision and reason: keep one pass because the micro-actions form one physically coupled action; switch to source performance or adjacent shots if repeated real runs cannot preserve contact/prop continuity.

## Creative-requirement transfer

| Requirement | Carrier | Exact implementation | Review evidence | Fallback |
|---|---|---|---|---|
| opening POV, room, identity, clothing, shirt, floor placement | start image | `inputs/opening-frame.png` in image input | compare first returned frames with file | rebuild/composite or edit/restyle |
| thunder-linked jolt, ears-before-head, step, lower, settle | primary prompt | entire `submitted-text.txt` | inspect order and continuity in every variant | simplify one competing layer, split, or use source performance |
| two-handed shirt ownership | start image plus prompt | visible shirt/hands and explicit support throughout | inspect both hands and prop every phase | repair/edit or make endpoint/source motion stronger |
| mattress response and cloth lag | primary prompt and review | explicit local compression, fold pull, sleeves/fabric settle last | visible contact response | start/end or video-edit route |
| seated endpoint | prompt landing plus acceptance | final hold described; no end image sent | terminal-frame inspection | select/repair or change operation |
| exact line and audio | post-production plan | approved voice plus rain/thunder/Foley stems | final composite review | alternate performance/dubbing route |

## Operation card

Operation name used by surface: Image to Video  
Exact target/editor/API/model: Runway web application, Gen-4.5  
Evidence date/source: 2026-08-04; official Runway Gen-4.5 creation and Image-to-Video prompting guides listed in `submission-sheet.md`  
Actual controls/request keys: image input in the prompt workflow; primary text prompt; aspect ratio; duration; FPS  
Actual files/text in each control: `inputs/opening-frame.png`; exact contents of `submitted-text.txt`; 16:9; 8 seconds; 24 FPS  
Settings: 1280×720 input, 16:9, 8 seconds, 24 FPS  
What submitted media supplies: opening composition, room landmarks, visible guardian identity/clothing, shirt, floor placement, POV relation  
What prompt must still establish: cause, ordered action, body mechanics, mattress/fabric response, camera stabilization, landing  
What is routed elsewhere: exact dialogue, final audio mix, endpoint repair  
Prompt rewrite evidence: not observed; preserve any text transformation shown by the actual surface  
Unknowns: adherence, identity/prop continuity, seated endpoint fidelity, and current account-specific UI behavior.

## Exact submission package

- submission sheet: `submission-sheet.md`;
- primary text file: `submitted-text.txt`;
- auxiliary text files: none for the picture generation field;
- submitted media: `inputs/opening-frame.png`;
- request template, when used: none for this web example;
- post-production plan: `post-production.md`.

## Acceptance criteria

Required:

- one continuous first-person approach-and-sit action;
- same guardian, clothing, brow scar, and folded shirt;
- ears turn before head after thunder;
- one readable step and controlled lowering path;
- shirt remains supported by both hands;
- mattress/bedding visibly reacts to weight;
- final camera is level at pillow height with a stable facial hold.

Flexible:

- exact step length, foot adjustment, cloth fold, lightning contour, and small timing variation.

Reject or repair:

- cut/teleport replaces movement; guardian stands on bed or floats; shirt changes owner/disappears/fuses; body never reaches mattress; camera reverses/selfies/orbits; bed remains rigid; landing cannot support dialogue or next-frame continuity.

---

<!-- Canonical artifact: examples/storm-watch/runway-gen45-i2v/submission-sheet.md -->

> **SUPERSEDED (2026-08-04).** This file describes the pre-rewrite beat (folded teal shirt, the English line "Safe.", a single stand-to-sit clip) and schematic input media since reclassified under `../planning-diagrams/`. The evidence-dated target-surface facts remain valid reference; everything beat-specific awaits the rebuild against the rewritten `source-brief.md` (Clip 1 of two), which starts only after the character sheet and boundary frames exist and are inspected. See `../phase-a-plan.md`.

# Exact Submission Sheet

## Target surface

- product/editor/API/model as displayed: Runway web application, Gen-4.5;
- account/tier/region when relevant: requires a plan that exposes Gen-4.5; exact account controls must be rechecked at run time;
- date checked: 2026-08-04;
- evidence sources:
  - https://help.runwayml.com/hc/en-us/articles/46974685288467-Creating-with-Gen-4-5
  - https://help.runwayml.com/hc/en-us/articles/48324313115155-Image-to-Video-Prompting-Guide

## Operation

- exact operation selected: Gen-4.5 Image to Video;
- reason: the literal opening composition, identity, prop ownership, and floor/bed relation are the hardest evidence for this branch; official guidance treats the uploaded image as the visual starting evidence and asks the text to concentrate on motion.

## File-to-control mapping

| Actual control/request key | Exact project file | Operator action | What this file contributes |
|---|---|---|---|
| image input in the prompt workflow | `inputs/opening-frame.png` | upload the PNG before generation | literal opening composition, visible guardian/prop, POV relation, room and light |

## Text fields

| Actual field/request key | Exact text file | Paste/use rule |
|---|---|---|
| primary text prompt | `submitted-text.txt` | paste the file literally; do not paste the director package |

## Settings

| Actual setting | Exact selection/value |
|---|---|
| model | Gen-4.5 |
| aspect ratio | 16:9 |
| duration | 8 seconds |
| FPS | 24 |

## Requirements routed outside this pass

| Requirement | Alternate operation/post path | Rejoin/review point |
|---|---|---|
| exact line “Safe.”, speaker, voice, lip timing | `post-production.md` voice/lip-sync or deliberate dubbing | after an accepted stable final picture hold |
| rain, thunder, mattress, and cloth audio | separate stems and final edit | final picture-and-audio composite |
| exact seated endpoint if prompt-only landing drifts | variant selection, picture repair, or change to first/last-frame/edit route | before final continuity-frame extraction |

## Preflight

- verify the image file opens and matches `frame-inspection.md`;
- recheck that the current product still shows Gen-4.5 Image to Video and the chosen duration/FPS controls;
- preserve the exact submitted text and a screenshot/export of settings;
- do not assume a separate negative-prompt field that is not present on the actual surface;
- create the run record before submission and preserve every returned variant.

Evidence state: documentation-grounded, not run. No output fidelity, continuity success, prompt adherence, or quality is claimed.

---

<!-- Canonical artifact: examples/storm-watch/runway-gen45-i2v/post-production.md -->

> **SUPERSEDED (2026-08-04).** This file describes the pre-rewrite beat (folded teal shirt, the English line "Safe.", a single stand-to-sit clip) and schematic input media since reclassified under `../planning-diagrams/`. The evidence-dated target-surface facts remain valid reference; everything beat-specific awaits the rebuild against the rewritten `source-brief.md` (Clip 1 of two), which starts only after the character sheet and boundary frames exist and are inspected. See `../phase-a-plan.md`.

# Post-Production and Alternate-Path Plan

## Requirements not completed in picture generation

| Requirement | Reason not carried in this pass | Concrete next operation | Required source/output | Acceptance |
|---|---|---|---|---|
| exact line “Safe.” with Iven as speaker | exact wording, speaker ownership, and lip synchronization are not assumed from this picture package | approved voice recording plus documented lip-sync/performance operation, or deliberate off-camera dubbing over the hold | accepted picture variant and approved Iven voice | exact word, correct speaker, low clipped delivery, line occurs after settling |
| steady rain and close thunder | picture prompt describes visible causality but does not complete the final mix | create or select rain/thunder stems and place them in edit | clean ambience/effect stems | rain continuous; thunder aligned with initial jolt; line remains intelligible |
| mattress and cloth Foley | visible response does not create final production audio | add restrained contact and cloth stems | Foley or recorded material sounds | contact sounds support rather than exaggerate the action |
| precise final continuity frame | the planned endpoint is not the actual returned composite | select/repair picture, finish audio, then extract the true terminal frame | final edited master | frame is readable and physically usable for the next clip |

## Dialogue/audio

- exact line and speaker: Iven says “Safe.”;
- voice/performance source: approved Iven voice, low, clipped, protective, with one quiet preparatory breath;
- lip-sync or visual hold: use the stable final facial hold when lip-sync is available; otherwise place the line over a natural near-still bedside hold that does not demand visible articulation;
- ambience/effects/music stems: steady rain, one close thunderclap, restrained mattress compression, folded-shirt and sleeve movement; no competing music during the line;
- timing and mix notes: thunder precedes the approach, contact sounds land with the sit, the line follows body/material settling, and ambience remains present below the voice.

## Picture repair

- crop/stabilization: retain pillow-height POV and avoid a reverse/selfie read;
- identity/contact/prop correction: repair or reject variants where the guardian changes, the shirt leaves both hands, or the body does not reach the mattress;
- transition/composite: if the one-pass action fails repeatedly, use source performance plus edit/restyle or split the stand and sit across deliberately joined shots;
- color/light continuity: preserve the stable warm left lamp and cool rear-right window contribution.

## Rejoin

- files produced: final picture master, dialogue stem, ambience/effects stem, final mixed master;
- edit timeline position: dialogue begins only after the sit and material settle;
- terminal frame to extract after final composite: the last stable frame of the finished picture-and-audio master, not the planned endpoint illustration.

---

<!-- Canonical artifact: examples/storm-watch/runway-gen45-i2v/result-log.md -->

> **SUPERSEDED (2026-08-04).** This file describes the pre-rewrite beat (folded teal shirt, the English line "Safe.", a single stand-to-sit clip) and schematic input media since reclassified under `../planning-diagrams/`. The evidence-dated target-surface facts remain valid reference; everything beat-specific awaits the rebuild against the rewritten `source-brief.md` (Clip 1 of two), which starts only after the character sheet and boundary frames exist and are inspected. See `../phase-a-plan.md`.

# Storm Watch · Runway Gen-4.5 · Run Review
Run status: not run

Evidence state: documentation-grounded submission package; no returned video exists.

## Exact run identity

- date/time: not run;
- operator: none;
- target/editor/API/model shown at run time: not observed;
- submission sheet: `submission-sheet.md`;
- submitted media/text/settings: proposed only; see the sheet and exact text file;
- service-returned rewritten prompt, if any: none because no request occurred;
- output files and variant IDs: none.

## Variant observations

No variants exist. Do not fill observation fields until the exact package has been submitted and actual outputs are inspectable.

## Accepted result

- accepted variant: none;
- accepted visible/audible events: none;
- story/canon delta proposed: none;
- artifacts explicitly not canonized: all planned outcomes remain unobserved;
- extracted final frame: none;
- final audio tail: none.

## Requirement-transfer findings

No outcome findings exist. When run, compare every variant against identity, ears-before-head order, one-step lowering path, two-handed shirt ownership, mattress response, final hold, and continuity usefulness.

## Scoped tactic

No tactic has been inferred. A future change must cite an exact returned symptom rather than an imagined model limitation.

## State updates

None. This not-run example does not modify canon or production behavior.

---

<!-- Canonical artifact: examples/storm-watch/veo31-first-last/director-package.md -->

> **SUPERSEDED (2026-08-04).** This file describes the pre-rewrite beat (folded teal shirt, the English line "Safe.", a single stand-to-sit clip) and schematic input media since reclassified under `../planning-diagrams/`. The evidence-dated target-surface facts remain valid reference; everything beat-specific awaits the rebuild against the rewritten `source-brief.md` (Clip 1 of two), which starts only after the character sheet and boundary frames exist and are inspected. See `../phase-a-plan.md`.

# Parallel Home · Storm Watch · Clip 1 · Director Package
Status: prepared for Veo 3.1 first-and-last-frame generation; not submitted

## Story and continuity

- episode purpose: convert the POV's nighttime alarm into Iven's quiet bedside reassurance;
- clip function: interpolate one physically continuous stand-to-sit response between inspected endpoints;
- previous accepted endpoint: none; both endpoint images were created for this fresh clip;
- intended visible/audible change: standing vigilance becomes seated reassurance without changing shirt ownership;
- next bridge/landing: the actual accepted finished endpoint, not merely the supplied end illustration, will seed continuation.

## Inspected evidence

| Media | Submitted/planning/source | Direct observations | Uncertainty |
|---|---|---|---|
| `inputs/start-frame.png` | submitted first frame | schematic pillow-height POV; guardian stands on floor left of mattress; shirt in both hands; room/light landmarks visible | realistic motion, identity, contact, and adherence untested |
| `inputs/end-frame.png` | submitted last frame | same room/camera; guardian seated at left mattress edge; legs below edge; local mattress dip; shirt still in both hands | target may fail to interpolate or match endpoint; planned frame is not a returned terminal frame |

## Shot proposition

Opening image: supplied first frame with Iven standing beside the left mattress edge.

Dominant visible change: a thunder-linked ears/head reaction leads into the short step and controlled lowering to the supplied seated state.

Cause: thunder startles the POV and causes Iven to close the distance protectively.

Ordered physical path: camera jolt, ears, head, one step, hip/knee bend, mattress contact/dip, torso settle, sleeves/shirt settle, gaze return.

Performance change: alert shoulders soften after the seated contact.

Landing image: supplied last frame relation, followed by a stable hold suitable for the line and next continuity review.

Dialogue/sound: exact line and final sound are completed through `post-production.md` for this chosen model/package.

Must be exact: endpoint identities and room relation, two-handed shirt ownership, physically plausible stand-to-sit order, first-person camera, usable ending.

May vary: precise timing, foot placement, fold pattern, and lightning shape when endpoint function remains intact.

## Beat and causal spine

1. Start frame holds long enough to read the standing state.
2. Thunder causes one small first-person camera-body jolt.
3. Ears orient toward the rear-right window before the head.
4. Guardian keeps both hands under the shirt, takes the short step, bends through hips/knees, and reaches the mattress.
5. The supplied mattress dip becomes physically motivated; torso settles before sleeves and folded fabric.
6. Gaze returns and the shot reaches the supplied end relation without a cut.

The supplied images establish endpoints; the prompt remains specific about the causal physical path and performance order between them.

## Blocking table

| Subject | Start position/facing | Path/action | Contact/occlusion | End position/facing |
|---|---|---|---|---|
| POV camera/body | level at pillow height | one small jolt and recovery | foreground bed remains visible | same level relation at end |
| guardian | full body on floor beside left mattress edge | ears/head, short step, bend, sit | rear body reaches mattress; hands/prop remain visible | seated upright on edge, gaze POV |
| folded shirt | both hands at waist | travels with forearms | no transfer or disappearance | both hands across forearms |
| mattress/bedding | uncompressed at start | receives weight | local dip/fold at contact | supplied compressed endpoint |

## POV camera-body choreography

- body support and camera height: pillow-supported first-person view;
- gaze trigger: thunder-linked jolt, then recovery;
- movement path/amplitude: restrained; endpoints preserve the same basic camera relation;
- stabilization/re-anchor: reach the end frame level without reverse or detached orbit;
- forbidden physical impossibility and constructive alternative: endpoints must be physically connectable; if real interpolation produces teleportation or impossible lower-body motion, reject and change operation rather than add contradictory prose.

## Contact and prop continuity

- moving limb owner: guardian;
- contacted body/object and side: rear body to left mattress edge;
- visible contact point: supplied endpoint's local mattress dip;
- occlusion order: contact may obscure lower hips only after the step/lowering remains readable;
- physical feedback: supplied dip is motivated by body weight; bedding fold pulls toward contact;
- prop ownership throughout: shirt remains supported in both guardian hands;
- final readable state: supplied seated relation, stable gaze, level POV.

## Performance direction

- character objective/subtext: move closer without losing storm vigilance;
- opening behavior: shoulders high enough to read alertness; ears active;
- trigger response: ears precede head, no broad panic recoil;
- body/gaze/hand/anatomy detail: controlled one-step lowering, hands steady under the shirt, gaze returns after settling;
- change after action: small shoulder release and stable face;
- idle behavior during holds: restrained breath/ear life;
- OOC risks: exaggerated fear, rush, dropped prop, decorative gesture, broad smile.

## Dialogue and voice

- exact line: “Safe.”;
- speaker: Iven / visible guardian;
- language/speech stage: English teaching example; final canonical line;
- delivery and breath: low, clipped, protective, one quiet breath;
- visual window: after reaching the end relation;
- same-pass, separate operation, or post route: separate voice/lip-sync or dubbing in `post-production.md`;
- subtitle/caption route: off.

## Sound, atmosphere, light, and music

- ambient bed: steady rain;
- trigger effect: close thunderclap;
- contact/material sounds: restrained mattress and cloth;
- named light/weather cause and visible effect: warm left lamp stable; rear-right window remains cool/rainy;
- music cue/stem/edit point: no competing music during trigger or line;
- audio bridge/tail: rain carries through the end.

## Clip structure and duration

- target story time: 8 seconds;
- selected output duration: 8 seconds;
- slack and how it is used: brief endpoint hold;
- causal ordering or requested timing: ordered progression only; no claim of frame-accurate timestamps;
- split decision and reason: one interpolation because start and end describe one coupled action; use source performance/edit or adjacent shots if actual variants cannot connect them plausibly.

## Creative-requirement transfer

| Requirement | Carrier | Exact implementation | Review evidence | Fallback |
|---|---|---|---|---|
| opening scene/identity/prop | first image | `inputs/start-frame.png` as `image`/Start | compare opening frames | rebuild start or edit/restyle |
| seated endpoint/contact geometry | last image | `inputs/end-frame.png` as `lastFrame`/End | compare terminal frames and contact path | repair/select/edit; planned image alone is not accepted result |
| causal path and performance order | primary prompt | `submitted-text.txt` | inspect order, continuity, and physical plausibility | simplify, source performance, or split |
| unwanted reverse/cut categories | documented REST negative field | `negative-prompt.txt` only in `parameters.negativePrompt` | inspect whether categories appear | constructive media/prompt, repair, reject |
| exact line and sound | post-production | approved voice and stems | final composite review | alternate performance/dubbing route |
| actual continuation frame | accepted final composite | extract after all repair/audio | inspect true terminal frame | corrective derivative with lineage |

## Operation card

Operation name used by surface: Image-to-video with Start and optional End / first-and-last-frame generation  
Exact target/editor/API/model: Google Cloud Gemini Enterprise Agent Platform / Veo `veo-3.1-generate-001`  
Evidence date/source: 2026-08-04; official first/last-frame procedure, Veo 3.1 model page, prompt rewriter page, and API fields listed in `submission-sheet.md`  
Actual controls/request keys: Prompt; Start/`instances[0].image`; End/`instances[0].lastFrame`; `parameters.aspectRatio`; `durationSeconds`; `sampleCount`; `resolution`; optional `negativePrompt`; `storageUri`  
Actual files/text in each control: start/end PNGs, exact primary text, exact exclusion list, and request placeholders from the package files  
Settings: 16:9, 8 seconds, 4 results, 720p  
What submitted media supplies: both endpoint compositions, identity/clothing/prop at endpoints, room/camera relation, intended contact landing  
What prompt must still establish: causal action order, continuous physical path, performance change, material settling  
What is routed elsewhere: exact dialogue and final audio mix; endpoint repair if needed  
Prompt rewrite evidence: prompt rewriting is documented for Veo 3.1 and cannot be disabled; preserve any returned rewritten prompt when exposed  
Unknowns: actual interpolation, endpoint adherence, identity/prop continuity, and service behavior for this exact request.

## Exact submission package

- submission sheet: `submission-sheet.md`;
- primary text file: `submitted-text.txt`;
- auxiliary text files: `negative-prompt.txt` for the documented REST field only;
- submitted media: `inputs/start-frame.png`, `inputs/end-frame.png`;
- request template, when used: `request-body.template.json`;
- post-production plan: `post-production.md`.

## Acceptance criteria

Required:

- continuous first-person physical path between supplied states;
- same guardian, clothing, scar, shirt, room, and camera relation;
- ears-before-head response after thunder;
- no cut or teleport;
- shirt remains in both hands;
- contact and mattress dip are physically motivated;
- end is stable and useful for dialogue/continuity.

Flexible:

- exact step length, cloth folds, timing, and lightning geometry.

Reject or repair:

- endpoints are connected through teleportation, morphing, reverse angle, or impossible legs; shirt changes owner/disappears; mattress contact is unreadable; end misses the supplied relationship; final composite cannot seed the next clip.

---

<!-- Canonical artifact: examples/storm-watch/veo31-first-last/submission-sheet.md -->

> **SUPERSEDED (2026-08-04).** This file describes the pre-rewrite beat (folded teal shirt, the English line "Safe.", a single stand-to-sit clip) and schematic input media since reclassified under `../planning-diagrams/`. The evidence-dated target-surface facts remain valid reference; everything beat-specific awaits the rebuild against the rewritten `source-brief.md` (Clip 1 of two), which starts only after the character sheet and boundary frames exist and are inspected. See `../phase-a-plan.md`.

# Exact Submission Sheet

## Target surface

- product/editor/API/model as displayed: Veo on Google Cloud Gemini Enterprise Agent Platform; API model `veo-3.1-generate-001`;
- account/tier/region when relevant: model availability and project quota must be checked; example uses the documented `us-central1` publisher-model endpoint;
- date checked: 2026-08-04;
- evidence sources:
  - https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/generate-videos-from-first-and-last-frames
  - https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/veo/3-1-generate
  - https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/turn-the-prompt-rewriter-off

## Operation

- exact operation selected: image-to-video using distinct first and last frame inputs;
- reason: the seated contact/end relation is critical enough to supply as visual evidence rather than leave entirely to a text-only landing.

## File-to-control mapping

| Actual control/request key | Exact project file | Operator action | What this file contributes |
|---|---|---|---|
| console Input images → Start / REST `instances[0].image` | `inputs/start-frame.png` | upload as Start or place its Cloud Storage URI in `image.gcsUri` | opening room, standing pose, identity, shirt ownership, POV relation |
| console Input images → End / REST `instances[0].lastFrame` | `inputs/end-frame.png` | upload as End or place its Cloud Storage URI in `lastFrame.gcsUri` | seated relation, contact dip, final prop/camera state |

## Text fields

| Actual field/request key | Exact text file | Paste/use rule |
|---|---|---|
| console Prompt / REST `instances[0].prompt` | `submitted-text.txt` | use the file literally |
| REST `parameters.negativePrompt` | `negative-prompt.txt` | use only in the documented separate parameter; do not silently append it to the primary prompt |

## Settings

| Actual setting | Exact selection/value |
|---|---|
| model | `veo-3.1-generate-001` |
| aspect ratio | 16:9 |
| duration | 8 seconds |
| number of outputs / `sampleCount` | 4 |
| resolution | 720p |
| output location / `storageUri` | operator-supplied Cloud Storage URI |

## Requirements routed outside this pass

| Requirement | Alternate operation/post path | Rejoin/review point |
|---|---|---|
| exact line “Safe.”, approved voice, exact speaker/lip timing | `post-production.md` | after accepted endpoint hold |
| steady rain, close thunder, mattress/cloth Foley | separate audio stems and mix | final composite |
| mismatch to supplied end or impossible interpolation | variant selection, picture repair, source-performance/edit, or adjacent shots | before extracting continuity frame |

## Prompt rewriting

Official documentation checked for this example states that prompt rewriting cannot be disabled for Veo 3 and 3.1. Preserve the exact original text and any rewritten prompt returned or exposed by the service. Do not treat the prose as a deterministic program.

## Preflight

- upload both exact 1280×720 PNGs and confirm Start/End assignment;
- replace every infrastructure placeholder in `request-body.template.json` outside the prompt files;
- verify current model, region, quota, duration, resolution, and output-count controls;
- preserve the actual request and any service-returned rewritten prompt;
- create the run record before submission and retain all four results.

Evidence state: documentation-grounded, not run. No output fidelity, interpolation success, prompt adherence, or quality is claimed.

---

<!-- Canonical artifact: examples/storm-watch/veo31-first-last/post-production.md -->

> **SUPERSEDED (2026-08-04).** This file describes the pre-rewrite beat (folded teal shirt, the English line "Safe.", a single stand-to-sit clip) and schematic input media since reclassified under `../planning-diagrams/`. The evidence-dated target-surface facts remain valid reference; everything beat-specific awaits the rebuild against the rewritten `source-brief.md` (Clip 1 of two), which starts only after the character sheet and boundary frames exist and are inspected. See `../phase-a-plan.md`.

# Post-Production and Alternate-Path Plan

## Requirements not completed in picture generation

| Requirement | Reason not carried in this pass | Concrete next operation | Required source/output | Acceptance |
|---|---|---|---|---|
| exact line “Safe.” with Iven as speaker | exact wording, speaker ownership, and lip synchronization are not assumed from this picture package | approved voice recording plus documented lip-sync/performance operation, or deliberate off-camera dubbing over the hold | accepted picture variant and approved Iven voice | exact word, correct speaker, low clipped delivery, line occurs after settling |
| steady rain and close thunder | picture prompt describes visible causality but does not complete the final mix | create or select rain/thunder stems and place them in edit | clean ambience/effect stems | rain continuous; thunder aligned with initial jolt; line remains intelligible |
| mattress and cloth Foley | visible response does not create final production audio | add restrained contact and cloth stems | Foley or recorded material sounds | contact sounds support rather than exaggerate the action |
| precise final continuity frame | the planned endpoint is not the actual returned composite | select/repair picture, finish audio, then extract the true terminal frame | final edited master | frame is readable and physically usable for the next clip |

## Dialogue/audio

- exact line and speaker: Iven says “Safe.”;
- voice/performance source: approved Iven voice, low, clipped, protective, with one quiet preparatory breath;
- lip-sync or visual hold: use the stable final facial hold when lip-sync is available; otherwise place the line over a natural near-still bedside hold that does not demand visible articulation;
- ambience/effects/music stems: steady rain, one close thunderclap, restrained mattress compression, folded-shirt and sleeve movement; no competing music during the line;
- timing and mix notes: thunder precedes the approach, contact sounds land with the sit, the line follows body/material settling, and ambience remains present below the voice.

## Picture repair

- crop/stabilization: retain pillow-height POV and avoid a reverse/selfie read;
- identity/contact/prop correction: repair or reject variants where the guardian changes, the shirt leaves both hands, or the body does not reach the mattress;
- transition/composite: if the one-pass action fails repeatedly, use source performance plus edit/restyle or split the stand and sit across deliberately joined shots;
- color/light continuity: preserve the stable warm left lamp and cool rear-right window contribution.

## Rejoin

- files produced: final picture master, dialogue stem, ambience/effects stem, final mixed master;
- edit timeline position: dialogue begins only after the sit and material settle;
- terminal frame to extract after final composite: the last stable frame of the finished picture-and-audio master, not the planned endpoint illustration.

---

<!-- Canonical artifact: examples/storm-watch/veo31-first-last/result-log.md -->

> **SUPERSEDED (2026-08-04).** This file describes the pre-rewrite beat (folded teal shirt, the English line "Safe.", a single stand-to-sit clip) and schematic input media since reclassified under `../planning-diagrams/`. The evidence-dated target-surface facts remain valid reference; everything beat-specific awaits the rebuild against the rewritten `source-brief.md` (Clip 1 of two), which starts only after the character sheet and boundary frames exist and are inspected. See `../phase-a-plan.md`.

# Storm Watch · Veo 3.1 First/Last Frame · Run Review
Run status: not run

Evidence state: documentation-grounded submission package; no returned video exists.

## Exact run identity

- date/time: not run;
- operator: none;
- target/editor/API/model shown at run time: not observed;
- submission sheet: `submission-sheet.md`;
- submitted media/text/settings: proposed only; see the sheet, exact text, exclusion file, and request template;
- service-returned rewritten prompt, if any: none because no request occurred;
- output files and variant IDs: none.

## Variant observations

No variants exist. When run, preserve all outputs and compare both supplied endpoints, the physical path, prompt rewrite evidence, unwanted cuts, contact, prop ownership, and endpoint usefulness.

## Accepted result

- accepted variant: none;
- accepted visible/audible events: none;
- story/canon delta proposed: none;
- artifacts explicitly not canonized: all planned outcomes remain unobserved;
- extracted final frame: none;
- final audio tail: none.

## Requirement-transfer findings

No outcome findings exist. The supplied end image remains a planned endpoint, not a successful terminal frame.

## Scoped tactic

No tactic has been inferred. Any next change must cite an exact returned symptom.

## State updates

None. This not-run example does not modify canon or production behavior.

---

<!-- Canonical artifact: examples/storm-watch/seedance20-first-last/director-package.md -->

# Parallel Home · Storm Watch · Clip 1 · Director Package
Status: prepared for Seedance 2.0 first-and-last-frame generation with in-pass audio on the OpenRouter surface; submission recorded in `result-log.md`

## Story and continuity

- episode purpose: turn storm alarm into a negotiated compromise between Iven's guard posture and the POV's invitation;
- clip function: the invitation. Iven's watch is interrupted by the POV's request, and his attention divides without his body yielding;
- previous accepted endpoint: none; this is the episode's first clip, and both endpoint images were created from the approved character sheet;
- intended visible/audible change: standing vigilance acquires one point of attention toward the bed: a small head turn, one swiveled ear, a lifted tail, under continuous rain, after the POV lifts the blanket corner and pats the mattress;
- next bridge/landing: Clip 2, the compromise, starts from this clip's accepted terminal frame, not from the supplied end image.

## Inspected evidence

| Media | Submitted/planning/source | Direct observations | Uncertainty |
|---|---|---|---|
| `../media/clip1-start.jpg` | submitted `first_frame` | pillow-height POV; bed lower-right; Iven on the left floor strip, back three-quarter, face to the rainy rear-right window; folded teal sleepwear held flat at waist; lamp left dominant; POV hand on near bedding | far hand's grip occluded by his body; target adherence untested |
| `../media/clip1-end.jpg` | submitted `last_frame` | same frame with the blanket corner folded back, the POV hand flat on the exposed sheet, his head turned a few degrees bedward, near ear swiveled back, tail lifted | far ear partially occluded; a planned frame, not a returned terminal frame |
| `../media/character-sheet.png` | production authority, not submitted | one integrated white-furred anthro wolf, digitigrade, scar above his left brow, charcoal robe | proves the design, not the target's ability to animate it |

Full inspections are in `../frame-inspection.md`; hashes and lineage in `../media/media-log.md`.

## Shot proposition

Opening image: supplied first frame, Iven standing watch at the bedside, back to the POV.

Dominant visible change: his ears track a thunder roll; the POV's own hand lifts the near blanket corner and pats the mattress twice; his head turns a few degrees toward the bed and his near ear swings back.

Cause: the storm holds his watch; the POV's invitation interrupts it.

Ordered physical path: camera jolt, ear rotation with the thunder, blanket lift by the POV hand, two soft pats, his head's small turn, near-ear swivel, slight tail lift, settle into the supplied end relation.

Performance change: unbroken vigilance acquires a single point of attention toward the bed.

Landing image: supplied last frame relation, held stable.

Dialogue/sound: rain, one close thunderclap, blanket and pat sounds are requested in this pass; his one low word stays in `post-production.md`.

Must be exact: endpoint identities and room relation, two-handed sleepwear carry throughout, no torso turn, no step, POV hand ownership of the blanket action, first-person camera, usable ending.

May vary: lightning presence, exact ear timing, fold shapes, rain texture, the character of generated ambience.

## Beat and causal spine

1. The start frame holds long enough to read the watch.
2. A close thunderclap lands with one small first-person camera jolt; he does not startle.
3. His upright ears turn with the rolling thunder; feet and torso stay planted.
4. The POV's hand lifts the near blanket corner a hand's width and pats the exposed mattress twice.
5. His head turns a few degrees toward the bed; the near ear swivels back while the far ear holds the window; the tail lifts slightly.
6. The shot settles into the supplied end relation without a cut.

The supplied images establish both endpoints; the prompt carries the causal order, the POV hand's ownership of the invitation, and the sound.

## Blocking table

| Subject | Start position/facing | Path/action | Contact/occlusion | End position/facing |
|---|---|---|---|---|
| POV camera/body | level at pillow height | one small jolt, then the hand's blanket lift and two pats | hand moves from bedding to exposed sheet | same level relation, hand at rest on the sheet |
| Iven | standing on the left floor strip, back three-quarter, face to window | ear rotation, small head turn only | body continues to part-occlude the held bundle | same stance, head a few degrees bedward, near ear back |
| folded sleepwear | both hands at waist | travels nowhere | no transfer, no drop, no unfolding | both hands at waist, unchanged |
| blanket/mattress | corner flat | near corner lifted by the POV hand, two pats | fold exposes pale sheet | corner folded back, POV hand resting on sheet |
| tail | relaxed toward the floor | slight lift | none | lifted, not fully relaxed |

## POV camera-body choreography

- body support and camera height: pillow-supported first-person view, level;
- gaze trigger: the thunderclap jolt, then recovery; no orbit, no reverse;
- the POV acts: the visible hand performs the blanket lift and pats; the camera does not move to follow it beyond natural coupling;
- stabilization/re-anchor: return to the supplied end relation;
- camera control setting: none exists on this surface; the required jolt and stillness are carried by the prompt;
- forbidden physical impossibility and constructive alternative: if variants connect the endpoints with a step, a torso turn, or a teleport, reject and adjust seed, duration, or the end anchor rather than adding contradictory prose.

## Contact and prop continuity

- moving limb owner for the invitation: the POV's hand, and only it, touches the blanket and mattress;
- visible contact point: the exposed sheet where the pats land;
- physical feedback: the blanket corner folds back a hand's width; soft pat compressions;
- prop ownership throughout: the folded teal sleepwear stays supported in Iven's two hands; no transfer, no unfolding, no set-down in this clip;
- occlusion order: his body may part-occlude the bundle, as in both supplied frames; the near hand's grip stays readable;
- final readable state: supplied end relation with the POV hand at rest.

## Performance direction

- character objective/subtext: hold the watch; let the invitation in without yielding the post;
- opening behavior: standing straight, ears upright and windowward, grip steady;
- trigger response: ears track the thunder; no flinch, no crouch, no broad gesture;
- response to the invitation: the head turn is small and controlled; one ear yields, the other does not; the tail's slight lift is the only warmth shown;
- idle behavior during holds: breath, ear micro-motion, rain light on fur;
- OOC risks: startle reactions, turning around, stepping toward the bed, dropping or unfolding the sleepwear, tail wagging.

## Dialogue and voice

- exact line: one word, Japanese, proposed canon 「大丈夫」, low, almost under the thunder;
- speaker: Iven, back to camera;
- language/speech stage: Japanese; single-word stage; no sentence is built around it;
- same-pass, separate operation, or post route: post-production. His back is to the camera, so no on-screen lip performance exists to conflict with, and in-pass speech is excluded in the primary prompt so generated audio cannot collide with the approved voice;
- subtitle/caption route: off by default; a sidecar track, proposed English, is prepared in delivery metadata and never burned in.

## Sound, atmosphere, light, and music

- ambient bed: steady rain, requested in this pass via `generate_audio`;
- trigger effect: one close thunderclap aligned by prose to the opening jolt;
- action sounds: soft blanket lift and two quiet mattress pats;
- named light/weather cause and visible effect: warm left lamp stable and dominant; cool rain light rear-right; no lightning is required by either endpoint;
- music cue/stem/edit point: music excluded in the primary prompt;
- audio bridge/tail: rain carries through the end hold into Clip 2;
- production hypothesis and review: generated ambience is a candidate stem, not final audio; if it is unusable or fights the line, mute it and use the stems in `post-production.md`.

## Clip structure and duration

- target story time: about 8 seconds;
- selected output duration: 8 seconds, from the documented 4-15 s range;
- slack and how it is used: opening watch hold and closing settle;
- causal ordering or requested timing: ordered progression only, no frame timestamps;
- split decision and reason: the invitation is one coupled exchange, one clip; the compromise is a separate clip that starts from this clip's accepted terminal frame.

## Creative-requirement transfer

| Requirement | Carrier | Exact implementation | Review evidence | Fallback |
|---|---|---|---|---|
| opening scene/identity/prop/POV | first image | `../media/clip1-start.jpg` as `first_frame` | compare opening frames | rebuild frame from the sheet |
| invitation endpoint | last image | `../media/clip1-end.jpg` as `last_frame` | compare terminal frames | repair/select; planned image is not an accepted result |
| causal path, POV hand ownership, ear performance | primary prompt | `submitted-text.txt` | inspect order and ownership in every variant | simplify, adjust seed/duration, or re-anchor |
| unwanted reverse/cut/step/turn categories | primary prompt exclusions | one negation per artifact, no separate field exists | inspect whether categories appear | reject and adjust |
| rain, thunder, blanket and pat sounds | this pass | `generate_audio` true plus the sound sentence | listen to every variant | mute and use post stems |
| the one low word and speaker | post-production | approved voice over the hold | final composite review | timing shift within the hold |
| actual continuation frame | accepted final composite | extract after picture/audio acceptance | inspect the true terminal frame | corrective derivative with lineage |

## Operation card

Operation name used by surface: video generation with first and last frame images
Exact target/editor/API/model: OpenRouter `POST /api/v1/videos` / `bytedance/seedance-2.0`
Evidence date/source: 2026-08-04; the videos/models listing, the video-generation guide, and seven direct submissions recorded in the field studies
Actual controls/request keys: `model`, `prompt`, `frame_images[].{type,image_url,frame_type}`, `aspect_ratio`, `duration`, `resolution`, `seed`, `generate_audio`
Actual files/text in each control: the two jpeg frames as base64 data URLs, the exact primary text, per `request-body.template.json`
Settings: 720p, 16:9, 8 s, seed 21, `generate_audio` true
What submitted media supplies: both endpoint compositions, identity, clothing, prop state, room geometry, POV relation
What prompt must still establish: causal order, the POV hand's ownership of the invitation, ear choreography, stillness constraints, sound, every exclusion
What is routed elsewhere: the word, the voice, the mix, subtitles, Clip 2
Prompt rewrite evidence: no rewritten prompt returned in any observed response; unobserved rather than absent
Unknowns: seed determinism; default watermark behavior; adherence for this exact media pair.

## Exact submission package

- submission sheet: `submission-sheet.md`;
- primary text file: `submitted-text.txt`;
- auxiliary text files: none; no separate exclusion field exists;
- submitted media: `../media/clip1-start.jpg`, `../media/clip1-end.jpg`, as data URLs;
- request template: `request-body.template.json`;
- post-production plan: `post-production.md`.

## Acceptance criteria

Required:

- one continuous first-person shot between the supplied states, no cut, no teleport, no morph;
- same guardian, clothing, room, and camera relation as the supplied frames;
- the sleepwear stays folded in his two-handed carry throughout;
- the POV hand, not his, performs the blanket lift and pats;
- his feet do not move and his torso does not turn;
- ears track the thunder before the head moves;
- the end state is stable and usable as Clip 2's opening evidence;
- generated audio contains no speech and no music.

Flexible:

- lightning, exact ear timing, fold shapes, pat timing, rain and thunder texture.

Reject or repair:

- a step, a torso turn, or a walk; endpoint connection by teleport or morph; the sleepwear unfolding, dropping, or changing hands; the POV hand acting as his hand or a third hand appearing; camera reverse or orbit; speech or music in the generated audio; an end state that cannot seed Clip 2.

---

<!-- Canonical artifact: examples/storm-watch/seedance20-first-last/submission-sheet.md -->

# Exact Submission Sheet

## Target surface

- product/editor/API/model as displayed: OpenRouter, `POST https://openrouter.ai/api/v1/videos`; model `bytedance/seedance-2.0`, canonical slug `bytedance/seedance-2.0-20260414`;
- account/tier/region when relevant: any OpenRouter API key with video access; no region selection is exposed;
- date checked: 2026-08-04;
- evidence sources:
  - `GET https://openrouter.ai/api/v1/videos/models`, retrieved directly on 2026-08-04: supported durations 4-15 s, resolutions 480p/720p/1080p/4K, aspect ratios including 16:9, `frame_images` roles `first_frame` and `last_frame`, `generate_audio` true, `seed` true, allowed passthrough parameters `watermark` and `req_key`;
  - the OpenRouter video-generation guide and skills reference, same day, for the request/response shape;
  - direct observations from seven submissions executed on this surface on 2026-08-04, preserved in `../../field-study/2026-08-04-seedance20-openrouter/run-record.md` and `../../field-study/2026-08-04-seedance20-openrouter-prose-identity/run-record.md`.

This branch previously documented BytePlus ModelArk for the same model; that sheet remains in git history. The same model reached through ModelArk uses `content[]` entries with `role` values instead of `frame_images[].frame_type`, documents `camera_fixed`, and was never actually submitted to. The two surfaces are not interchangeable, which is exactly what the third branch exists to demonstrate: the target surface, not the model name, decides the submission.

## Operation

- exact operation selected: image-to-video generation from separate first and last frames, with in-pass audio;
- reason: the invitation beat is anchored by two inspected pose-close frames, so the endpoint relation travels as media rather than text; the field study's run 4 showed a visible switch at the contact when widely separated endpoints were both anchored, so the clip that anchors both ends is the small-motion clip by design;
- second reason: this surface generates audio in the same pass, so the storm bed is attempted here with the post stems kept as authority.

## File-to-control mapping

| Actual control/request key | Exact project file | Operator action | What this file contributes |
|---|---|---|---|
| `frame_images[0]`: `type` `image_url`, `frame_type` `first_frame` | `../media/clip1-start.jpg` | encode as a `data:image/jpeg;base64,` URL in `image_url.url` | opening room and stated geometry, sheet-matched identity from behind, watch posture, two-handed sleepwear carry, POV relation |
| `frame_images[1]`: `type` `image_url`, `frame_type` `last_frame` | `../media/clip1-end.jpg` | encode as a `data:image/jpeg;base64,` URL in `image_url.url` | lifted blanket corner with the POV hand on the sheet, the small head turn, the swiveled near ear, the lifted tail |

Mime types must match the actual containers recorded in `../media/media-log.md`: both Clip 1 frames are jpeg. Base64 data URLs at these sizes (654 KB and 674 KB) match how the field study's run 4 media reached this surface.

## Text fields

| Actual field/request key | Exact text file | Paste/use rule |
|---|---|---|
| `prompt` | `submitted-text.txt` | use the file literally |

No separate negative or exclusion parameter exists on this surface, so every exclusion is written in the primary text, one negation per unwanted artifact.

## Settings

| Actual setting | Exact selection/value |
|---|---|
| `model` | `bytedance/seedance-2.0` |
| `resolution` | `720p` |
| `aspect_ratio` | `16:9` |
| `duration` | 8, from the documented 4-15 s range |
| `seed` | 21, fixed; whether this surface honors seed is unverified |
| `generate_audio` | true |

Cost arithmetic, observed: this model bills `video_tokens` at $0.000007. Every 8 s 720p run on 2026-08-04 billed exactly $1.2096, which is 172,800 video tokens; the model page's per-second listing did not predict charges, the token SKU does.

Queue behavior, observed same day: identical settings returned in 21.5 and 60.5 minutes. Plan polling accordingly.

## Requirements routed outside this pass

| Requirement | Alternate operation/post path | Rejoin/review point |
|---|---|---|
| Iven's one low word, Japanese, proposed 「大丈夫」, approved voice | `post-production.md`; his back is to the camera, so no lip performance exists to conflict with | over the standing hold, after picture acceptance |
| generated ambience that is muddy or fights the stems | mute it and use the rain, thunder, and Foley stems | final composite |
| sidecar subtitle track, proposed English, off by default | delivery metadata; never burned into the picture | delivery packaging |
| endpoint mismatch or discontinuous motion | variant selection, repair, re-run with adjusted seed or duration | before extracting the terminal frame |
| Clip 2, the compromise | its own package; starts from this clip's accepted terminal frame | after Clip 1 acceptance |

## Retrieval

Submission returns `{id, status, polling_url}` with status `pending`. Poll `GET https://openrouter.ai/api/v1/videos/{id}` until `completed` or a failure status; the poll response carries `usage.cost`. Download `GET /api/v1/videos/{id}/content?index=0`. Verify the container locally (duration, dimensions, track presence) before any viewing claim, and preserve every response.

## Unresolved on this surface

- whether `seed` produces deterministic repeats: unverified;
- default watermark behavior and what the `watermark` passthrough changes: unobserved; the operator reported no watermark across seven viewed outputs;
- prompt rewriting: no rewritten prompt has been returned in any response; treat rewrite behavior as unobserved rather than absent;
- one status-latency anomaly is on record: the dashboard reportedly showed completed while the API still returned pending for a job; which row was seen is unconfirmed.

## Preflight

- confirm both frame files' hashes against `../media/media-log.md`;
- build the request from `request-body.template.json`, inserting the prompt file verbatim and both data URLs;
- record the request as sent, minus the base64 payloads, alongside the run;
- create the result-log entry before submission and preserve every returned variant and response.

Evidence state: surface facts observed directly on 2026-08-04. This package's own submission is recorded in `result-log.md`.

---

<!-- Canonical artifact: examples/storm-watch/seedance20-first-last/post-production.md -->

# Post-Production and Alternate-Path Plan

Applies to the Clip 1 invitation pass. Every requirement routed out of the picture pass lands here with a concrete rejoin point.

## Dialogue

- line: one word, Japanese, proposed canon 「大丈夫」, low, almost under the thunder; single-word speech stage, nothing added around it;
- speaker: Iven; his back is to the camera for the entire clip, so there is no on-screen mouth to sync and no lip-performance risk;
- route: approved voice recording laid over the standing hold, after the thunderclap and before the POV's blanket lift; exact placement is a mix decision inside that window;
- the picture pass excludes speech (`submitted-text.txt`), so generated audio cannot collide with the approved voice;
- rejoin: after a picture variant is accepted, before the final mix.

## Generated-audio review

`generate_audio` runs in the picture pass. Treat the returned track as a candidate ambience stem only:

- keep it when the rain reads naturally, the thunderclap lands near the jolt, no speech or music is present, and the pats are either present or cleanly absent;
- mute it and use the stems below when it is muddy, mistimed, carries speech or music, or fights the recorded word.

## Stems and Foley

- steady rain bed, loopable, low-frequency-controlled so the word sits above it;
- one close thunderclap aligned to the opening jolt; a low thunder roll under the middle for the ear choreography to track;
- blanket lift, two soft mattress pats, matched to the POV hand's on-screen timing;
- no music.

## Subtitles

- default off; nothing burned into the picture;
- one sidecar track, proposed language English, carrying the single caption for the word and optional atmospherics; prepared at delivery packaging, not in the picture pass.

## Repair and alternate paths

- endpoint drift at the last frame: prefer variant selection; then a re-run with adjusted seed or 9-10 s duration; do not add corrective prose that contradicts the supplied frames;
- unwanted motion (a step, torso turn): reject the variant; if persistent across seeds, re-anchor with a closer end frame;
- pat timing unusable for Foley: cut Foley to picture rather than re-running for sound alone.

## Finishing and continuity

- grade: keep the lamp warm and dominant; do not lift the window exposure;
- after acceptance and the mix, extract the actual terminal frame from the finished composite; that frame, inspected, is Clip 2's opening evidence;
- archive: exact request, all returned variants, accepted composite, extracted frame, and the updated result log.

---

<!-- Canonical artifact: examples/storm-watch/seedance20-first-last/result-log.md -->

# Storm Watch · Seedance 2.0 First/Last Frame · Run Review

Run status: run. Take 1 completed on 2026-08-04; machine-side verification is done, and the operator's viewing decides acceptance.

## Exact submission

- take 1 submitted: 2026-08-04 13:17:42 UTC (22:17:42 JST); status `pending` on acceptance;
- job id: `b00ddyOO3QfCL6UGKFTK`;
- request: exactly `request-body.template.json` with the placeholders filled: `submitted-text.txt` verbatim (sha256 first 16 `5d637d0e726a7999`, 1,432 bytes) and the two jpeg data URLs whose source hashes match `../media/media-log.md` (`949cdc8b6acff07d`, `3d21c3b0e335a955`);
- settings as sent: 720p, 16:9, 8 s, seed 21, `generate_audio` true;
- raw submit/poll responses and the downloaded video are preserved outside the repository under `production-media/storm-watch-clip1/`.

## Returned variants

| Take | Variant | Returned metadata verified locally | Cost (`usage.cost`) | Complete file preserved? |
|---|---|---|---|---|
| 1 | 1 | 8.058 s, 1280x720, video and audio tracks present, 2,713,371 bytes | $1.2096 | yes, outside the repository |

Timing: completion first observed by polling at 13:29:22 UTC, about 11.7 minutes after submission. With the same-day observations of 21.5 and 60.5 minutes, the queue spread on this surface now spans roughly 12 to 60 minutes for identical settings. The cost matched the `video_tokens` arithmetic exactly.

## Direct observations

The operator viewed take 1, variant 1. The assistant decoded nothing; container metadata above is the only machine-side observation.

- Required criteria: all met, per the operator. One continuous first-person shot with no cut, teleport, or morph; he neither walks nor turns; the sleepwear stays folded in the two-handed carry; the POV hand owns the blanket lift and pats; the ears respond to the thunder first; the audio contains no speech and no music; the end state is stable.
- Flexible items recorded: lightning is present. The generated audio carries no rain bed; the storm ambience is absent. Whether the thunderclap landed in the audio was not separately reported and does not change the routing below.

## Accepted variant and continuation

User decision: take 1, variant 1 accepted for picture. The generated audio is rejected as an ambience candidate because the rain bed is absent; per `post-production.md` it is muted, the rain, thunder, and Foley stems carry the sound, and the word is laid over the standing hold.

Criteria waived: none. The storm bed's required carrier was always the post stems, with the in-pass audio as a candidate attempt; the designed fallback fired, and the requirement survives on its alternate path.

Repair/post-production required: audio replacement per plan; no picture repair.

Finished endpoint: the accepted terminal frame was extracted locally (ffmpeg 9.0, 0.1 s before end of stream) and inspected; it is `../media/clip2-start.png` (sha256 first 16 `7fb8dd33518ba731`, 1280×720). Supplementary frame-level verification by the assistant from extracted stills: at mid-clip the POV hand grips the lifting blanket corner, confirming the invitation's ownership, and the terminal state matches the end anchor with mild blanket-geometry drift, recorded in `../frame-inspection.md`. Clip 2's gate is open.

# Clip 2 · The Compromise

Run status: submitted, awaiting completion.

## Exact submission

- take 1 submitted: 2026-08-04 14:22:38 UTC (23:22:38 JST); status `pending` on acceptance;
- job id: `WnR2D3GJcDUBUfl0HM6D`;
- operation: first/last-frame generation. `first_frame` is the real extracted Clip 1 terminal frame `../media/clip2-start.png` (`7fb8dd33518ba731`, png); `last_frame` is the planned compromise anchor `../media/clip2-end.png` (`b23955c4ec3a8284`, png); primary text `clip2-submitted-text.txt` (sha256 first 16 `2fe100284bd13626`, 1,449 bytes);
- settings: 720p, 16:9, duration 10 s (lengthened from 8 because this clip carries the episode's largest pose change; the field study's run 4 showed the seam risk of widely separated anchors, and duration is one of its recorded mitigations), seed 22, `generate_audio` true;
- expected cost by the token arithmetic: 21,600 video tokens/s × 10 s × $0.000007 = $1.512;
- raw responses and the video are preserved outside the repository under `production-media/storm-watch-clip2/`.

## Returned variants

| Take | Variant | Returned metadata verified locally | Cost (`usage.cost`) | Complete file preserved? |
|---|---|---|---|---|
| 1 | 1 | 10.055 s, 1280x720, video and audio tracks present, 3,964,133 bytes | $1.512 | yes, outside the repository |

Completion first observed by polling at 14:52:07 UTC, about 29.5 minutes after submission. The cost matched the `video_tokens` arithmetic exactly for the second time (216,000 tokens at $0.000007).

## Direct observations

Assistant frame-level observations from extracted stills (supplementary; motion and audio are the operator's):

- t≈4 s: a genuine mid-lowering pose exists: knees deeply bent, hips descending to the mattress edge, tail swinging over the bed, sleepwear still in hand. This is the intermediate articulation whose absence defined the field study's run 4 seam;
- t≈5 s: seated on the edge, weight compressing the bedding, handling the sleepwear;
- t≈7 s: leaning slightly and placing the sleepwear on the bedding beside the pillow position;
- terminal: seated upright facing the window, hands at rest on his thighs, the folded sleepwear lying flat beside the pillow, the tail resting across the bedding at his side, digitigrade feet on the floor, room and lighting held. Mild drift from the planned end anchor in seat position and tail sweep, recorded;
- during the descent the head transitionally faces left rather than the window; the seated states before and after face the window.

Operator viewing, first report: the bed sits lower-right; the character keeps his back to the viewer throughout; he moves to the bed rear-facing, sits, and, still without looking at the viewer, places the sleepwear with his left hand. The one-handed placement deviates from the prompt's "releasing it with both hands"; the required outcome, the sleepwear ending beside the pillow and out of his hands, is met, so this is recorded as accepted variation unless the operator objects. The rear-facing approach is the never-turn constraint expressing itself in motion.

Operator, second report: `clip1-take1.mp4` and `clip2-take1.mp4` watched in sequence read as one continuous piece. This clears the named seam risk at the sit, and more: the clip boundary itself reads seamless, so the sequential-finalization loop (render, accept, extract the real terminal frame, open the next clip from it) held end to end on its first real use.

Operator, third report: Clip 2's picture is very slightly stretched horizontally.

Machine-side audio measurement (ffmpeg volumedetect): clip 1 mean -22.3 dB, max -2.0 dB; clip 2 mean -33.1 dB, max -5.5 dB. Both tracks carry real content. Clip 1's content therefore excludes rain (operator report) and speech and music (required checks) while being far from silent; what it does contain has not been described. Clip 2's audio content is not yet described.

Aspect hypothesis, recorded as hypothesis and not established: Clip 2 mixed input dimensions, a 1280×720 extracted `first_frame` against a 1376×768 generated `last_frame` (aspect difference 0.78%), while Clip 1's two inputs shared 1376×768. Scoped mitigation for any retake and for all future submissions: conform every boundary image to the delivery resolution before submission. Post route: a sub-percent horizontal correction in the finishing pass.

Operator, fourth report: Clip 2's generated audio content is rain.

Audio consequence: the two takes split on the same kind of request. Clip 1's track carried substantial non-rain content; Clip 2's carried rain. No tendency about rain delivery on this surface is recordable from a 1-of-2 split, and none is recorded. Routing stays per `post-production.md`: the stems carry the episode-wide rain bed, because the brief requires rain continuous across the join and Clip 1's track has none; Clip 2's generated rain is a candidate to blend at the mix.

User decision on take 1: reject for the horizontal stretch; retake with conformed media. Take 1's continuity findings stand as observations: the sit is continuous, the clip join reads seamless, the causal order and end state are correct. The retake changes exactly one variable.

## Take 2

- submitted: 2026-08-04 15:12:30 UTC (2026-08-05 00:12:30 JST); job id `W0208XQJSNeWtwbbj5V0`;
- single variable against take 1: the `last_frame` is the conformed 1280×720 anchor (`376d3fa0aae506c0`), so both boundary images now share the delivery resolution. Prompt (`2fe100284bd13626`), seed 22, duration 10 s, and all other settings identical to take 1;
- purpose: remove the mixed-dimension input hypothesized to cause the stretch, while maximizing the chance of reproducing take 1's accepted motion.

Returned variants:

| Take | Variant | Returned metadata verified locally | Cost (`usage.cost`) | Complete file preserved? |
|---|---|---|---|---|
| 2 | 1 | 10.055 s, 1280x720, video and audio tracks present, 3,865,678 bytes | $1.512 | removed in local cleanup after rejection; extracted stills remain outside the repository |

Completion observed about 6 minutes after submission; the same-day queue spread for identical settings now spans roughly 6 to 60 minutes. The cost matched the token arithmetic for the third time. Audio track content present (mean -32.3 dB, max -7.1 dB), content pending the operator's ear.

Assistant frame-level observations: the mid-lowering articulation at t≈4 s is reproduced under the same seed and prompt, and the terminal state lands on the conformed anchor: seated facing the window, hands at rest, sleepwear folded beside the pillow, tail across the bedding, room and lighting held. Whether the horizontal stretch is gone is not resolvable at the assistant's eye and belongs to the operator.

Operator viewing: the aspect ratio is correct now, and take 2 is slightly more zoomed than take 1, enough that the clip join is perceptible.

Diagnosis recorded: conforming the anchor's resolution fixed the aspect but could not fix what the anchor never had, framing agreement with the real opening. The end anchor was generated from the Clip 1 start frame before the terminal frame existed, so its field of view was free; in take 1 the mismatch expressed as stretch, in take 2 as a zoom offset visible at the join. The full sequential-finalization rule follows: a continuation clip's end anchor is derived from the extracted terminal frame itself, camera and framing inherited, only the staged change applied.

User decision on take 2: reject for the join-visible zoom offset. Take 3 follows with the re-derived anchor as the single changed variable.

## Take 3

- anchor re-derived: `../media/clip2-end.png` is now an edit of the real terminal frame (camera and field of view inherited; the first derivation attempt stripped his robe and was rejected; the accepted version is conformed by direct scale, `7b90d46f3552e057`); prompt, seed 22, and 10 s unchanged;
- submission attempted 2026-08-04 15:31:59 UTC: rejected by the surface with HTTP 402, insufficient OpenRouter credits, before any job was created. No charge occurred;
- resubmitted unchanged after the operator's top-up, 2026-08-04 15:39:03 UTC: accepted, job id `7w30dA5TEech6xt6mo0u`.

Returned variants:

| Take | Variant | Returned metadata verified locally | Cost (`usage.cost`) | Complete file preserved? |
|---|---|---|---|---|
| 3 | 1 | 10.055 s, 1280x720, video and audio tracks present, 3,259,846 bytes | $1.512 | yes, outside the repository |

Completion observed about 4.6 minutes after submission. Audio content present (mean -29.4 dB, max -4.4 dB), content pending the operator's ear.

Assistant frame-level observations: the opening frame's framing closely matches the Clip 1 terminal frame at still level, with no zoom offset apparent, which is what the terminal-derived anchor was for; the terminal frame lands on the re-derived anchor: robed upright seat facing the window, hand at rest on the thigh, digitigrade feet on the floor, sleepwear folded beside the pillow, tail across the bedding, room and framing held.

Operator viewing: aspect correct; a residual zoom offset against Clip 1 remained perceptible at the join, smaller than take 2's. Diagnosis: the offset is generation re-synthesis drift, measured at a constant 2.1-2.3% center zoom with zero translation at both ends of the clip; input-side fixes had reached their floor, and the remainder belongs to the edit.

## Join, finishing, and episode master

- geometric registration: a constant 2.2% zoom-in conform on Clip 1 registers the join; measured residual across the finished cut is 0.1-0.2% with zero shift;
- the cut is masked as a diegetic lightning flash calibrated to the scene's own flash grammar, measured from Clip 1's real in-picture lightning: a double pulse, +47% peak luminance, three-to-four-frame decay, the window blowing out inside its measured trim bounds while the lamp's warmth holds. A four-frame picture crossfade and a matching audio crossfade run underneath. Earlier drafts that lifted the whole room flat and over the in-scene reference intensity were rejected by the operator and superseded;
- audio assembly: Clip 2's generated rain, the one track the operator confirmed as rain, runs as the episode-wide bed; Clip 1's generated track is mixed above it for the first half; rain crossfades into rain at the join; a limiter caps at -0.9 dBFS. Master levels: mean -25.9 dB, max -3.4 dB;
- episode master: `production-media/storm-watch-episode/episode-master.mp4`, 17.917 s, 1280x720, video identical to the verified join build;
- continuity landing: the master's final frame is extracted and stored as `../media/episode-continuity-frame.png`; the next episode opens from that real frame;
- prepared sidecar: `subtitles-en.srt`, one caption, off by default, timed to the standing hold where the word lands;
- closure state: verified by measurement and frame inspection on the assistant's side; the operator's veto stands open. The two items that remain the owner's by nature: the voice for the single word 「大丈夫」 (casting is canon), and final acceptance of the assembled master.

The named risk is the seam at the sit; the acceptance criteria for the walk-turn-sit, the sleepwear release beside the pillow, and the tail settle follow the Clip 2 shot proposition in `../phase-a-plan.md`.

---

## Literal field file: `examples/storm-watch/runway-gen45-i2v/submitted-text.txt`

```text
A close thunderclap causes one small first-person jolt. The guardian's ears angle toward the rainy rear-right window before his head follows. Keeping the folded shirt supported in both hands, he takes one measured step to the left mattress edge and lowers his weight into a seated position. The mattress edge compresses under him and pulls one bedding fold inward; his loose sleeves and the folded fabric settle after his torso. Rain continues at the window. He returns his gaze to the POV and holds the final pose as the camera settles level at pillow height, all in one continuous shot.
```

---

## Literal field file: `examples/storm-watch/veo31-first-last/submitted-text.txt`

```text
Connect the supplied first and last frames with one physically continuous first-person action. A close thunderclap causes one small camera-body jolt as the guardian's ears turn toward the rainy rear-right window before his head follows. Without changing his two-handed support of the folded shirt, he takes the short step to the mattress, bends through hips and knees, and lowers into the supplied seated pose. His weight creates the visible mattress dip before his torso settles; his loose sleeves and the folded fabric come to rest last. His gaze returns to the POV as the camera finishes level at pillow height.
```

---

## Literal field file: `examples/storm-watch/veo31-first-last/negative-prompt.txt`

```text
selfie view, reverse angle, visible camera wearer, mirror reflection, extra people, duplicate limbs, text overlays, hard cut, teleportation
```

---

## Literal field file: `examples/storm-watch/veo31-first-last/request-body.template.json`

```json
{
  "instances": [
    {
      "prompt": "${CONTENTS_OF_SUBMITTED_TEXT}",
      "image": {
        "gcsUri": "${GCS_URI_FOR_START_FRAME}",
        "mimeType": "image/png"
      },
      "lastFrame": {
        "gcsUri": "${GCS_URI_FOR_END_FRAME}",
        "mimeType": "image/png"
      }
    }
  ],
  "parameters": {
    "aspectRatio": "16:9",
    "durationSeconds": 8,
    "sampleCount": 4,
    "resolution": "720p",
    "negativePrompt": "${CONTENTS_OF_NEGATIVE_PROMPT}",
    "storageUri": "${OUTPUT_STORAGE_URI}"
  }
}
```

---

## Literal field file: `examples/storm-watch/seedance20-first-last/submitted-text.txt`

```text
One continuous first-person shot between the supplied first and last frames, photographic grounded clean realism matching both frames.

A close thunderclap opens the shot and causes one small camera-body jolt at pillow height. The standing wolf guardian is already on watch at the bedside, back to the camera, facing the rainy rear-right window; he does not startle. His upright ears turn with the rolling thunder while his body and feet stay planted, and he keeps the folded dark teal sleepwear supported in both hands at his waist the whole time.

Then the viewer's own hand at the lower edge lifts the near corner of the blanket a hand's width and pats the exposed mattress twice, softly. In response his head turns a few degrees toward the bed, his near ear swivels back toward the mattress while the far ear stays on the window, and his tail lifts slightly, reaching the supplied last frame exactly. His torso does not turn, he takes no step, and the sleepwear never leaves his two-handed grip.

Sound: steady rain throughout; one close thunderclap with the opening jolt; a soft blanket lift and two quiet mattress pats; low rolling thunder under the middle. No speech. No music.

No cut. No reverse angle. No selfie view. No visible camera wearer. No mirror. No extra person. No duplicate limbs. No text overlay. No teleportation. No morphing. The room, the lamp, the window, and the camera relation stay exactly as supplied.
```

---

## Literal field file: `examples/storm-watch/seedance20-first-last/clip2-submitted-text.txt`

```text
One continuous first-person shot between the supplied first and last frames, photographic grounded clean realism matching both frames.

The standing wolf guardian accepts a silent invitation. After a held beat, he takes one short step along the bedside and, with a quarter turn of his hips, lowers himself through bending knees to sit on the left edge of the mattress, still facing the rainy rear-right window, never turning toward the camera. His weight presses a visible dip into the bedding as he settles. Seated upright, he leans slightly and places the folded dark teal sleepwear on the bedding beside the viewer's pillow at the lower edge, releasing it with both hands, then rests his hands on his thighs. Last, his full plumed tail sweeps to his side and comes to rest across the blanket over the viewer's covered legs, pressing the fabric where it lies. His ears stay toward the window and his back stays upright the whole time.

The viewer's hand rests at the near bedding edge and does not move.

Sound: steady rain throughout; soft digitigrade footfalls on wood; quiet mattress compression and cloth settle; the faint slide of the tail over the blanket. No speech. No music. No thunderclap.

No cut. No reverse angle. No selfie view. No visible camera wearer. No mirror. No extra person. No duplicate limbs. No text overlay. No teleportation. No morphing. The room, the lamp, the window, and the camera relation stay exactly as supplied.
```

---

## Literal field file: `examples/storm-watch/seedance20-first-last/request-body.template.json`

```json
{
  "model": "bytedance/seedance-2.0",
  "prompt": "<insert the verbatim contents of submitted-text.txt>",
  "frame_images": [
    {
      "type": "image_url",
      "image_url": { "url": "data:image/jpeg;base64,<base64 of ../media/clip1-start.jpg>" },
      "frame_type": "first_frame"
    },
    {
      "type": "image_url",
      "image_url": { "url": "data:image/jpeg;base64,<base64 of ../media/clip1-end.jpg>" },
      "frame_type": "last_frame"
    }
  ],
  "aspect_ratio": "16:9",
  "duration": 8,
  "resolution": "720p",
  "seed": 21,
  "generate_audio": true
}
```

---

## Literal field file: `examples/storm-watch/seedance20-first-last/subtitles-en.srt`

```text
1
00:00:01,700 --> 00:00:03,000
It's all right.
```
