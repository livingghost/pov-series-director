# Real Run Record

Run status: run. Five submissions were executed against one surface on 2026-08-04.

This is a controlled comparison, not a single run. The beat is the `Storm Watch` stand-to-sit from `examples/storm-watch/`. What changed across submissions was the media supplied and the parameter that received it. Everything else that could be held fixed was held fixed.

## Identity

Run ID: 2026-08-04-seedance20-openrouter

Date/time and timezone: 2026-08-04, UTC

Operator: repository owner, with the submissions issued from a local shell

Product/editor/API as shown: OpenRouter, `POST https://openrouter.ai/api/v1/videos`, polled at the returned `polling_url`

Model/version as shown: `bytedance/seedance-2.0`, canonical slug `bytedance/seedance-2.0-20260414`

Operation selected: varied by submission; see the table below

Documentation or direct-surface evidence: OpenRouter video-generation docs checked 2026-08-04 for the `frame_images` and `input_references` distinction and the request/response shape. The surface reported every result itself; nothing here is inferred from a vendor claim.

This surface is **not** the one recorded in `examples/storm-watch/seedance20-first-last/submission-sheet.md`, which documents BytePlus ModelArk. The request keys differ (`frame_images[].frame_type` here against `content[].role` there), the endpoint differs, and `camera_fixed` and `watermark` do not exist here. These runs therefore do not validate that sheet.

## Exact submission

Director package path: `examples/storm-watch/seedance20-first-last/director-package.md` for the beat; the submissions deviate from it as recorded below

Submission sheet path: none. No sheet existed for this surface when the runs were made.

Input file paths and hashes:

| Used by | File | sha256 (first 16) | Bytes |
|---|---|---|---|
| runs 1-3 | `examples/storm-watch/seedance20-first-last/inputs/start-frame.png` | `4c87b7688d46222e` | 12,098 |
| runs 1-3 | `examples/storm-watch/seedance20-first-last/inputs/end-frame.png` | `b8bb6a95729d8237` | 12,752 |
| run 4 | `inputs/start-frame.png` | `b8639a287704f6a3` | 1,769,560 |
| run 4 | `inputs/end-frame.png` | `69a30a21395e8fbf` | 1,575,351 |
| run 5 | none | | |

The run-1-to-3 files are the repository's schematic teaching frames. The run-4 files were generated for this study and are preserved here. They do not satisfy `examples/storm-watch/media-briefs/`: the folded teal shirt is absent, so the prop-ownership spine of the beat could not be exercised.

Primary submitted-text paths and hashes:

| Run | File | sha256 (first 16) | Bytes |
|---|---|---|---|
| 1 | `prompts/run1-submitted-text.txt` | `6a37a8340a3b54c0` | 982 |
| 2 | `prompts/run2-submitted-text.txt` | `4fa7e06f4ab75447` | 1,867 |
| 3 | `prompts/run3-submitted-text.txt` | `6c12f2dd4c2cbf41` | 1,871 |
| 4 | `prompts/run4-submitted-text.txt` | `aa3403341ed4f9ac` | 1,475 |
| 5 | `prompts/run5-submitted-text.txt` | `844324d4a750992e` | 1,676 |

Other field-text paths and hashes: none. This surface documents no separate exclusion field, so every exclusion was written into the primary text as one negation per artifact.

Settings, identical across all five: `aspect_ratio` 16:9, `duration` 8, `resolution` 720p, `seed` 11, `generate_audio` true.

Service-returned rewritten prompt, when available: none returned.

UI/operator edits after package creation: the submitted text was revised per run as recorded in the table below.

## Submissions

| Run | Media supplied | Parameter | Prompt change from the previous run | Job ID | Cost |
|---|---|---|---|---|---|
| 1 | schematic start and end | `frame_images` | baseline: action and sound only | `xyH8BexUInYhaaYl36Wv` | $1.2096 |
| 2 | schematic start and end | `frame_images` | added that the frames are layout diagrams, added the realism style, added identity facts, excluded diagram/vector/outline/illustration/cartoon | `yzF1E85gKywTjdHJIYD9` | $1.2096 |
| 3 | schematic start and end | `input_references` | first paragraph only, to match the changed role of the images | `OnWddxyfqHcuTqkwzstG` | $1.2096 |
| 4 | production-style start and end | `frame_images` | revised to match the media: shirt clauses removed, sleeves kept | `Mq085MdLmHBB4Q6eRqIO` | $1.2096 |
| 5 | none | none | style and identity moved into prose, since nothing else could carry them | `UNnmamS5YrGQiKERO8hs` | $1.2096 |

Total observed cost: $6.048. The model page listed $0.06726 per second, which predicts about $0.54 for eight seconds. Every run billed $1.2096. The listed rate did not predict the charge, and the reason is unverified.

## Creative requirements declared before viewing

| Requirement | Carrier used | Required/flexible | Observable acceptance |
|---|---|---|---|
| grounded clean realism | supplied media in runs 1-4, prose in run 5 | required | output is photographic, not diagrammatic |
| Iven's species, build, fur, and brow scar | supplied media in runs 1-4, prose in run 5 | required | the character matches the established design |
| room, lamp, window, and camera relation | supplied media in runs 1-4, prose in run 5 | required | the same room is recognizable |
| continuous stand-to-sit with no cut | prose in all runs | required | no cut, no teleport, no morph at the contact |
| rain, one thunderclap, contact sound | `generate_audio` in all runs | flexible | an audio track exists and does not carry speech |

## Returned variants

| Run | Variant | Returned metadata verified locally | Complete file preserved? |
|---|---|---|---|
| 1 | 1 | 8.058 s, 1280x720, video and audio tracks present | yes, outside the repository |
| 2 | 1 | 8.058 s, 1280x720, video and audio tracks present | yes, outside the repository |
| 3 | 1 | 8.058 s, 1280x720, video and audio tracks present | yes, outside the repository |
| 4 | 1 | 8.058 s, 1280x720, video and audio tracks present | yes, outside the repository |
| 5 | 1 | 8.058 s, 1280x720, video and audio tracks present | yes, outside the repository |

Every submission returned exactly one output. The duration, dimensions, and track presence above were read from the MP4 container locally and are the only observations made without human eyes.

The video files are deliberately not committed. Runs 1 to 3 would misrepresent the project, and all five are large enough to change the character of the repository.

## Direct observations by run

The operator viewed every output. The assistant viewed none of them, and has no ability to decode video here. Every statement in this section is the operator's, recorded verbatim in substance.

### Runs 1, 2, and 3

Output was the supplied schematic diagram in motion. Run 2 was indistinguishable from run 1 despite the prompt stating that the frames were layout diagrams, requesting photographic realism, and excluding diagram, flat vector shapes, outline drawing, illustration, and cartoon. Run 3, which passed the same images through `input_references` instead of `frame_images`, was also indistinguishable.

Accept / reject / repair and reason: reject all three. The output style is not the project style anchor.

### Run 4

Character identity and clothing: correct. The brow scar was present. The robe with loose sleeves was present.

Actual action order: the guardian took his hands out of his pockets and sat down on the bed naturally.

Prop identity and ownership: not exercised. The supplied media had no folded shirt, so the prompt did not direct one.

Unexpected additions, cuts, or artifacts: **at the moment of sitting there was a visible instantaneous switch between the two supplied frames.** The seam was perceptible at the contact.

Accept / reject / repair and reason: reject or repair. The example's own acceptance criteria list "no cut or teleport" as required and list endpoints connected through teleportation or morphing as a reject condition. This symptom meets that condition.

### Run 5

Style: correct. The output was properly generated and realistic.

Character identity: did not match the design used in run 4. The operator described the returned character as resembling a ferret-person rather than the muscular white werewolf.

The submitted description was "a tall guardian with white fur and a narrow scar above his left brow", taken from `source-brief.md`. **That description never states a species, a build, a muzzle shape, ear shape, or musculature.** The operator's point stands: a ferret-person satisfies it. The run did not test whether prose can carry identity, because the prose supplied did not specify identity. It tested what an underspecified description returns.

Accept / reject / repair and reason: reject for series use, but not as evidence against prose. The correct next test is a fully specified character description with no media.

## Accepted variant

User decision: none accepted for production. Runs 1 to 3 fail on style, run 4 fails on the contact seam, run 5 fails on identity.

Criteria waived, if any: the folded shirt and its two-handed ownership were waived for run 4 because the supplied media did not contain the prop. That waiver means run 4 did not test the canonical beat.

Repair/post-production required: not attempted. No variant was carried forward.

## Finished endpoint

Final composite path: none. No run was accepted, so no terminal frame was extracted and no canon was updated.

## Requirement-transfer findings

| Requirement | Carrier | Observed outcome | Smallest next change |
|---|---|---|---|
| grounded clean realism | supplied media | ran 1-3: the supplied schematic style appeared in the output under both image parameters, and five explicit style exclusions did not change it | supply media that already looks the way the shot should look |
| grounded clean realism | prose alone | run 5: realistic output with no media supplied | none; prose was sufficient for style here |
| character identity | supplied media | run 4: correct species, build, fur, and brow scar | none |
| character identity | prose alone | run 5: a different creature. The description carried no species, build, muzzle, ears, or musculature, so this is a property of the description, not a demonstrated limit of prose | specify the character fully, then retest before concluding anything about prose |
| room and camera relation | supplied media | run 4: the room and the light held | none |
| room and camera relation | prose alone | run 5: a room was built from the description. Whether it could match a previous episode was not tested | compare two text-only runs of the same room before concluding |
| continuous stand-to-sit | prose, endpoints anchored | run 4: a perceptible switch at the contact | reduce the pose distance between endpoints, lengthen the duration, or move the landing off the last-frame anchor |
| rain, thunder, contact sound | `generate_audio` | an audio track was returned in every run; its quality was not assessed | assess against the post-production stems before keeping it |

## Narrow conclusion

Five submissions, one variant each, one beat, one surface, one day.

**The model treated every supplied image as a literal appearance, not as a representation of something else.** Runs 1 to 3 asked it, in prose, to read the supplied frames as layout diagrams and render the result photographically, and listed five exclusions against diagrammatic output. It rendered the diagrams in motion all three times, under both `frame_images` and `input_references`. Run 5, which supplied no images, produced realistic output from the same style wording. The style in runs 1 to 3 therefore came from the images, and no prompt wording available to us overrode it.

**Prose carried style. What it does for identity was not tested.** Run 5 got the look right from words alone. It also returned a creature that did not match run 4. The description it was given, taken from `source-brief.md`, names height, fur colour, and one facial scar, and names no species, build, muzzle, ears, or musculature. An unrelated animal satisfies that text. This run therefore measured an underspecified description, and says nothing about what a complete one would do.

That is a finding about the example rather than the model. `source-brief.md` describes a recurring lead without stating what he is, and the gap stayed invisible for as long as media carried the answer.

**Anchoring both endpoints had a cost.** Run 4 was the only run with correct style, correct identity, and a held room, and it was also the only run with a visible seam at the moment of contact. Fixing both ends leaves the model free only in the middle, and the landing was forced.

These statements describe this beat, this model, this surface, and this day. They are not product limits. In particular, nothing here supports a claim about how this model behaves with other kinds of reference media, other durations, or other operations, and the one-variant-per-run design means no statement here has a denominator greater than one.

The repository consequence is recorded separately: the schematic teaching frames under `examples/storm-watch/` are documentation illustrations, and submitting them as endpoint media produces documentation illustrations in motion.
