# SWE1 – Übung 3, WS 2026/27

Minimale Repository-Vorlage für die eigenständige Anforderungsanalyse und UML-Modellierung im Zweierteam.

Die drei Fallstudien sind **Fundbüro**, **Peer-to-Peer-Verleih** und **Repair-Café**. Den konkreten Umfang legt das aktuelle Übungsblatt fest; technische und fachliche Entwurfsentscheidungen werden dadurch nicht vorweggenommen.

## Struktur

```text
.agents/skills/
├── requirements-coach/SKILL.md
└── noun-extraction/.gitkeep
.github/copilot-instructions.md
AGENTS.md
README.md
.gitignore
docs/
├── 01-anforderungen/.gitkeep
├── 02-review/.gitkeep
└── 03-objektmodell/.gitkeep
kurs/uebung-03.md
```

- [docs/01-anforderungen/](docs/01-anforderungen/): eigene Anforderungsartefakte.
- [docs/02-review/](docs/02-review/): freigegebenes Review und Reflexion.
- [docs/03-objektmodell/](docs/03-objektmodell/): eigene Objektmodelle und UML-Artefakte.
- [kurs/uebung-03.md](kurs/uebung-03.md): KI-Freigaben für Übung 3 und Verweis auf das vollständige Übungsblatt.
- [AGENTS.md](AGENTS.md): allgemeine Regeln für KI-Assistenten.

Die `.gitkeep`-Dateien halten die zunächst leeren Verzeichnisse in Git fest. `docs/` gehört dem studentischen Team; `kurs/`, `AGENTS.md` und `.agents/skills/` werden durch den Kurs gepflegt.

## KI-Nutzung

Für die KI-Nutzung gelten [AGENTS.md](AGENTS.md) und die [Freigaben für Übung 3](kurs/uebung-03.md).

Der bestehende [requirements-coach](.agents/skills/requirements-coach/SKILL.md) bleibt erhalten. Für `noun-extraction` ist lediglich ein Verzeichnis reserviert; dieser Skill ist noch nicht implementiert.
