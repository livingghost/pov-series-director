# Story Functions, Segment Roles, Sound, and Stitching

## 1. Five story functions

The method uses five ordered functions rather than five equal time boxes:

1. **Setup or continuing-action entry**: establish the current playable situation without process-only warm-up.
2. **Build**: introduce pressure, desire, mismatch, or a variable.
3. **Turn trigger**: the visible or audible event that changes the beat's direction.
4. **Turn payoff or reaction**: the character-specific consequence of the trigger.
5. **Settle or bridge**: gather the relationship into a stable image or hand the action into the next segment.

Default story duration is fifteen seconds only when the project and runtime allow it. Allocate seconds by complexity; do not divide automatically into equal thirds.

## 2. Turn design

Use a Turn type as editorial vocabulary when it clarifies the designed change. The label must point to a different trigger, reaction, or ending; omit it when deleting the label would change nothing:

- **Reversal:** an expectation breaks.
- **Escalation:** a small problem grows.
- **Reveal:** the POV sees what was hidden.
- **Intrusion:** a person, object, sound, or external force enters.

Comedy often benefits from an earlier trigger and more reaction time. Tender or painful episodes may place the payoff later and leave more settle time. Avoid placing the Turn at the same structural position in several consecutive episodes without intent.

A short episode carries one emotional peak. Split a story that needs several peaks into charge and release episodes rather than flattening them into one clip.

## 3. Segment roles

The role controls hook and ending requirements.

| Role | Opening | Ending |
|---|---|---|
| `standalone_short` | hook required | quiet settle or purposeful unresolved image required |
| `chapter_opening` | hook required | settle or forward bridge |
| `interior_segment` | continue prior action; no artificial hook | action/audio/occlusion bridge preferred |
| `chapter_closing` | contextual entry | quiet settle and relationship consequence required |

Do not force a greeting, anomaly, or closing pause into an interior segment merely to satisfy a short-form template.

## 4. Sound design

Record three fields during analysis:

```text
ambient bed =
turn effect =
closing or bridge sound =
```

Sound is functional when a character hears it, reacts to it, or it hides a seam. Use one ambient bed and one key effect in one or two beats. At the Turn, the functional effect outranks music.

## 5. Music design

Give a storyline a simple instrumentation identity and recurring motif only when music is part of the project. Describe instrumentation, pulse, register, and motif behavior rather than relying on a song title.

- Setup: ambience first; motif may enter lightly.
- Build: add one layer.
- Turn: music steps aside or cuts so the functional effect lands.
- Settle: motif returns or yields to ambience and one object sound.

Delivery may be native generation, an audio reference, or post-production. `production-state.md` determines which channels are actually available.

## 6. Narration episodes

An optional narration workflow: a present-time voice-over frames scenes from the past, as in a memoir or retrospective episode. The POV rules still apply inside the depicted scenes.

- Cold narration over a warm scene. The narrator speaks from the present, calm and even; the depicted past stays alive, warm, and concretely rendered. The temperature difference between the two layers carries the emotion. Never age or soften the past with a degradation filter; keep sound wording concrete per `references/lexicon.md`.
- Scoring under narration. While a narration sentence runs, keep only low sustained texture and let melody answer in the gaps. Musical phrases enter after a narration sentence lands, so the pauses set the entries. The heaviest line plays dry, with no music at all.
- In-world metronome. A repeating diegetic sound, such as knitting needles, sword practice, or a fire, can keep time instead of a drum part.
- Cross-episode motif arc. The recurring motif may travel complete, fragmented, off-key, varied, and finally fully stated across episodes, tracking the character's state.
- Narration lines are voice metadata like dialogue. Keep on-scene flashback dialogue within the project's dialogue density, and record narration in the dialogue and subtitle metadata block.

## 7. Multi-clip stitching

A clip is a delivery unit, not a shot. Default to one continuous take per clip and declare any internal cut, such as a blink cut or an occlusion wipe, together with the beat it serves. A target that adds its own cuts reassigns the packed story time and the beat plan silently, so state the shot plan in every clip prompt and record any unrequested cut as a render observation in `production-state.md`.

Use `runtime-capabilities.md` for arithmetic, input roles, operation gates, and packing. Every ordinary seam records:

- outgoing clip or V asset
- actual outgoing ending S anchor
- actual or planned incoming opening S anchor
- bridge type: `action`, `audio`, `occlusion`, `eyeline`, `light`, or `continuation-input`
- repeated continuity anchors: ambient bed, pose, held prop, facing, and practical light

Cut at a story-function boundary whenever possible. If a function must split, use one causal micro-boundary such as preparation/action or contact/release.

`generated-transition` is a distinct bridge backed by an actual target operation, not another name for a cut. It requires the exact surface to accept the necessary source videos or boundary controls together, plus two inspected boundary frames and a recorded file-to-control recipe. Record it as:

```text
bridge type: generated-transition
outgoing operand: V10-v1
outgoing endpoint anchor: S21-v1
incoming operand: V11-v1
incoming endpoint anchor: S22-v1
generated bridge/output: V12-v1
operation: transition
story duration:
generated duration:
operation-card/run ID:
```

If any requirement is unavailable or unknown, preserve the intended bridge in the director package and use an ordinary edit, create an intermediate boundary asset, or redesign the shot. Never infer transition support from generic video-reference or single-operand editing support.

Spare generated time is an intentional hold or ambience tail. Never hide it by claiming the generated clip is shorter than the verified available duration.

## 8. Long-form workflow

For a chapter or film assembled from many segments:

- hooks belong at the film opening and chapter openings
- quiet closing pauses belong at chapter endings
- interior segments cut on continuing action or sound
- record narration as one coherent text before dividing it
- score music by chapter in post when per-clip restarts would be distracting
- scale Setup, Build, Turn, and Settle across the chapter while each segment retains a local causal progression

## 9. Story-analysis fields

```text
segment role =
target story duration =
Turn = function/beat ___ · type ___
ambient bed =
turn effect =
closing or bridge sound =
hook = required/not required · type ___
one-line retell =
emotional peak =
```
