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
