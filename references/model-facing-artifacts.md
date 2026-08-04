# Model-Facing Artifacts and Creative-Requirement Transfer

A video generator does not receive the whole production process. It receives a particular set of media files, field values, and text on a particular surface. The director package may be much richer than that submission. The job is not to delete the extra knowledge; it is to **carry each creative requirement into the strongest real channel available**.

This document defines the handoff without pretending that natural-language labels are hidden program states.

## 1. Keep five artifacts distinct

### A. Director package

The complete creative and continuity specification. It may contain:

- canon and episode purpose;
- character identity, behavior, dialogue, and performance notes;
- inspected-frame observations;
- spatial blocking and contact geometry;
- sound, atmosphere, music, and localization plans;
- internal asset IDs and lineage;
- intended opening, action path, and landing;
- reasons for target and operation choices;
- acceptance criteria and known uncertainty.

This package exists so useful direction is not lost merely because a single prompt field is small or incapable.

### B. Operation card

A concrete account of what the operator will do on the actual target surface:

```text
Target surface and dated evidence:
Actual operation:
Actual controls or API keys used:
Actual files placed in each control:
Exact settings selected:
What the operation receives from media:
What the prompt must still establish:
What the operation cannot carry:
Alternate production route for unsupported requirements:
```

A name such as `image-to-video` is only a heading. The card is the operative distinction.

### C. Exact field contents

The literal text sent to each model-facing field:

- primary prompt;
- separate negative or exclusion field, when one actually exists;
- dialogue, audio, mask, motion, or edit instruction fields, when separately exposed;
- API request values that influence generation.

Store the exact text in separate files so it can be reproduced and compared with results. Do not reconstruct it later from memory.

### D. Post-production and alternate-path plan

Requirements that cannot be carried reliably in the selected generation pass remain active. Route them deliberately to:

- another generation pass;
- a first- or last-frame asset;
- a subject/character reference;
- an edit, restyle, extension, lip-sync, or performance-transfer operation;
- audio, dialogue, Foley, music, subtitle, or grading post-production;
- a neighboring shot;
- an explicitly accepted area of variation.

The route must say what is created and how it rejoins the episode. “Unsupported” is not permission to erase the requirement.

### E. Run evidence

After generation, preserve:

- exact surface/model/version shown at run time;
- exact submitted files, text, and settings;
- all returned variants, not only the chosen one;
- direct observations against the acceptance criteria;
- extracted first and final frames;
- accepted/rejected decision and reason;
- next submission changes.

A planned result is not run evidence. A documentation-grounded package is not a generated example.

## 2. Use a creative-requirement transfer table

Before final submission, map every consequential requirement from the director package to a real carrier.

| Creative requirement | Why it matters | Strongest available carrier | Exact implementation | Review evidence | If it fails |
|---|---|---|---|---|---|
| Guardian identity and clothing | recurring-character continuity | subject reference, composite start image, or source operand | upload named file to documented control; describe only missing placement/action | compare face, fur, clothing in all variants | strengthen image evidence, composite the frame, or use edit/restyle |
| POV begins at pillow height | spatial continuity | literal first frame | start image shows mattress edge and camera height | compare generated first frames | rebuild start image; do not add more abstract prose |
| Guardian sits while retaining shirt | causal action and prop ownership | start/end frames plus motion prompt, or source performance/edit | exact body path and two-handed grip in prompt; endpoint image where supported | inspect hands, shirt, mattress compression, landing | split action, simplify competing motion, or use performance/edit path |
| Line “Safe.” | character beat | native speech field/pass or audio/lip-sync post | exact line, speaker, timing window, voice direction | listen and inspect speaker/lip sync | preserve picture and route line to audio/lip-sync |
| Rain and thunder | atmosphere and action trigger | source image/video, primary prompt, audio field, or post | rain visible in frame; thunder tied to jolt/ear reaction; ambience mixed separately if needed | inspect/weather and listen | retain visual action; rebuild audio in post |
| No visible POV face | POV rule | framing in start/end/source media and camera path | image composition excludes face; motion never reverses into selfie angle | inspect all frames | redesign framing or crop/edit; a prohibition alone is weak |

A carrier may be a submitted image, source video, exact phrase, separate field, downstream operation, or an accepted uncertainty. “Mentioned in the production record” is not a carrier to the generator.

## 3. Preserve specificity by moving it, not deleting it

Suppose the director package contains this complete beat:

```text
A close thunderclap startles the already-awake POV. The viewpoint jolts once at pillow height. The guardian's ears angle toward the rear-right window before his head follows. He keeps the folded shirt in both hands, takes one measured step to the bed, lowers onto the left mattress edge, and lets his weight compress the mattress. His loose sleeve and the folded fabric settle after his torso. A lightning flash reveals the brow scar. Once still, he looks back to the POV and says softly, “Safe.” Rain remains the ambient bed.
```

A target pass may not carry all of this well at once. A downgrade would delete the ear reaction, fabric lag, mattress response, line, and sound. A proper transfer keeps the whole beat and assigns it:

```text
Start/end images:
- pillow-height room geometry;
- standing and seated endpoints;
- shirt in both hands;
- scar, clothing, window, and light direction.

Primary motion prompt:
- thunder-linked jolt;
- ears before head;
- one measured step;
- lower and sit;
- mattress compression;
- cloth settles last;
- gaze returns to POV.

Audio or post path:
- steady rain ambience;
- thunder at the jolt;
- exact spoken line after the landing.

Review:
- identity, grip, action order, contact feedback, endpoint, speech ownership.
```

Nothing has been made less specific. The specificity has been distributed across real media and production steps.

## 4. Write exact submitted text as a self-contained instruction

Self-contained does not mean “describe everything.” It means every textual reference resolves either to:

- something visible in the submitted media;
- an actual documented target tag/control;
- a noun phrase introduced in the text itself.

Weak target text:

```text
Use C01 and P01. Keep the composition consistent with Image Notes. Follow the approved dimension contract. End in the canonical bridge pose.
```

Those references belong to the director package.

Self-contained image-to-video text:

```text
A close thunderclap causes one small first-person jolt. The white-furred guardian keeps the folded dark shirt in both hands as his ears angle toward the rain-lit window before his head follows. He takes one measured step to the left mattress edge and settles, with the fabric responding after his body stops. The camera returns level at pillow height in one continuous shot.
```

When the submitted start image already makes identity, clothing, room, and composition unmistakable, the text may be shorter and concentrate on change. When it does not, the missing facts must be supplied through another real carrier.

## 5. Internal IDs may remain in operator-facing material

Internal IDs are useful for asset lineage and repeatability:

```text
S01-v3 -> Start image control
C01-v2 -> Subject reference control
V07-r2 -> Source video operand
```

They should remain in the submission sheet. They should not be pasted into the target prompt unless the target itself exposes and documents that exact tag syntax. The issue is not that IDs are forbidden; it is that the generator cannot resolve private bookkeeping names by itself.

## 6. Do not confuse concise prompts with generic prompts

A concise prompt can still contain:

- an initiating cause;
- ordered physical action;
- body mechanics and material response;
- camera-body relation;
- a readable landing;
- one performance detail that changes interpretation.

Generic:

```text
The character walks over and sits cinematically.
```

Concise but directed:

```text
After the thunder, his ears turn first. He takes one measured step without changing his two-handed grip, lowers onto the left mattress edge, and lets the mattress and folded fabric settle after his weight.
```

The second prompt is not longer because of labels. It is stronger because each clause changes what can appear on screen.

## 7. A requirement may be deliberately deferred

Deferral is acceptable when it is explicit and preserves the creative requirement.

Example:

```text
Requirement: exact line “Safe.” in the guardian's canonical voice.
Selected picture-generation pass: silent image-to-video; exact speech behavior unverified.
Decision: generate a stable one-second facial hold after the sit; add the line through the approved voice and lip-sync workflow; carry rain and thunder as separate audio stems.
Acceptance: picture is not final until the line, speaker ownership, timing, and mix are reviewed.
```

This is not a deletion. It is a production route.

## 8. Completion test

A clip package is ready for an operator only when:

1. the full director package still contains the intended story, choreography, performance, sound, and endpoint;
2. every critical requirement has a carrier or an explicit alternate route;
3. the operation card names actual controls and actual files;
4. exact field contents are preserved literally;
5. no exact prompt depends on inaccessible production shorthand;
6. unresolved requirements are visible rather than silently removed;
7. nothing excluded in a negative or exclusion field is also requested in the primary prompt;
8. the result log is either `not run` or contains direct observations from preserved outputs.

Item 7 needs an actual read of both files side by side. A negative field written early and a prompt revised later drift apart quietly: the exclusion still says no camera move while the revised spine now asks for a slow push. The submission then carries two opposed instructions and the result cannot be diagnosed, because either outcome matches something that was submitted.

The point is not to make the prompt sterile. The point is to make the whole production concrete enough that each part can be submitted, generated, edited, or reviewed.
