# Real Run Record

Run status: run. Both submissions were executed on 2026-08-04 and both outputs are downloaded and container-verified. Operator observation is recorded for run A; run B viewing and the A-against-B comparison are pending. The pre-registration below was written before execution and is unchanged.

## Purpose

`examples/storm-watch/source-brief.md` in the working tree currently asserts: "A written description alone has already proved insufficient." The sibling record `../2026-08-04-seedance20-openrouter/run-record.md` does not support that sentence as written. Its run 5 submitted a description that named height, fur colour, and one scar, and no species, build, muzzle, ears, or musculature; the record concludes that the run "measured an underspecified description, and says nothing about what a complete one would do", and names the correct next test: a fully specified character description with no media.

This record is that test. Until it runs and is observed, the brief's sentence is a hypothesis, and the rewritten brief is not committed.

## Identity

Run ID: 2026-08-04-seedance20-openrouter-prose-identity

Date/time and timezone: 2026-08-04, UTC. Run A submitted 11:31:46, run B submitted 11:31:48. Completion first observed by polling at 11:53:16 for run A (about 21.5 minutes) and 12:32:18 for run B (about 60.5 minutes), at 15-30 second polling granularity. Same settings, same day; the queue-time spread is a factor of about three.

Operator: repository owner authorized the spend (about $2.42 for two submissions) and views the outputs; the assistant issues the API submissions from the workspace shell via `submit-and-poll.ps1`, which is preserved in this directory

Product/editor/API as shown: OpenRouter, `POST https://openrouter.ai/api/v1/videos`, polled at the returned `polling_url`

Model/version as shown: `bytedance/seedance-2.0`, canonical slug `bytedance/seedance-2.0-20260414`

Operation selected: text-only generation. No image or video key is present in either request.

Documentation or direct-surface evidence: the same-day surface check recorded in the sibling record, plus this record's own check of the OpenRouter video-generation guide and the OpenRouterTeam skills reference on 2026-08-04: `POST /api/v1/videos` takes top-level `model`, `prompt`, `aspect_ratio`, `duration`, `resolution`, `seed`, `generate_audio`; the submit response carries `id`, `status`, `polling_url`; the poll response carries `status`, `unsigned_urls`, and `usage.cost`; the completed video downloads from `GET /api/v1/videos/{id}/content?index=0`.

## Experimental design

Base submission: run 5 of the sibling record, the only text-only run executed so far on this surface.

Single variable: the Subject paragraph. Everything else in the submitted text is carried over from run 5 verbatim.

Run 5 subject paragraph (underspecified):

> Subject: Iven, a tall guardian with white fur and a narrow scar above his left brow, wearing a dark open robe with loose sleeves over dark trousers.

This record's subject paragraph (complete, taken from the rewritten `source-brief.md` character section):

> Subject: Iven, an adult male anthropomorphic wolf who stands upright on digitigrade legs. He is about two metres tall and heavily built, with visible shoulder and chest mass under short white fur that runs to cream at the throat. He has a long muzzle, upright ears that move independently, yellow eyes, and a full plumed tail. A narrow scar crosses the ridge above his left brow. He wears an open dark robe with loose sleeves over dark trousers and is barefoot.

Two submissions with byte-identical text and different seeds:

- Run A answers: does the complete description return the intended character at all?
- Run A against Run B answers: does the same complete description return the same individual twice?

Caveat declared in advance: whether this surface honors `seed` has never been verified. If it does not, A and B are simply two independent samples of the same prompt, and the A-against-B comparison reads the same way.

## Exact submission

Director package path: none. This is a controlled variation on the sibling record's run 5, not an episode production. No variant from this record enters canon or continuity.

Submission sheet path: none. The request bodies as sent are `requests/runA-request.json` and `requests/runB-request.json`, built by inserting the prompt files verbatim into the documented top-level fields and verified by JSON round-trip against the prompt files. The earlier `*.template.json` pre-check files were superseded by these and removed in cleanup. Raw submit and poll responses and the downloaded videos are preserved outside the repository under `field-study-media/2026-08-04-seedance20-openrouter-prose-identity/`.

Input file paths and hashes: none. No media is submitted; that is the point of the test.

Primary submitted-text paths and hashes:

| Run | File | sha256 (first 16) | Bytes |
|---|---|---|---|
| A | `prompts/runA-submitted-text.txt` | `40e990e1ec7262e9` | 1,978 |
| B | `prompts/runB-submitted-text.txt` | `40e990e1ec7262e9` | 1,978 |

The identical hashes are deliberate: they document that the only difference between the two submissions is the seed in the request body.

Other field-text paths and hashes: none. This surface documents no separate exclusion field; exclusions are in the primary text, unchanged from run 5.

Settings: `aspect_ratio` 16:9, `duration` 8, `resolution` 720p, `generate_audio` true, identical to the sibling record's runs. `seed` 11 for run A, matching run 5; `seed` 12 for run B.

Cost: predicted at about $2.42 from the sibling record's observed $1.2096 per run. Actual `usage.cost` was 1.2096 for each run, $2.4192 total, matching the sibling record's per-run charge.

Service-returned rewritten prompt, when available: none returned. The poll response carries only `id`, `generation_id`, `polling_url`, `status`, and `usage`.

UI/operator edits after package creation: none permitted without updating the prompt files and their hashes first.

## Creative requirements declared before viewing

Identity criteria. These decide the hypothesis:

| Requirement | Carrier used | Required/flexible | Observable acceptance |
|---|---|---|---|
| species reads as an anthropomorphic wolf: long muzzle, upright ears, full plumed tail | prose alone | required | not a ferret, cat, dog-breed, or other creature; wolf-like head and tail are visible |
| tall, heavily built: visible shoulder and chest mass | prose alone | required | the build is heavy, not slender |
| short white fur, cream at the throat | prose alone | required (white); flexible, recorded (cream throat) | white-furred; throat colouring noted |
| narrow scar above the left brow | prose alone | required (presence); flexible, recorded (laterality) | a brow scar is visible; which side is noted |
| yellow eyes | prose alone | flexible, recorded | eye colour noted if resolvable at 720p |
| open dark robe with loose sleeves, dark trousers, barefoot | prose alone | required (robe and trousers); flexible, recorded (barefoot) | clothing matches |
| cross-run identity: A and B show the same individual | prose alone | required for the repeatability reading only | same species read, build class, fur pattern, face; a reasonable viewer says it is the same character |

Scene criteria. These are recorded but do not decide the hypothesis:

| Requirement | Carrier used | Required/flexible | Observable acceptance |
|---|---|---|---|
| room, lamp, window, POV relation per text | prose alone | flexible, recorded | layout noted against the scene paragraph |
| one continuous take, no cut, no teleport | prose | flexible, recorded | seams noted |
| audio present, no speech | `generate_audio` and exclusions | flexible, recorded | track presence and speech noted |

## Pre-registered decision rule

The outcome licenses a specific edit to `examples/storm-watch/source-brief.md`, decided now, before viewing, so the brief's final wording cannot be fitted to the result after the fact. In every outcome the brief's prescription of a character reference sheet survives; what changes is only the evidence sentence and its citation. In every outcome the conclusion is scoped: one beat, one surface, one day, two runs.

| Outcome | Observation | Licensed edit to the brief |
|---|---|---|
| F: insufficient | any required identity criterion fails in either run | the sentence stands; add this record as its citation alongside the sibling record, stating both the underspecified and the complete description failed on this surface |
| P: partial | both runs individually satisfy the required criteria, but A and B are not the same individual | replace the sentence: a complete written description fixed species and build within a single run but did not return the same individual across two runs; the reference sheet is required for cross-run identity |
| S: sufficient | both runs satisfy the required criteria and read as the same individual | replace the sentence: only the underspecified description is proven insufficient; a complete description sufficed on this surface in two runs; the reference sheet is justified as the derivation anchor for endpoint frames and cross-surface consistency, not by prose insufficiency |

## Returned variants

| Run | Variant | Returned metadata verified locally | Complete file preserved? |
|---|---|---|---|
| A | 1 | 8.058 s, 1280x720, video and audio tracks present, 2,463,495 bytes | yes, outside the repository |
| B | 1 | 8.058 s, 1280x720, video and audio tracks present, 3,038,868 bytes | yes, outside the repository |

Each submission returned exactly one output. Job IDs: `m6xciiUH62AfbVXZRqoQ` (A), `2klRfbneOdpC8OL4DfGd` (B). The videos and raw responses are preserved outside the repository under `field-study-media/`, consistent with the sibling record's handling.

One unresolved surface observation: at about 12:00 UTC the operator reported the OpenRouter dashboard showing a completed state while the job endpoint, the saved `polling_url`, and the content endpoint all still returned pending for run B, which the API first reported completed at 12:32:18. Which dashboard row the operator saw was not confirmed, so this stays an operator report, not an established discrepancy.

## Direct observations by run

Observation protocol: the operator views every output. The assistant cannot decode video and views none of them; container metadata is the only machine-side observation. Each run is answered against the criteria tables above, item by item, before any interpretation is written.

### Run A

The operator confirmed the identity checklist in a blanket statement ("the checkpoints all apply") and then itemized the deviations below. Items not itemized are recorded as confirmed-by-summary, not as individually described.

Species read: wolf. The head carries the expected muzzle and upright ears. The operator's qualification: the result reads as a literal wolf's head joined to a fur-covered human body, an uncanny join rather than an integrated anthropomorphic design. The pre-registered criterion (wolf-like head and tail, not another species) is met; the integration quality is recorded as an additional observation, not folded back into the criterion.

Build: confirmed by summary (tall, heavy).

Fur and throat: confirmed by summary (white).

Brow scar and side: confirmed by summary; side not itemized.

Eye colour: not itemized.

Clothing and feet: confirmed by summary.

Room, lamp, window, POV relation: the bed sat at the left of frame instead of filling the lower foreground. The submitted text says only that the bed and blanket fill the lower foreground and never states the bed's side; in the sibling record's runs this fact was carried by the submitted media. Scene item: recorded, does not decide the hypothesis.

Continuity of the take: confirmed by summary; no cut or teleport was reported beyond the seating artifact below.

Sound: confirmed by summary (rain, thunder, contact; no speech).

Unexpected additions, cuts, or artifacts: the character walked to the bed and lowered into a seated pose in front of the mattress without landing on it, holding an air-chair posture. The sit never connected to the mattress edge. Operator observation, recorded before the identity checklist was answered.

### Run B

The operator answered run B through the A-against-B comparison rather than item by item. No failed required criterion was reported; the comparison framing treats run B as the same design category as run A, with two itemized deviations.

Species read: wolf, per the comparison framing; not separately itemized.

Build: somewhat more muscular than run A. Still within the required tall-and-heavily-built.

Brow scar and side: present, placed near the right eye on the brow ridge. Whether "right" is screen-right or the character's right was not disambiguated; on a facing character, screen-right is the character's left. The decisive fact for the cross-run criterion is that the two runs place the scar differently, which holds under either convention.

Fur and throat, eye colour, clothing and feet, room, continuity, sound: not separately itemized.

### A against B

Same individual? No. Operator verdict: not the same character. The scar placement differs between the two runs, and run B's build is noticeably heavier than run A's. The cross-run identity criterion fails.

## Accepted variant

User decision: not applicable. This is a controlled test; no variant is carried into production, canon, or continuity regardless of outcome.

Criteria waived, if any: none.

Repair/post-production required: not applicable.

## Finished endpoint

Final composite path: none by design.

## Requirement-transfer findings

| Requirement | Carrier | Observed outcome | Smallest next change |
|---|---|---|---|
| character identity | prose alone, complete description | each run individually satisfied the required criteria; run A's design read as a literal wolf's head joined to a fur-covered human body rather than an integrated anthropomorphic design | carry the design in an approved character reference sheet; prose carries facts, not the design |
| cross-run identity stability | prose alone, identical text, different seed | failed: the scar placement moved and the build shifted between two byte-identical submissions | anchor the individual with approved character media before the next identity-bearing generation |
| scene layout without media | prose alone | the bed's side was never stated and the model chose frame-left; the seat landed in the air in front of the mattress | state every load-bearing layout fact in the text, or supply the start frame that carries it |

## Narrow conclusion

Outcome: P, partial.

A complete written description, submitted twice with byte-identical text and different seeds, satisfied the required identity criteria in each run taken alone: 2 of 2 runs read as an anthropomorphic wolf, heavily built, white-furred, scarred, in the described clothing. The same description did not return the same individual twice: in the single A-against-B comparison the scar placement moved and the build shifted. Prose fixed the category. It did not fix the individual.

Two observations recorded outside the decision: run A's design read as a literal wolf's head joined to a fur-covered human body rather than an integrated anthropomorphic character, and run A seated the character in the air in front of the mattress, in a room whose bed side the text had never stated.

The licensed P edit was applied to `examples/storm-watch/source-brief.md`: the sentence "A written description alone has already proved insufficient" is replaced by the scoped finding, with this record added as its citation.

These statements describe this beat, this model, this surface, and this day, over two runs and one comparison. They are not product limits. Whether this surface honors `seed` was not verified, so the two runs are read simply as two samples of the same prompt.
