# Approved Media Log

Generator: `google/gemini-3-pro-image` via OpenRouter `POST /api/v1/chat/completions` with image output, 2026-08-04. Every generation's exact prompt is preserved under `prompts/`; rejected iterations are preserved outside the repository under `production-media/storm-watch/`.

Approval state: the owner delegated intermediate approvals on 2026-08-04 ("proceed through video generation without approval"), so acceptance below is the assistant's inspection against the media briefs, recorded as provisional until the owner's final review. The sleepwear colour, dark teal, is a design decision carried over from the pre-rewrite prop colour and shares that provisional status.

## Iterations

| # | File | Derived from | Generation id | Cost | Verdict |
|---|---|---|---|---|---|
| 1 | sheet-v1 | text only | `gen-1785848525-qf5EpEe99LrQ2oyzb7sw` | $0.1385 | rejected: plantigrade legs; scar side inconsistent between views; build too light; robe brown rather than dark |
| 2 | sheet-v2 | edit of v1 | `gen-1785848643-qf4I6H6kKIaM92aLoHu9` | $0.1415 | accepted → `character-sheet.png` |
| 3 | clip1-start-v1 | character sheet | `gen-1785848751-PgJrNlAVQHr3DgTFn1bT` | $0.1410 | rejected: sleepwear unfolded and dangling from one hand |
| 4 | clip1-start-v2 | edit of v1 | `gen-1785848823-rsjZczAGC0DwkUhRYrBa` | $0.1368 | accepted → `clip1-start.jpg` |
| 5 | clip1-end-v1 | edit of accepted start | `gen-1785848920-sCTvIaiPVRq8KpgcCJid` | $0.1378 | accepted → `clip1-end.jpg` |
| 6 | clip2-end-v1 | accepted start + sheet | `gen-1785849014-Hh1B5ZzxD1yGhBdbyBCZ` | $0.1422 | accepted, later superseded: generated before the terminal frame existed, its free framing caused the take 1 stretch and the take 2 join-visible zoom |
| 7 | clip2-end-v2 | edit of the real terminal frame | `gen-1785857331-2GBo8VxkyOyuBOAZl9n9` | $0.1378 | rejected: the edit removed his robe and hunched the pose |
| 8 | clip2-end-v3 | edit of the real terminal frame, clothing and posture constrained | `gen-1785857402-pX6yGj4tHAWTyzvl4o4P` | $0.1383 | accepted → `clip2-end.png` |

Total image cost: $0.8378 of the $5.00 cap. Costs are the `usage.cost` values returned per generation; unlike the video surface, the listed accounting matched the returned charge mechanism directly.

## Accepted files

| File | Format | Pixels | sha256 (first 16) | Bytes |
|---|---|---|---|---|
| `character-sheet.png` | png | 1376×768 | `be0db21958b36c3b` | 1,411,320 |
| `clip1-start.jpg` | jpeg | 1376×768 | `949cdc8b6acff07d` | 653,709 |
| `clip1-end.jpg` | jpeg | 1376×768 | `3d21c3b0e335a955` | 673,637 |
| `clip2-end.png` | png | 1280×720 | `7b90d46f3552e057` | 1,127,180 |
| `clip2-start.png` | png | 1280×720 | `7fb8dd33518ba731` | 931,638 |

`clip2-end.png` is the v3 derivation: an edit of the real terminal frame `clip2-start.png`, so camera and field of view are inherited rather than re-invented, conformed from 1365×768 by direct Lanczos scale to 1280×720 (aspect difference 0.024 percent, no crop, no zoom introduced). Two standing rules came out of the Clip 2 takes: every boundary image is conformed to the delivery resolution before submission, and a continuation clip's end anchor is derived from the extracted terminal frame itself, not from pre-render planning media. Earlier `clip2-end.png` states (`b23955c4ec3a8284` original, `376d3fa0aae506c0` crop-conformed) are preserved in git history.

`clip2-start.png` is not a generation: it is the terminal frame of the accepted Clip 1 take 1 (job `b00ddyOO3QfCL6UGKFTK`), extracted locally with ffmpeg 9.0 at 0.1 s before end of stream, after the operator accepted the take. It is the real geometry Clip 2 starts from.

| `episode-continuity-frame.png` | png | 1280×720 | `7a73f726f2af4b16` | see file |

`episode-continuity-frame.png` is the final frame of the finished episode master (`production-media/storm-watch-episode/episode-master.mp4`), extracted after the join, flash masking, and audio assembly were complete. It is the continuity landing the next episode opens from: Iven seated guard on the left mattress edge facing the window, the sleepwear beside the pillow, his tail across the blanket.

The generator returns 1376×768 rather than exactly 1280×720; the aspect deviation from 16:9 is under one percent. Submission mime types must match the container formats above, not the file extensions' historical assumptions.
