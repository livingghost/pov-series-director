#!/usr/bin/env python3
"""Validate repository, anti-downgrade, and canonical-example invariants.

This validator does not evaluate generated video quality. It verifies source coverage,
reproducible packaging, run-status disclosure, current-template conformance, and
concrete creative-detail transfer.
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
import re
import struct
import sys
import tomllib
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


@dataclass
class Finding:
    path: str
    message: str


class Validator:
    def __init__(self, root: Path) -> None:
        self.root = root
        self.findings: list[Finding] = []
        self.package_count = 0
        with (root / "package-manifest.toml").open("rb") as handle:
            self.manifest = tomllib.load(handle)

    def fail(self, path: Path | str, message: str) -> None:
        if isinstance(path, Path):
            try:
                shown = str(path.relative_to(self.root))
            except ValueError:
                shown = str(path)
        else:
            shown = path
        self.findings.append(Finding(shown, message))

    def require_file(self, rel: str) -> Path:
        path = self.root / rel
        if not path.is_file():
            self.fail(rel, "required file is missing")
        return path

    def read(self, rel: str) -> str:
        path = self.require_file(rel)
        if not path.is_file():
            return ""
        try:
            return path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            self.fail(path, "must be UTF-8 text")
            return ""

    def require_markers(self, rel: str, markers: list[str]) -> None:
        text = self.read(rel)
        folded = text.casefold()
        for marker in markers:
            if marker.casefold() not in folded:
                self.fail(rel, f"missing anti-regression marker: {marker!r}")

    @staticmethod
    def headings(text: str, level: int = 2) -> list[str]:
        prefix = "#" * level + " "
        return [line[len(prefix):].strip() for line in text.splitlines() if line.startswith(prefix)]

    @staticmethod
    def sha256(path: Path) -> str:
        digest = hashlib.sha256()
        digest.update(path.read_bytes())
        return digest.hexdigest()

    def validate_manifest_and_version(self) -> tuple[list[str], list[str]]:
        package = self.manifest.get("package", {})
        version = package.get("version")
        if not isinstance(version, str) or not re.fullmatch(r"\d{4}\.\d{2}\.\d{2}\.\d+", version):
            self.fail("package-manifest.toml", "package.version must use YYYY.MM.DD.N")
            version = ""

        skill = self.read("SKILL.md")
        match = re.search(r'^\s*version:\s*"([^"]+)"', skill, re.MULTILINE)
        if not match or match.group(1) != version:
            self.fail("SKILL.md", "front-matter version must match package.version")

        knowledge = self.manifest.get("knowledge", {})
        specialists = knowledge.get("specialist_sources")
        operational = knowledge.get("operational_sources")
        if not isinstance(specialists, list) or len(specialists) != 15:
            self.fail("package-manifest.toml", "knowledge.specialist_sources must contain all 15 specialist references")
            specialists = specialists if isinstance(specialists, list) else []
        if not isinstance(operational, list) or len(operational) != 4:
            self.fail("package-manifest.toml", "knowledge.operational_sources must contain 4 operational references")
            operational = operational if isinstance(operational, list) else []
        all_refs = specialists + operational
        if len(set(all_refs)) != len(all_refs):
            self.fail("package-manifest.toml", "knowledge source lists contain duplicates")
        for rel in all_refs:
            self.require_file(rel)
            if not rel.startswith("references/"):
                self.fail("package-manifest.toml", f"knowledge source is not under references/: {rel}")

        flat = self.manifest.get("flat", {})
        runtime = flat.get("runtime", {})
        full = flat.get("full", {})
        runtime_sources = runtime.get("sources") if isinstance(runtime, dict) else None
        full_sources = full.get("sources") if isinstance(full, dict) else None
        expected_runtime = ["SKILL.md", *all_refs]
        if (
            not isinstance(runtime_sources, list)
            or set(runtime_sources) != set(expected_runtime)
            or len(runtime_sources) != len(expected_runtime)
            or not runtime_sources
            or runtime_sources[0] != "SKILL.md"
        ):
            self.fail("package-manifest.toml", "runtime adapter must contain SKILL.md plus every knowledge source exactly once")
            runtime_sources = runtime_sources if isinstance(runtime_sources, list) else []
        if not isinstance(full_sources, list) or full_sources != [*runtime_sources, "examples/demo-episode.md"]:
            self.fail("package-manifest.toml", "full adapter must equal runtime sources plus examples/demo-episode.md")

        for profile, cfg in (("runtime", runtime), ("full", full)):
            output = cfg.get("output") if isinstance(cfg, dict) else None
            if not isinstance(output, str):
                self.fail("package-manifest.toml", f"flat.{profile}.output must be a path")
            else:
                self.require_file(output)

        release = self.manifest.get("release", {})
        output = release.get("output") if isinstance(release, dict) else None
        expected_zip = f"dist/pov-series-director-{version}.zip"
        if output != expected_zip:
            self.fail("package-manifest.toml", f"release.output must be {expected_zip}")
        includes = release.get("include") if isinstance(release, dict) else None
        if not isinstance(includes, list) or not includes:
            self.fail("package-manifest.toml", "release.include must be non-empty")
        else:
            for rel in includes:
                if not (self.root / rel).exists():
                    self.fail("package-manifest.toml", f"release include is missing: {rel}")

        return specialists, operational

    def validate_specialist_coverage(self) -> None:
        markers: dict[str, list[str]] = {
            "references/state-and-trust.md": ["Ownership map", "character-profiles.md", "Exact submission records", "Direct observations"],
            "references/runtime-capabilities.md": ["Operation proof card", "Clip packing is delivery arithmetic", "Performance transfer", "Packaging gate"],
            "references/production-rules.md": ["semantic density budget without erasing coupled detail", "Contact", "Dialogue, sound", "Creative-requirement transfer"],
            "references/lexicon.md": ["Visual prose", "Clean-realism quality profile", "Negative constraints"],
            "references/style-rules.md": ["Five spatial anchoring rules", "First-person presence", "Stillness without a dead frame"],
            "references/dialogue-rules.md": ["Character Grammar", "Write in the dialogue language", "Subtitle localization"],
            "references/structure-music.md": ["Five story functions", "Music design", "Narration episodes", "Multi-clip stitching"],
            "references/hook-retention.md": ["Avoid process-only openings", "Early micro-change", "One-line retell"],
            "references/multi-character.md": ["Blocking table", "Zero-simile blocking", "Coordinate translation table"],
            "references/contact-scenes.md": ["Universal geometry rules", "Carrying", "Hugs", "Hand contact"],
            "references/atmosphere-quality.md": ["Weather is an acting system", "Light must have a source", "Night scenes"],
            "references/pov-camera.md": ["The body drives the camera", "Sound-driven camera", "Direct interaction with the POV"],
            "references/performance-details.md": ["Expression tiers", "Idle pose and signature move", "Detail stacking"],
            "references/templates.md": ["Phase B: full director package", "Creative-requirement transfer", "Post-Production and Alternate-Path Plan", "Master Checklist"],
            "references/operational-distinctions.md": ["A first frame is not a subject reference", "A video reference is not a video operand", "Workflow stages are evidence changes"],
            "references/prompt-composition.md": ["Write the shot proposition", "Distinguish coupled motion", "Integrate contact", "revision ladder"],
            "references/model-facing-artifacts.md": ["Creative-Requirement Transfer", "Preserve specificity by moving it, not deleting it", "post-production"],
            "references/target-adaptation.md": ["Same beat, genuinely different submissions", "Prompt rewriting", "observable changes"],
        }
        for rel, required in markers.items():
            self.require_markers(rel, required)

    @staticmethod
    def source_comments(text: str) -> list[str]:
        return re.findall(r"<!-- Source: ([^>]+) -->", text)

    def validate_adapters(self, specialists: list[str], operational: list[str]) -> None:
        runtime_path = self.root / self.manifest["flat"]["runtime"]["output"]
        full_path = self.root / self.manifest["flat"]["full"]["output"]
        runtime = runtime_path.read_text(encoding="utf-8") if runtime_path.is_file() else ""
        full = full_path.read_text(encoding="utf-8") if full_path.is_file() else ""

        expected_runtime_comments = self.manifest["flat"]["runtime"]["sources"][1:]
        expected_full_comments = self.manifest["flat"]["full"]["sources"][1:]
        if self.source_comments(runtime) != expected_runtime_comments:
            self.fail(runtime_path, "source comments/order do not match runtime manifest")
        if self.source_comments(full) != expected_full_comments:
            self.fail(full_path, "source comments/order do not match full manifest")

        for rel in specialists + operational:
            marker = f"<!-- Source: {rel} -->"
            if marker not in runtime:
                self.fail(runtime_path, f"missing complete runtime source: {rel}")
            if marker not in full:
                self.fail(full_path, f"missing complete full source: {rel}")

        if "<!-- Source: examples/demo-episode.md -->" in runtime:
            self.fail(runtime_path, "runtime adapter must omit the long worked example")
        if "<!-- Source: examples/demo-episode.md -->" not in full:
            self.fail(full_path, "full adapter must include the generated worked example")
        if "examples/test-cases.md" in runtime or "examples/test-cases.md" in full:
            self.fail("adapters", "flat adapters must not include the evaluation source: examples/test-cases.md")

        if len(runtime.encode("utf-8")) < 120_000:
            self.fail(runtime_path, "runtime adapter is unexpectedly small; specialist knowledge may have regressed")
        if len(full.encode("utf-8")) <= len(runtime.encode("utf-8")):
            self.fail(full_path, "full adapter must be larger than runtime adapter")

        for marker in (
            "mattress compresses",
            "limb ownership",
            "Character Grammar",
            "Weather is an acting system",
            "Multi-Character POV Blocking",
            "Performance Detail Library",
            "Creative-Requirement Transfer",
        ):
            if marker.casefold() not in runtime.casefold():
                self.fail(runtime_path, f"anti-downgrade content missing: {marker!r}")

    @staticmethod
    def image_dimensions(path: Path) -> tuple[int, int] | None:
        try:
            data = path.read_bytes()
        except OSError:
            return None
        if data[:8] == b"\x89PNG\r\n\x1a\n" and len(data) >= 24:
            return struct.unpack(">II", data[16:24])
        if data[:2] == b"\xff\xd8":
            i = 2
            while i < len(data) - 9:
                if data[i] != 0xFF:
                    i += 1
                    continue
                marker = data[i + 1]
                if marker in (0xC0, 0xC1, 0xC2, 0xC3):
                    height, width = struct.unpack(">HH", data[i + 5:i + 9])
                    return (width, height)
                if marker in (0xD8, 0x01) or 0xD0 <= marker <= 0xD7:
                    i += 2
                    continue
                i += 2 + struct.unpack(">H", data[i + 2:i + 4])[0]
        return None

    def validate_exact_text(self, rel: str, required: list[str]) -> None:
        text = self.read(rel)
        forbidden_patterns = {
            "unresolved handlebars token": r"\{\{[^}]+\}\}",
            "infrastructure placeholder": r"\$\{[^}]+\}",
            "private asset ID": r"\b[CSVPA]\d{2}(?:-v\d+)?\b",
        }
        for label, pattern in forbidden_patterns.items():
            if re.search(pattern, text):
                self.fail(rel, f"contains {label}")
        for phrase in ("Image Notes", "dimension contract", "production record", "asset registry", "manifest label"):
            if phrase.casefold() in text.casefold():
                self.fail(rel, f"contains inaccessible production shorthand: {phrase!r}")
        for marker in required:
            if marker.casefold() not in text.casefold():
                self.fail(rel, f"rich exact direction was lost: {marker!r}")
        if len(text.split()) < 45:
            self.fail(rel, "exact prompt is suspiciously generic/short for the worked choreography")

    def validate_generated_demo(self) -> None:
        script = self.require_file("scripts/build_demo.py")
        demo = self.read("examples/demo-episode.md")
        if not script.is_file():
            return
        spec = importlib.util.spec_from_file_location("pov_build_demo", script)
        if spec is None or spec.loader is None:
            self.fail(script, "could not load generated-example builder")
            return
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        expected = module.render()
        if demo != expected:
            self.fail("examples/demo-episode.md", "generated reading view is stale; run scripts/build_demo.py")

    def validate_template_conformance(self) -> None:
        phase_a_rel = "examples/storm-watch/phase-a-plan.md"
        phase_a = self.read(phase_a_rel)
        expected_a = [
            "Episode purpose",
            "Clip packing",
            "Story and retention design",
            "POV and physical design",
            "Performance and dialogue",
            "Sound, atmosphere, and music",
            "Intended operation",
            "Existing approved media",
            "Media to create or extract",
            "Shot proposition, Clip 1",
            "Shot proposition, Clip 2 (provisional; opening not finalized)",
            "Provisional creative-requirement transfer",
        ]
        if self.headings(phase_a) != expected_a:
            self.fail(phase_a_rel, "Phase A headings do not match the current canonical template")
        for marker in ("awaiting media", "Do not claim", "character-reference-brief.md", "clip1-start-frame-brief.md"):
            if marker.casefold() not in phase_a.casefold():
                self.fail(phase_a_rel, f"Phase A provenance/stop condition missing: {marker!r}")

        expected_b = [
            "Story and continuity",
            "Inspected evidence",
            "Shot proposition",
            "Beat and causal spine",
            "Blocking table",
            "POV camera-body choreography",
            "Contact and prop continuity",
            "Performance direction",
            "Dialogue and voice",
            "Sound, atmosphere, light, and music",
            "Clip structure and duration",
            "Creative-requirement transfer",
            "Operation card",
            "Exact submission package",
            "Acceptance criteria",
        ]
        for rel in (
            "examples/storm-watch/runway-gen45-i2v/director-package.md",
            "examples/storm-watch/veo31-first-last/director-package.md",
            "examples/storm-watch/seedance20-first-last/director-package.md",
        ):
            text = self.read(rel)
            if self.headings(text) != expected_b:
                self.fail(rel, "Phase B director-package headings do not match the current canonical template")
            for marker in ("Inspected evidence", "Creative-requirement transfer", "Operation card", "Exact submission package"):
                if marker.casefold() not in text.casefold():
                    self.fail(rel, f"current Phase B mechanism missing: {marker!r}")

    def validate_examples(self) -> None:
        required_chain = [
            "examples/storm-watch/README.md",
            "examples/storm-watch/source-brief.md",
            "examples/storm-watch/phase-a-plan.md",
            "examples/storm-watch/media-briefs/character-reference-brief.md",
            "examples/storm-watch/media-briefs/clip1-start-frame-brief.md",
            "examples/storm-watch/media-briefs/clip1-end-frame-brief.md",
            "examples/storm-watch/media-briefs/clip2-end-frame-brief.md",
            "examples/storm-watch/planning-diagrams/README.md",
            "examples/storm-watch/frame-inspection.md",
            "examples/storm-watch/target-contrast.md",
        ]
        for rel in required_chain:
            self.require_file(rel)

        self.require_markers(
            "examples/storm-watch/README.md",
            ["canonical artifact set", "derivation chain", "Evidence state", "not run"],
        )
        self.require_markers(
            "examples/storm-watch/source-brief.md",
            ["Media initially available", "No approved visual media", "Runway Gen-4.5", "Veo 3.1", "Seedance 2.0"],
        )
        self.require_markers(
            "examples/storm-watch/planning-diagrams/README.md",
            ["never submit", "planning", "does not control the generator"],
        )
        self.require_markers(
            "examples/storm-watch/frame-inspection.md",
            ["Direct visual observations", "character-sheet.png", "clip1-start.jpg", "clip2-start.png", "digitigrade", "two-handed"],
        )
        self.validate_template_conformance()
        self.validate_generated_demo()

        media_specs = {
            "examples/storm-watch/media/character-sheet.png": (1376, 768),
            "examples/storm-watch/media/clip1-start.jpg": (1376, 768),
            "examples/storm-watch/media/clip1-end.jpg": (1376, 768),
            "examples/storm-watch/media/clip2-start.png": (1280, 720),
            "examples/storm-watch/media/clip2-end.png": (1280, 720),
            "examples/storm-watch/media/episode-continuity-frame.png": (1280, 720),
        }
        for rel, expected in media_specs.items():
            path = self.require_file(rel)
            if path.is_file():
                dims = self.image_dimensions(path)
                if dims != expected:
                    self.fail(path, f"approved media must be {expected[0]}x{expected[1]}, found {dims}")
        self.require_markers(
            "examples/storm-watch/media/media-log.md",
            ["Iterations", "Accepted files", "sha256", "conformed"],
        )

        packages = {
            "examples/storm-watch/runway-gen45-i2v": {
                "run_state": "not run",
                "superseded": True,
                "required_text": ["thunderclap", "ears", "folded shirt", "mattress", "loose sleeves", "pillow height", "one continuous shot"],
                "extra": ["post-production.md"],
                "post_markers": ("Safe.", "rain", "thunder", "mattress", "final"),
            },
            "examples/storm-watch/veo31-first-last": {
                "run_state": "not run",
                "superseded": True,
                "required_text": ["supplied first and last frames", "thunderclap", "ears", "two-handed", "mattress", "loose sleeves", "pillow height"],
                "extra": ["negative-prompt.txt", "request-body.template.json", "post-production.md"],
                "post_markers": ("Safe.", "rain", "thunder", "mattress", "final"),
            },
            "examples/storm-watch/seedance20-first-last": {
                "run_state": "run",
                "superseded": False,
                "required_text": ["supplied first and last frames", "thunderclap", "ears", "two-handed", "sleepwear", "mattress", "pillow height", "steady rain"],
                "extra": ["request-body.template.json", "post-production.md", "clip2-submitted-text.txt", "subtitles-en.srt"],
                "post_markers": ("大丈夫", "rain", "thunder", "mattress", "final"),
            },
        }

        for base, config in packages.items():
            for rel in ("README.md", "director-package.md", "submission-sheet.md", "submitted-text.txt", "result-log.md", *config["extra"]):
                self.require_file(f"{base}/{rel}")
            self.validate_exact_text(f"{base}/submitted-text.txt", config["required_text"])

            combined = "\n".join(
                self.read(f"{base}/{rel}")
                for rel in ("README.md", "director-package.md", "submission-sheet.md", "result-log.md")
            )
            result = self.read(f"{base}/result-log.md")
            if config["run_state"] == "not run":
                if "not run" not in combined.casefold():
                    self.fail(base, "worked target package must disclose not run")
                if re.search(r"Run status:\s*(?:returned|accepted|rendered)", combined, re.IGNORECASE):
                    self.fail(base, "not-run worked package claims a run result")
                if not re.search(r"Run status:\s*not run", result, re.IGNORECASE):
                    self.fail(f"{base}/result-log.md", "result log must explicitly say Run status: not run")
            else:
                if not re.search(r"Run status:\s*run\b", result, re.IGNORECASE):
                    self.fail(f"{base}/result-log.md", "executed package must explicitly say Run status: run")
                for marker in ("job id", "usage.cost", "terminal frame"):
                    if marker.casefold() not in result.casefold():
                        self.fail(f"{base}/result-log.md", f"run evidence is incomplete: missing {marker!r}")
            if config["superseded"] and "SUPERSEDED" not in combined:
                self.fail(base, "superseded package must carry its supersession banner")

            post = self.read(f"{base}/post-production.md")
            for marker in config["post_markers"]:
                if marker.casefold() not in post.casefold():
                    self.fail(f"{base}/post-production.md", f"creative requirement disappeared from alternate path: {marker!r}")

        self.package_count = len(packages)

        seedance = "examples/storm-watch/seedance20-first-last"
        self.validate_exact_text(
            f"{seedance}/clip2-submitted-text.txt",
            ["supplied first and last frames", "sleepwear", "tail", "mattress", "digitigrade"],
        )
        if (self.root / f"{seedance}/negative-prompt.txt").exists():
            self.fail(seedance, "this surface documents no separate exclusion field, so a negative-prompt file misrepresents the submission")
        for marker in ("one negation per unwanted artifact", "No speech."):
            if marker.casefold() not in "\n".join(
                self.read(f"{seedance}/{rel}") for rel in ("submission-sheet.md", "submitted-text.txt")
            ).casefold():
                self.fail(seedance, f"exclusions must be carried in the primary text: missing {marker!r}")

        json_rel = "examples/storm-watch/veo31-first-last/request-body.template.json"
        try:
            body = json.loads(self.read(json_rel))
        except json.JSONDecodeError as exc:
            self.fail(json_rel, f"invalid JSON: {exc}")
        else:
            try:
                instance = body["instances"][0]
                parameters = body["parameters"]
                assert "image" in instance and "lastFrame" in instance and "prompt" in instance
                assert parameters["negativePrompt"]
                assert parameters["durationSeconds"] == 8
                assert parameters["sampleCount"] == 4
                assert parameters["resolution"] == "720p"
            except (KeyError, IndexError, TypeError, AssertionError):
                self.fail(json_rel, "request template is missing first/last/prompt/negative/settings mapping")

        seed_json_rel = f"{seedance}/request-body.template.json"
        try:
            body = json.loads(self.read(seed_json_rel))
        except json.JSONDecodeError as exc:
            self.fail(seed_json_rel, f"invalid JSON: {exc}")
        else:
            try:
                frame_types = [item.get("frame_type") for item in body["frame_images"]]
                assert frame_types == ["first_frame", "last_frame"]
                assert body["model"] == "bytedance/seedance-2.0"
                assert isinstance(body["prompt"], str) and body["prompt"]
                assert 4 <= body["duration"] <= 15
                assert body["resolution"] == "720p"
                assert body["aspect_ratio"] == "16:9"
                assert body["generate_audio"] is True
                assert "camera_fixed" not in body
                assert "negativePrompt" not in body and "negative_prompt" not in body
            except (KeyError, IndexError, TypeError, AssertionError):
                self.fail(seed_json_rel, "request template must map both frame_type endpoints, the observed settings, and no invented keys")

        self.require_markers(
            "examples/storm-watch/target-contrast.md",
            ["SUPERSEDED", "observable submission difference", "one start image", "two endpoint images"],
        )

        demo = self.read("examples/demo-episode.md")
        for marker in (
            "Generated Canonical Worked Example",
            "Source Brief Supplied to the Skill",
            "Phase A",
            "Boundary Frame Inspection",
            "Director Package",
            "Creative-requirement transfer",
            "Run status: not run",
            "Run status: run",
            "mattress",
            "大丈夫",
        ):
            if marker.casefold() not in demo.casefold():
                self.fail("examples/demo-episode.md", f"generated detailed demo is missing {marker!r}")

        tests = self.read("examples/test-cases.md")
        case_numbers = [int(n) for n in re.findall(r"^##\s+(\d+)\.", tests, re.MULTILINE)]
        if case_numbers != list(range(1, 43)):
            self.fail("examples/test-cases.md", "must contain sequential regression cases 1 through 42")
        for marker in ("Label deletion test", "Rich direction survives target rewrite", "No imaginary Phase C", "Coupled micro-actions"):
            if marker not in tests:
                self.fail("examples/test-cases.md", f"missing key reasoning regression: {marker}")

    def validate_claim_boundaries(self) -> None:
        all_runtime = "\n".join(
            self.read(rel)
            for rel in ["SKILL.md", *self.manifest["knowledge"]["specialist_sources"], *self.manifest["knowledge"]["operational_sources"]]
        )
        if "video quality is validated" in all_runtime.casefold():
            self.fail("references", "runtime must not claim deterministic validator checks video quality")
        version = self.manifest.get("package", {}).get("version", "")
        self.require_markers(
            "README.md",
            ["canonical conforming output", "scripts/build_demo.py", "not run"],
        )
        self.require_markers(
            "CHANGELOG.md",
            [f"## {version}", "canonical artifact chain", "scripts/build_demo.py", "not run"],
        )

    def run(self) -> int:
        specialists, operational = self.validate_manifest_and_version()
        self.validate_specialist_coverage()
        self.validate_adapters(specialists, operational)
        self.validate_examples()
        self.validate_claim_boundaries()

        if self.findings:
            for finding in self.findings:
                print(f"ERROR {finding.path}: {finding.message}", file=sys.stderr)
            print(f"validation failed with {len(self.findings)} finding(s)", file=sys.stderr)
            return 1

        runtime_sources = len(self.manifest["flat"]["runtime"]["sources"])
        full_sources = len(self.manifest["flat"]["full"]["sources"])
        print("validation passed")
        print(f"- specialist references: {len(specialists)}")
        print(f"- operational references: {len(operational)}")
        print(f"- runtime flat sources: {runtime_sources}")
        print(f"- full flat sources: {full_sources}")
        print(f"- canonical worked chain: source brief → Phase A → media → inspection → {self.package_count} Phase B packages")
        print(f"- target packages: {self.package_count}; Runway and Veo not run, Seedance run with preserved evidence")
        print("- generated video quality: not evaluated")
        return 0


def main() -> int:
    try:
        return Validator(ROOT).run()
    except (FileNotFoundError, KeyError, tomllib.TOMLDecodeError) as exc:
        print(f"validation setup error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
