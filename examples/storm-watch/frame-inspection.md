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
