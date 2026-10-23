# Software Engineering 1 – KI als Lernpartner

**Vorlage für Zweierteams im Semester.** Ihr bearbeitet eure eigene Fallstudie. Die KI soll euer Verständnis herausfordern und beim Coding helfen – nicht möglichst schnell eine perfekte Anwendung produzieren.

> **Vor jeder KI-Nutzung:** aktuelles Übungsblatt und [`docs/SEMESTERREGELN.md`](docs/SEMESTERREGELN.md) lesen. Ein Skill ist **keine** Erlaubnis, eine eigenständig zu lösende Aufgabe mit KI bearbeiten zu lassen. Die Freigaben für Challenge und Compare können verschieden sein.

## Einstieg

1. Dieses Repository als Teamvorlage übernehmen und in VS Code oder einer kompatiblen Arbeitsumgebung öffnen.
2. Aktuelle Aufgaben und KI-Freigaben prüfen. Die drei möglichen Fallstudien (Fundbüro, Verleihplattform, Repair-Café) sind **Beispiele**, keine festgelegten Anforderungen.
3. Eigene Personas, Ziele, Szenarien und weitere Artefakte in [`docs/`](docs/README.md) speichern.
4. Erst nach Freigabe einen passenden Skill aufrufen. Bei Codeaufträgen die konkrete Story und Akzeptanzkriterien nennen.
5. Nach jeder größeren Änderung: selbst erklären, lokal prüfen und mit dem zweiten Teammitglied besprechen.

Diese Vorlage enthält absichtlich **keinen Anwendungs-Stack**. Die Java-Dateien in `examples/pilot/` sind ausschließlich ein optionaler Demonstrationsfall.

## Was ist ein Agent Skill?

Ein **Agent Skill** ist eine wiederverwendbare Arbeitsanweisung für einen KI-Agenten. Er erklärt, **wann** eine Methode sinnvoll ist, **welche Eingaben** benötigt werden, **wie** der Agent arbeitet und **wie** ihr Ergebnisse selbst überprüft. Jeder Skill liegt als `.agents/skills/<name>/SKILL.md` vor. `AGENTS.md` enthält dagegen allgemein gültige Leitplanken; `docs/` gehört zu **eurem** Projekt.

## Unser Lernzyklus: Create → Challenge → Compare → Reflect → Revise

| Schritt | Was passiert? | Wer entscheidet? |
|---|---|---|
| **Create** | Ihr erstellt eine erste Fassung eigenständig. | Studierende |
| **Challenge („Grill me“)** | Der Tutor stellt maximal drei kritische Fragen pro Runde; meist zwei Runden. Er wartet auf eure Antworten. | Studierende beantworten |
| **Compare** | Nur nach eigener Erstfassung und gesonderter Freigabe: Der Tutor zeigt einen **vorläufigen** Alternativvorschlag und gleicht Unterschiede ab. | Studierende bewerten |
| **Reflect** | Kurzer Lernbericht: belegte Missverständnisse, Lücken, offene Entscheidungen, Alternativen und Stärken. | Studierende prüfen |
| **Revise** | Ihr entscheidet, ob und wie ihr euer Artefakt verbessert. | Studierende |

**Wichtig:** Ein KI-Vorschlag ist keine Musterlösung und wird nicht automatisch Teil der freigegebenen Spezifikation. Eine Abweichung ist nicht zwingend ein Fehler. Der Agent darf **nur belegte** Missverständnisse als solche bezeichnen.

## Beispiel: Requirements „Grill me“

Ihr legt eure selbst erstellten **Personas, Ziele und Szenarien** ab, etwa in `docs/scenarios/`. Erst wenn eine Reviewphase erlaubt ist:

```text
Nutze requirements-coach im Challenge-Modus.
Lies nur docs/scenarios/persona.md, ziele.md und szenario.md.
Grill me zur Systemgrenze, zum Nutzerwert und zu Ausnahmen.
Stelle höchstens 3 Fragen und warte jeweils auf unsere Antworten.
Noch keine Stories, Use Cases oder Akzeptanzkriterien ausgeben.
```

Danach schreibt ihr eure **eigene** erste Fassung von User Stories, Use Cases und Akzeptanzkriterien. Wenn die Lehrperson den **Compare-Modus** gesondert erlaubt hat:

```text
Nutze requirements-coach im Compare-Modus.
Unsere erste Fassung liegt in docs/user-stories/ und docs/use-cases/.
Erzeuge aus den zuvor gelesenen Ausgangsartefakten einen kleinen,
als vorläufig gekennzeichneten Vergleichsentwurf und gleiche ihn
mit unserer Fassung ab. Erfinde keine Anforderungen ohne Annahme.
Fasse höchstens fünf Lernpunkte nach der Lernbericht-Vorlage zusammen.
Ändere keine Spezifikationsdatei.
```

**Warum die zwei Schritte?** So erarbeitet ihr eine Lösung, bevor ihr euch an Vorschlägen der KI orientiert. Das KI-Feedback kann Irrtümer sichtbar machen, ohne eure Eigenleistung zu ersetzen.

## Skills und überprüfbare Lernziele

Die Stufen beziehen sich auf die revidierte **Bloom-Taxonomie nach Anderson und Krathwohl**: 3 Anwenden, 4 Analysieren, 5 Bewerten, 6 Erschaffen. Es wird eure Leistung beurteilt, nicht die der KI.

| Skill | Wann? | Lernziel (Stufe) |
|---|---|---|
| [`requirements-coach`](.agents/skills/requirements-coach/SKILL.md) | Eigene Personas/Szenarien und später Stories/Use Cases hinterfragen | Nutzerziele und Annahmen analysieren, Kriterien bewerten und eigenständig überarbeiten (4–6) |
| [`uml-review`](.agents/skills/uml-review/SKILL.md) | Ein **eigenes** UML-Modell verstehen und ggf. vergleichen | Modellierungsentscheidungen analysieren und begründen (4–5) |
| [`architecture-review`](.agents/skills/architecture-review/SKILL.md) | Vorhandene Komponenten-/Architekturskizzen kritisch betrachten | Kopplung und Schnittstellen bewerten (4–5) |
| [`implement-story`](.agents/skills/implement-story/SKILL.md) | Eine freigegebene, kleine Story ausdrücklich implementieren | Code erklären und Akzeptanzkriterien zuordnen (3–4) |
| [`test-coach`](.agents/skills/test-coach/SKILL.md) | Eigene Testideen hinterfragen und Tests überprüfen | Positiv-/Grenz-/Negativfälle ableiten und bewerten (3–5) |
| [`debug-coach`](.agents/skills/debug-coach/SKILL.md) | Fehlverhalten reproduzieren und untersuchen | Hypothesen überprüfen und Fehlerursachen begründen (3–5) |
| [`model-code-review`](.agents/skills/model-code-review/SKILL.md) | Nach Freigabe Modell gegen Code abgleichen | Bewusste Abstraktion und echte Widersprüche unterscheiden (4–5) |

Sagt dem Agenten ausdrücklich, welchen Skill und Modus ihr verwenden wollt. Viele kompatible Umgebungen bieten Skill-Auswahl über das Chat-Menü oder `/` an; Details können sich ändern. **Skills werden nicht garantiert automatisch ausgewählt.**

## Code: Verständlichkeit vor technischer Perfektion

Für SWE1 gilt: **einfach, korrekt, nachvollziehbar, testbar**. Bevorzugt sprechende Namen, überschaubare Kontrollflüsse, fachlich zusammenhängende Module, wenige Abhängigkeiten und kleine Inkremente. Vermeidet unnötige Muster, Frameworks, Services, abstrakte Basisklassen und künstliche Kleinstmodule. Diese Regel erlaubt **keine** unsichere oder kaputte Software: Freigegebene Akzeptanzkriterien und relevante Qualitätsanforderungen gelten weiterhin.

Beispielprompt:

```text
Nutze implement-story. Implementiere ausschließlich das erste
Akzeptanzkriterium von docs/user-stories/US-01.md.
Prüfe vorher die zugehörigen Anforderungen und betroffenen Dateien.
Bevorzuge einfache, verständliche Klassen ohne zusätzliche Schicht.
Führe vorhandene Tests aus und erkläre die zentrale Änderung kurz.
```

Beim Test-/Debugging-Chat zuerst nach **Beobachtung** und **eigener Hypothese** fragen, nicht direkt das ganze Programm ersetzen lassen. Failing Tests dürfen nicht „grün geredet“ werden.

## Tokenbudget: kurze, wertvolle Dialoge

- **Ein Ziel pro Auftrag:** ein Artefakt/ein Fehler/eine Story, nicht das gesamte Repo analysieren.
- **Pfade statt Dateidumps:** nur benötigte Dateien nennen, keine kompletten Chatauszüge erneut senden.
- **Ein Skill je Phase:** nicht alle Skills pauschal laden; keine langen Standardberichte.
- **Drei Fragen pro Runde:** zuerst antworten, dann bei Bedarf vertiefen; normalerweise nach zwei Runden vergleichen.
- **Kleiner Vergleich:** kein komplettes Soll-System. Lernbericht höchstens fünf relevante Punkte.
- **Lokal prüfen:** Git-Diff, Compiler, Test und ggf. PlantUML-Preview statt wiederholter KI-Anfragen.
- **Neuen Chat** bei unabhängigen Aufgaben beginnen, dafür lediglich relevante Entscheidungen/Pfade referenzieren.

Tokenverbrauch hängt von Werkzeug und Modell ab. Nicht durch Weglassen wichtiger Tests oder Sicherheitsfragen sparen.

## Dateien im Repository

```text
AGENTS.md                      globale, kurze Agent-Regeln
.agents/skills/*/SKILL.md      7 spezifische Lern-Workflows
docs/SEMESTERREGELN.md         Freigaben, vor Semesterstart festzulegen
docs/scenarios/                eigene Personas, Ziele und Szenarien
docs/user-stories/             eigene Stories und Akzeptanzkriterien
docs/use-cases/                eigene strukturierte Anwendungsfälle
docs/requirements/             funktionale und Qualitätsanforderungen
docs/uml/                      UML (optional PlantUML)
docs/architecture/             Schnittstellen und Entscheidungen
docs/learning/                 optionaler kurzer Learning Report
docs/lehrende/                 didaktisches Konzept / Pilotanleitung
examples/pilot/                **künstlicher** Testfall, kein Projektcode
scripts/check_repo.py          lokale Struktur-/Skill-Kontrolle
```

### PlantUML

Das textbasierte `.puml`-Format unterstützt Git-Diffs und KI-Analyse. Andere UML-Werkzeuge oder Papier bleiben zulässig, insbesondere bei komplexen Aktivitäts- und Komponenten-Notationen. Ein renderbares Diagramm ist **nicht automatisch** fachlich korrekt.

## Pilot und Teamarbeit

Einen **gefahrlosen Probelauf** mit einem künstlichen, absichtlich fehlerhaften Beispiel findet ihr in [`examples/pilot/README.md`](examples/pilot/README.md). Lehrende können mit [`docs/lehrende/PILOT-SZENARIEN.md`](docs/lehrende/PILOT-SZENARIEN.md) kontrollieren, ob der Agent die Grenzen einhält. Für die Datei-/Skill-Prüfung (optional Python 3, Standardbibliothek):

```bash
python3 scripts/check_repo.py
```

**Das Repo wurde nicht in Codex/Copilot durch eine echte Agent-Sitzung geprüft.** Der Pilot dient genau diesem Test. Das Repository ist eine Vorlage, kein fertiges GitHub-Repository. Jede Zweiergruppe dokumentiert Entscheidungen, lässt Änderungen gegenlesen und verantwortet ihre Abgabe. Für Lehrende: [`LEHRKONZEPT.md`](docs/lehrende/LEHRKONZEPT.md).
