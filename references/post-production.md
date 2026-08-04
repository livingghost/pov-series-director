# Post-Production, Clip Joins, and Finishing

Finishing sits between the accepted picture and the continuity extraction. The order is fixed: accept the picture, finish it (join, repair, grade, mix), and only then extract the terminal frame that seeds the next clip or episode. A frame extracted before finishing can be invalidated by it.

Every boundary between clips is either a **continuity join** (story time continuous; the boundary must read as one unbroken take) or a **scene transition** (time or place changes; the boundary uses transition grammar on purpose). The choice is made during clip packing, not discovered in the edit.

## 1. Inputs from the rest of the procedure

- `structure-music.md` §7 names each boundary's bridge at packing time: `action`, `audio`, `occlusion`, `eyeline`, `light`, or `continuation-input`, with outgoing and incoming anchors recorded, and treats `generated-transition` as an operation-backed bridge of its own. This reference does not rename that taxonomy; it finishes those bridges in the edit.
- A seam that asks the generator to perform motion inherits the motion-risk heuristics in `pov-camera.md` §9: a blink is moderate risk, a fast whip higher. Choosing a seam is also choosing a generation risk, so the choice is written into both clips' endpoint direction, not improvised at the cut.
- Dialogue, subtitle, and localization routes follow `dialogue-rules.md`; light and sound wording follows `atmosphere-quality.md`. The plan and record artifacts are defined in `templates.md` §9 and §10.

## 2. What separately generated clips do not promise

Verify per target surface, and record in `production-state.md`, whether the surface replays a supplied anchor frame or re-synthesizes it; do not assume either. Re-synthesis commonly shifts framing by a small near-constant amount and always repaints texture: fur, cloth, rain, grain, and noise re-render, so even a geometrically perfect cut can show a surface pop. Audio restarts rather than continues. Pixel continuity across independent generations is therefore an editing deliverable, and the join is planned before the clips are rendered: choose boundary poses, camera state, and a match point (matching scale, position, and shape across the boundary) at packing time, exactly as a match cut is planned at a shoot.

## 3. Finishing a continuity join

In order of preference:

1. **Execute the designed bridge.** When packing placed a maskable event on the boundary, cut inside it. The single-take tradition supplies placements per bridge type:
   - `eyeline`: a **blink**; in first-person work the camera is a character's vision, so a two-to-four-frame lid close over the boundary reads as thought punctuation, not as an edit;
   - `action`: a **whip** on a head turn, exiting one clip in fast rotation and entering the next in the same direction and speed, cut inside the heaviest blur;
   - `occlusion`: a **natural wipe**, a hand, held object, passing figure, or door frame filling the lens for a beat, cut on the covered frames;
   - `light`: a **dark or blown passage**, an unlit doorway, a light burst, steam or spray filling the frame;
   - a stylized rupture (glitch, static) only when the fiction itself supports it.
2. **Registered cut.** For a `continuation-input` bridge that must read as one take, conform one clip onto the other per §5 and cut hard.
3. **Masked cut.** Cover a registered cut's residual pop with a brief added scene event, calibrated per §6, usually over a short crossfade.
4. **Soft or morph cut.** A crossfade of a few frames dissolves texture repaint and is invisible on near-still poses; on fast motion it ghosts. Optical-flow morph transitions, where the toolchain offers them, interpolate small pose differences and suit locked-camera boundaries; inspect their output for warping before accepting.
5. **Unify layer, under every option above.** Match grade first (white balance, exposure, saturation between the two sides; an exposure jump exposes a cut on its own), then lay one shared fine grain or noise plate across both sides so the two generations stop disagreeing at the texture level. This edit-layer texture is not the prompt-side degraded-look vocabulary excluded for clean realism by `lexicon.md` §2; it stays fine, uniform, and subordinate to the delivery grade.

A boundary plan line in the post plan reads like:

```text
boundary: clip 2 → clip 3 · continuity join
bridge: occlusion (his sleeve crosses the lens as he reaches past the camera)
finish: cut on the covered frames; shared grain; rain bed continuous; kettle sound J-cut into clip 3
fallback: registered cut with a masked lamp flicker
```

## 4. Scene transitions

Transitions are vocabulary, not failure. The standing grammar: a hard cut with the audio bridging it; a dissolve for the passage of time; a fade to black for a chapter break; a match cut on shape, action, or sound to bind two places or times. First-person work adds its own: blink-to-black, falling asleep, and the eyes-opening reveal that a pillow-height series naturally opens episodes with; `pov-camera.md` §1 treats the blink as a small time skip in exactly this sense. Segment roles in `structure-music.md` §3 decide where hooks and quiet settles belong. A transition that exists to hide a production problem is a continuity join wearing the wrong label.

## 5. Conform and registration rules

- Conform every boundary image to the delivery resolution before submission; never mix dimensions in one request.
- Derive a continuation clip's endpoint anchors from extracted real frames, so camera and framing are inherited rather than re-invented; an anchor drawn before the real frame existed will disagree with it.
- Register to what the viewer last saw: the delivered frames of the preceding clip are the reference, never the submitted anchors.
- Measure or judge drift at both ends of the clip. Constant drift takes one constant transform; animate a correction only when the drift itself changes over the clip.
- Correct on the side whose other end is free, and prefer the zoom-in direction: zooming in crops safely, zooming out invents borders.

## 6. Masked-event calibration

An added flash, flicker, shadow, or passing light must be calibrated to the scene's own event grammar, never to taste:

- find the same class of event inside the delivered footage and imitate its observed intensity, envelope, and rhythm: attack, decay, single or double pulse;
- light the source first, per the source-and-landing rule in `atmosphere-quality.md` §3: the window, doorway, screen, or lamp region carries the strong change within its real edges, the room receives subordinate spill in the source's color temperature, and other practicals keep their own color;
- never exceed the scene's own reference event: a mask brighter than the storm it claims to be reads as an edit;
- keep transients transient: a handful of frames with decay, not a plateau.

## 7. Audio finishing

- **Split edits are the default at boundaries.** Let sound lead the picture into the next clip (J-cut) or trail over it (L-cut); a simultaneous audio-and-picture cut is the exception that must earn its abruptness.
- **The bed bridges every cut.** A continuous ambience or room-tone bed is the mortar between clips; without it, every edit is audible even when invisible. Harvest beds from whichever pass produced usable ambience, including one clip's generated track extended under its neighbors; stationary textures such as rain or room hum loop and restart inaudibly.
- Generated audio is a candidate stem, never the authority; judge each clip's track separately, since identical requests can return different contents. The ambient bed, turn effect, and closing sound named in `structure-music.md` §4 are the requirements the mix must land.
- Dialogue laid in post goes over a stable hold per `dialogue-rules.md`; a speaker facing away from camera removes lip-sync risk entirely and is worth choosing at the directing stage.
- Mix to the destination's loudness spec and name it in the plan: commonly about -14 LUFS integrated for streaming platforms, -16 for podcast norms, -23 LUFS under EBU R128 for European broadcast, true peak at or below -1 dBTP; verify the actual destination before mastering, and cap with a limiter so summed beds cannot clip.

## 8. Repair menu

Within the accepted picture, standard editorial repairs that need no regeneration, filling the picture-repair fields of the plan in `templates.md` §9: a small constant reframe inside the delivery raster; a retime of a beat whose physics read too fast or slow; stabilization of an unwanted wobble; a freeze or micro-extension giving a hold room for dialogue; paint-out of a small persistent artifact. Each repair is recorded with the same specificity as a submission, and any repair that moves pixels happens before the terminal frame is extracted.

## 9. Verifying the join

Before human review, verify what can be verified without eyes: compare boundary frames across every join for scale, shift, and content agreement; check duration, dimensions, track presence, and measured loudness. Human viewing then judges only what measurement cannot: whether motion reads continuous, whether the seam or mask belongs to the scene, whether the result is acceptable. A geometry or level defect a viewer catches that a measurement would have caught first is a process failure, not a viewing task.

## 10. Plan and record

The plan artifact is `templates.md` §9 and states, before the run: the boundary type and bridge for every clip boundary with its finishing choice and fallback, the dialogue route and window, the stems and their authority order, the grade and grain intent, the loudness target, the repair routes, and the rejoin point of every requirement routed here. After finishing, the run review (`templates.md` §10) records what was actually done with the same specificity as the submission itself: the conform applied, the seam or mask used and its calibration source, the bed's origin, the repairs, and the measured levels.
