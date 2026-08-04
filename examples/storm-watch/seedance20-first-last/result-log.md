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
