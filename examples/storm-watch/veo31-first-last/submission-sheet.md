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
