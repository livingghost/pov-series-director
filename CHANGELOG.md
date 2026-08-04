# Changelog

## 2026.08.04.2

First public release.

### Runtime

- Fifteen specialist references and four operational references. The specialist set covers project state and trust, runtime target evidence, production rules, the scoped lexicon, style rules, dialogue and localization, story functions and music, hooks and retention, multi-character blocking, contact scenes, atmosphere and image quality, first-person camera language, performance details, post-production and clip joins, and output templates; the operational set covers operational distinctions, prompt composition, model-facing artifacts, and target adaptation.
- The post-production reference finishes what the rest of the procedure routes: boundary types decided at packing time, the join menu from the single-take tradition with the blink as the POV-native cut, conform and registration rules, masked-event calibration against the scene's own light grammar, split edits and bed continuity for audio, loudness targets, a repair menu, and machine-first join verification.
- Division of labor by capability and authority: the user always holds spending, canon, and final acceptance; the host verifies what it can measure (containers, boundary frames, levels) before any human viewing, and a defect the human finds that a measurement could have found first is treated as a process failure.
- Three evidence stages with the finishing order fixed: Phase A ends by stating which media is still missing, Phase B conforms boundary media to the delivery resolution and derives continuation anchors from extracted real frames, and Phase C verifies machine-side first and extracts the terminal frame only after finishing.
- Creative-requirement transfer, operation cards built from real controls, and target facts recorded per surface with a source and a check date, so the bundle ships no vendor specification sheets and unknowns stay unknown.

### Worked example

- `examples/storm-watch/` is a canonical artifact chain: source brief → Phase A with two-clip packing → a character-reference brief and three boundary-frame briefs → approved production media with logged lineage under `media/` → direct frame inspection → per-target Phase B packages. Planning diagrams are kept separate and are never submitted.
- The Seedance 2.0 branch, on the directly observed OpenRouter surface, was executed for real: both clips rendered from sheet-derived media, the continuation opened from the extracted terminal frame, retakes recorded with their causes, the join registered and masked in finishing, and the episode's continuity frame preserved. Submissions, costs, and observations are in its result log.
- The Runway Gen-4.5 and Veo 3.1 branches are documentation-grounded and not run, superseded pending rebuild onto the new media; their evidence-dated surface facts remain valid reference.
- `examples/demo-episode.md` is assembled from the canonical artifacts by `scripts/build_demo.py`, so the reading view cannot silently diverge from the files it describes.
- `examples/field-study/` holds the run-record template and two controlled studies from 2026-08-04 whose findings shaped the current media rules: a schematic diagram submitted as an endpoint returns a schematic diagram in motion, and a complete written description fixes a character's category but not the individual.
- `examples/test-cases.md` holds forty-two regression cases.

### Packaging

- A runtime and a full single-file adapter for hosts that accept one file, both generated from `package-manifest.toml`.
- `scripts/build_demo.py`, `scripts/build_flat.py`, and `scripts/build_release.py`, each with a `--check` or verification path.
- `scripts/validate_skill.py` checks source coverage, adapter completeness, current-template conformance, exact-text self-containment, approved-media dimensions, and per-branch run-status disclosure. It does not evaluate generated video quality.

### Evidence boundary

- Only the Seedance branch claims run results, and only those preserved in its result log with the operator's recorded observations. The Runway and Veo packages remain explicitly `not run` and claim no generated output.
