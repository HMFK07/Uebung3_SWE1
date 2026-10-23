#!/usr/bin/env python3
"""Prüft die Repo-Vorlage ohne zusätzliche Bibliotheken (nicht das Agentverhalten)."""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = {
    "requirements-coach", "uml-review", "architecture-review",
    "implement-story", "test-coach", "debug-coach", "model-code-review",
}
REQUIRED = {
    "AGENTS.md", "README.md", "docs/SEMESTERREGELN.md",
    "docs/learning/LERNBERICHT-VORLAGE.md",
    "docs/lehrende/LEHRKONZEPT.md", "docs/lehrende/PILOT-SZENARIEN.md",
    "examples/pilot/persona-ziele-szenario.md",
    "examples/pilot/studentischer-entwurf.md",
}
issues = []
for path in sorted(REQUIRED):
    if not (ROOT / path).is_file():
        issues.append(f"Fehlende Datei: {path}")

base = ROOT / ".agents" / "skills"
actual = {p.name for p in base.iterdir() if p.is_dir()} if base.is_dir() else set()
if actual != SKILLS:
    issues.append(f"Skill-Namen stimmen nicht: erwartet {sorted(SKILLS)}, gefunden {sorted(actual)}")

for name in sorted(SKILLS):
    file = base / name / "SKILL.md"
    if not file.is_file():
        issues.append(f"Skill fehlt: {file.relative_to(ROOT)}")
        continue
    content = file.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", content, flags=re.S)
    if not match:
        issues.append(f"Ungültiges Frontmatter: {name}")
        continue
    lines = match.group(1).splitlines()
    fields = dict(line.split(":", 1) for line in lines if ":" in line)
    if fields.get("name", "").strip() != name:
        issues.append(f"Name im Header entspricht nicht dem Verzeichnis: {name}")
    description = fields.get("description", "").strip()
    if not description or len(description) > 1024:
        issues.append(f"description fehlt/zu lang: {name}")
    if len(content) > 5000:
        issues.append(f"Skill für den Pilot ungewöhnlich lang (>5000 Zeichen): {name}")

for file in sorted((ROOT / "README.md", ROOT / "docs" / "lehrende" / "LEHRKONZEPT.md")):
    text = file.read_text(encoding="utf-8")
    if "requirements-review" in text:
        issues.append(f"Alter Skillname in {file.relative_to(ROOT)}")


# Validate relative Markdown links so students can navigate the documentation.
for doc in ROOT.rglob("*.md"):
    body = doc.read_text(encoding="utf-8")
    for destination in re.findall(r"(?<!!)\[[^\]\n]*\]\(([^)]+)\)", body):
        if destination.startswith(("http://", "https://", "mailto:", "#")):
            continue
        target = (doc.parent / destination.split("#", 1)[0]).resolve()
        if not target.exists():
            issues.append(f"Fehlender lokaler Link in {doc.relative_to(ROOT)}: {destination}")

if issues:
    print("Strukturprüfung FEHLGESCHLAGEN:")
    for item in issues:
        print(" - " + item)
    sys.exit(1)

print(f"Strukturprüfung BESTANDEN: {len(SKILLS)} Skills, {len(REQUIRED)} Pflichtdateien.")
print("Hinweis: Keine UML-Semantik, keine Lernziele und kein Agent-Verhalten getestet.")
