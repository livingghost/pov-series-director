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
