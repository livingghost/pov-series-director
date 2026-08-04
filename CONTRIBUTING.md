# Contributing

Changes must improve the actual directing or production result, not merely add terminology.

## Contribution test

For every new distinction or label, show at least one concrete consequence:

- a different asset is created;
- a different real control/request key is used;
- exact submitted text changes;
- the shot is split or re-staged;
- a separate generation/edit/audio/post route is chosen;
- review evidence or acceptance changes.

When two labels produce the same media, controls, text, post path, and review, remove or merge the labels.

## Preserve specialist capability

Do not delete or flatten concrete knowledge about:

- story structure and hooks;
- POV camera/body behavior;
- blocking and multi-character staging;
- physical causality, contact, occlusion, and material response;
- character performance and anatomy;
- dialogue, language, voice, subtitles, sound, music;
- weather, light, atmosphere, and visual quality;
- asset lineage, boundary frames, clip packing, edit/extension/transition routes;
- result review and canon write-back.

A shorter runtime is not automatically better. Move detail into the correct carrier; do not erase it.

## Evidence standards

Vendor-specific claims require current official documentation or inspectable exact-surface evidence. Record the source and check date in the target-specific submission sheet; do not embed mutable vendor facts as timeless runtime rules.

Worked examples must disclose one of:

- `documentation-grounded, not run`; or
- exact submitted files/text/settings plus preserved outputs and direct observations.

Never narrate a successful render that is not included and inspectable.

## Build and test

```bash
python scripts/build_demo.py --check
python scripts/build_flat.py --profile all
python scripts/validate_skill.py
python scripts/build_release.py
```

The validator enforces runtime source coverage and several anti-downgrade invariants. Add a regression case when changing any core distinction.

## Pull requests

Describe:

1. the concrete production problem;
2. the before/after media, field, prompt, operation, or review difference;
3. which specialist knowledge is preserved;
4. the evidence level of any target-specific claim;
5. validation performed.
