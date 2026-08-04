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
