# Field study for real generator runs

Use this directory structure when testing whether the Skill's submission packages produce interpretable results on a real video generator.

```text
field-study/<target>/<case>/<run-id>/
├── source-record.md
├── director-package.md
├── submission-sheet.md
├── submitted-text.txt
├── other-field-texts/
├── inputs/
├── outputs/
├── terminal-frames/
└── result-log.md
```

## Minimum test design

For each fixed case:

1. freeze the media and exact text;
2. generate more than one variant where cost permits;
3. preserve every returned variant;
4. declare required and flexible outcomes before viewing results;
5. log direct observations independently for each variant;
6. repeat after a model/surface change rather than merging evidence;
7. change one submission element at a time when comparing alternatives.

## Suggested fixed cases

- start-frame fidelity with one subtle body movement;
- a recurring character already present in the start image;
- a start/end-frame physical transition;
- a prop remaining with the same owner;
- continuation from an extracted accepted terminal frame;
- one short spoken line, evaluated separately for speaker and wording;
- positive wording versus a real separate negative field, when both are supported by different surfaces.

## Do not publish misleading evidence

- Do not omit failed variants.
- Do not relabel a documentation example as a run.
- Do not infer a universal rule from one scene.
- Do not claim exact target versions that were not exposed to the operator.
- Do not redistribute private user media or credentials.

Copy [run-record-template.md](run-record-template.md) and [scoring-guide.md](scoring-guide.md) into each real run directory.
