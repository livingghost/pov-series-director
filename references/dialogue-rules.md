# Dialogue, Character Grammar, and Localization

## 1. Two tests

1. **Name-masking test:** hide the speaker label. The line should still sound attributable to that character.
2. **Function test:** if a line only explains the room, lore, or plot mechanics, give that job to the image or action and remove the line.

## 2. Common synthetic-dialogue tells

Fix these on sight:

- complete explanatory sentences when fragments would be natural
- dialogue any character could say
- emotion stated directly instead of leaking through word choice or avoidance
- customer-service politeness unrelated to the character
- symmetrical question-and-answer exchanges
- stock exclamations and generic acknowledgements
- translation shaped by another language's syntax
- every speaker receiving a line merely because they are present

## 3. Character Grammar

Each recurring character owns three language features in `character-profiles.md`:

- **Thinking grammar:** how they organize the world: verdicts, trades, commands, denials, questions, rituals, diagnoses, or gifts.
- **Vocabulary domain:** language borrowed from profession, origin, status, hobby, or worldview.
- **Sentence fingerprint:** habitual length, omissions, patches, particles, order, and repair patterns.

A catchphrase is optional. A way of thinking is mandatory.

Verification exercise: have the cast express the same fact and ensure every version differs in logic, vocabulary, and shape.

## 4. Conversation rules

- Prefer action answers, counter-questions, and sideways answers over direct answers when character-true.
- Draft fully, then cut at least a third of the words unless the character's established voice is verbose.
- A silent reaction is valid and often stronger than a reply.
- Follow the current speech stage exactly; do not unlock fluency early.
- During dialogue, keep body movement small and camera behavior stable unless the movement is the line's single dramatic action.

## 5. Write in the dialogue language

Compose each line directly in the character's `dialogue_language` and register. Do not first write an English line and mechanically translate it. Preserve subject omission, politeness level, particles, dialect, rhythm, and culturally natural indirectness.

When an execution target has limited spoken-language support, keep the canonical dialogue in the character's language and mark the audio path as post-production or unresolved. Do not silently change the character's language.

## 6. Subtitle policy

Subtitles are independent production data and default to `off`. If subtitles are requested without a language, use the series audience language when recorded; otherwise use `response_language` and label it explicitly.

When enabled, every track must declare:

- language
- delivery route (sidecar, metadata, burned-in, or another concrete path)
- exact text
- timing, once clip timing is locked
- translation style when it is not literal

Example metadata:

```text
Speaker: C01
Dialogue language: ja-JP
Line: 「……守る。」
Tone: low, clipped, protective
Subtitle [fr-FR, sidecar]: « …Je monte la garde. »
Subtitle [zh-Hans, sidecar]: 「……我来守夜。」
```

Omit subtitle entries when subtitles are off. Do not insert subtitle text into the visual prompt unless the user explicitly requests burned-in text and the exact target surface provides current evidence for that route. Otherwise preserve the subtitle as a sidecar or post-production deliverable.

## 7. Subtitle localization

- Preserve character grammar and social register, not only dictionary meaning.
- Keep names, invented terms, and recurring phrases consistent with the project's glossary.
- Mark deliberate adaptation, wordplay replacement, or honorific loss.
- For multiple tracks, translate from the canonical dialogue, not from another subtitle translation.
- Generate final timecodes only after the clip map is fixed; regenerate them if timing changes.

## 8. Beat-template fatigue

Keep the causal structure while rotating surface form:

- openings: sound first, visible hand already mid-task, peripheral entrance, awakened by weight, light opening through a gap
- reactions: listener close-up, held prop, posture change, off-frame line while watching the listener
- endings: object, back, dying sound, unfinished line, one body part, or continuing action

Review the previous two episodes and vary repeated sentence shapes deliberately.
