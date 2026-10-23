# Lehrkonzept SWE1 – Lernen mit KI-Agenten (Version 2)

**Adressaten:** Lehrende und Tutorinnen/Tutoren | **Status:** didaktischer Pilotentwurf, kein Prüfungsrecht | **Stand:** Oktober 2026

## 1. Bildungsauftrag und Ausgangslage

Studierende bearbeiten in Zweierteams über ein Semester eine Fallstudie. Als wechselnde Fälle eignen sich etwa Fundbüro, Verleihplattform und Repair-Café; in der Lehrveranstaltung kann eine Fahrkarten-/Fahrplan-App als Demonstrator dienen. Primäres Ziel ist **Software-Engineering-Kompetenz**, nicht möglichst große oder produktionsreife Software.

KI kann die technische Umsetzung beschleunigen, erzeugt aber ein didaktisches Risiko: Eine formal vollständige User Story, ein plausibles UML-Diagramm oder funktionierender Code sind **noch kein Lernnachweis**. Studierende sollen Nutzungsziele analysieren, Annahmen offenlegen, Modelle erklären, Anforderungen und Tests verknüpfen und Designentscheidungen begründen. Der Agent ist kritischer Tutor, nicht Product Owner, Abnehmer oder verbindlicher Referenzautor.

**Historische Restriktion:** Übungsblatt 1 (WS 2025/26) sah Anforderungserhebung und UML **ohne KI-Unterstützung** vor, KI beim Quellcode war erwünscht. Die in v2 vorgeschlagene KI-Challenge und das Compare-Feedback sind didaktische **Neuerungen** und benötigen ausdrückliche, gegebenenfalls zeitlich nachgelagerte Freigaben in den aktuellen Übungsblättern. Die ältere Regel darf nicht stillschweigend umgedeutet werden.

## 2. Didaktisches Prinzip: Create – Challenge – Compare – Reflect – Revise

### Create: Eigenständige Erstleistung

Personas, Ziele, Szenarien, User Stories, Use Cases, Akzeptanzkriterien und UML werden zuerst von den Studierenden entwickelt, soweit die Übung diese Leistungen verlangt. Zwischen den Phasen dürfen die Aufgaben an den Lernstand angepasst werden. Die Erstfassung wird **vor dem KI-Vergleich** gesichert oder abgegeben. Dies schützt den Vergleich vor bloßem Nachformulieren von KI-Vorschlägen.

### Challenge („Grill me“): fachlich begründete Fragen

Nach Freigabe erhält der Agent gezielte Artefakte, keine vollständige Repository-Kopie. Er fragt etwa: Welcher **Nutzerwert** ist belegt? Welche **Systemgrenze** wird vorausgesetzt? Was geschieht im **Alternativablauf**? Wie wäre eine Bedingung **beobachtbar prüfbar**? Standard: höchstens drei Fragen je Runde, in der Regel zwei Runden, danach Antwort abwarten. Die Begrenzung dient kognitiver Fokussierung und Tokenökonomie, darf für besondere Lernfälle didaktisch überschrieben werden.

Die Qualität der Fragen ist wichtiger als die Anzahl. Sie sollen **Begründungen** evozieren, nicht durch rhetorische Fragen bereits die Antwort liefern. Bei angemessener Antwort kann der Tutor den Punkt auch ausdrücklich als Stärke einordnen.

### Compare: unabhängiger, bewusst begrenzter Vergleich

**Nur nach vorhandener studentischer Erstfassung und gesonderter Freigabe.** Der Agent formuliert aus den freigegebenen Ausgangsartefakten (Persona/Ziele/Szenario und in der Challenge geklärten Antworten) einen **vorläufigen**, begrenzten Referenzvorschlag. Für Requirements beispielsweise 2–3 Stories, ein strukturierter Use Case mit einem Alternativablauf und wenige exemplarische Akzeptanzkriterien. Danach werden beide Fassungen nach Nutzerwert, Systemgrenze, Konsistenz, Alternativen und Prüfbarkeit verglichen.

„Unabhängig“ bedeutet hier **nicht** objektiv oder frei von Kontextbeeinflussung: Antworten aus der Challenge können bereits Lösungen enthalten. Die Alternative ist eine zweite fachliche Perspektive, **keine Musterlösung**. Zusätzliche Annahmen und mögliche falsche Interpretationen müssen sichtbar sein. Eine legitime Studentenversion darf vom KI-Vorschlag abweichen.

### Reflect: Missverständnisse korrekt klassifizieren

Ein kurzer Learning Report (optional `docs/learning/LERNBERICHT-VORLAGE.md`) enthält bis zu fünf relevante Befunde:

| Kategorie | Evidenzanforderung | Beispiel |
|---|---|---|
| **Belegtes Missverständnis** | Aussage/Artefakt **widerspricht** geklärtem Begriff oder Quelle; Beleg nennen | Ein externer Akteur wurde trotz vereinbarter Systemgrenze als interne Komponente verstanden |
| **Informationslücke** | Wichtige Angabe fehlt, Ursache ist **nicht** als Unverständnis erwiesen | Stornierungsfrist im Szenario nicht beschrieben |
| **Offene Entscheidung** | Mehrere plausible Varianten, noch nicht entschieden | Wie lange gilt eine Reservierung? |
| **Vertretbare Alternative** | Andere, begründbare Modellierung | Zwei geeignete Zerlegungen eines Use Cases |
| **Stärke** | Korrekte, nachvollziehbare studentische Entscheidung | Testbares Kriterium mit klarer Beobachtung |

Der Agent führt keine psychologische Diagnose durch. Ein Missverständnis soll nur bei konkret beobachtetem Widerspruch so bezeichnet werden. Die Dokumentation dient **formativer Rückmeldung**, nicht automatisch der Benotung.

### Revise: begründete Überarbeitung

Studierende entscheiden, ob sie Anforderungen, Modell oder Code ändern. Ein Compare-Vorschlag **ändert den genehmigten Stand nicht**. Anforderungen dürfen nicht nachträglich an fehlerhaften Code angepasst werden. Ein Lernziel kann bereits erreicht sein, wenn eine gut begründete Alternative **beibehalten** wird.

## 3. Verankerung in klassischen SWE-Methoden

### Requirements Engineering (in Anlehnung an Sommerville)

Aus Nutzungskontext und Stakeholder-Zielen werden Szenarien abgeleitet, diese in strukturierte Use Cases und in kleinere User Stories überführt; funktionale und Qualitätsanforderungen sowie Akzeptanzkriterien sichern Klarheit und Prüfbarkeit. **Dies ist ein didaktischer Weg, keine behauptete zwingende Reihenfolge.** Typische Challenge-Dimensionen: Ziel vs. Lösungsidee, Systemgrenze, Haupt-/Alternativablauf, Daten- und Qualitätsannahmen, Traceability, Stakeholder-Konflikte.

Der Agent darf Vorschläge nicht als genehmigte Requirements ausgeben und soll keine zusätzlichen Dienste (z. B. Identitätsanbieter oder Zahlungssystem) voraussetzen, wenn diese nicht gefordert sind.

### UML und objektorientierter Entwurf

Use-Case-, Objekt-, Klassen-, Aktivitäts-, Zustands- und Komponentendiagramme modellieren verschiedene Sichten. Ein `uml-review` prüft getrennt (a) Werkzeug-/PlantUML-Renderbarkeit, (b) UML-Notation und (c) fachliche Passung. Gerade Multiplizitäten, Kompositionen, Zustände, Entscheidungsknoten und Komponenteninterfaces laden zu Verständnisfragen ein. Grafische UML-Werkzeuge bleiben zugelassen, wo PlantUML eine unterrichtete Notation nicht angemessen abbildet.

### Wasserfall / V-Modell: Verifikation und Validierung

Traditionelle Phasen (Anforderungen, System-/Komponentenentwurf, Implementierung, Test) strukturieren die **Arten der Entscheidungen**, ohne das Semester auf ein reines Wasserfallverfahren festzulegen. Die V-Modell-Perspektive koppelt Entwicklungsartefakte an Prüfaktivitäten:

| Entwickeln / Spezifizieren | Passende Prüfung | Leitfrage |
|---|---|---|
| Persona, Stakeholder-Ziel, Szenario | Nutzungsbezogene **Validierung** | Entwickeln wir das richtige System für den Nutzer? |
| Anforderungen / Akzeptanzkriterien | Akzeptanz-/Systemtests | Erfüllt das System die beschriebenen Erwartungen? |
| Komponenten und Schnittstellen | Integrationsprüfung | Funktionieren die vereinbarten Interaktionen? |
| Klassen, Methoden, Algorithmen | Unit- und Komponententests | Entspricht die Implementierung dem Entwurf/Vertrag? |

**Verifikation** prüft Übereinstimmung mit einer Spezifikation, **Validierung** Eignung für den tatsächlichen Zweck. Die erfolgreiche Ausführung eines Tests ist keine automatische Validierung eines Bedürfnisses.

### Iterativ-inkrementelle Entwicklung / Scrum

Nach der Erarbeitung ausreichender, priorisierter Stories entsteht ein kleiner Product Backlog. Team und Lehrende können an Scrum angelehnte Praktiken einsetzen: Priorisierung, Sprintziel, Sprint Review, Retrospektive, Definition of Done, Story Points und ggf. Burndown. Zweierteams sollen dabei **keine simulierte Großorganisation** nachbauen. Kleine implementierte Inkremente werden getestet und geprüft; fachliches Feedback kann eine neue **Iteration** über bestehendes Verhalten auslösen.

Die Verbindung mit dem Challenge-Zyklus ist methodisch: Anforderungen werden **verstanden** und geprüft, Code wird **begrenzter Umfang** der Spezifikation, Tests liefern **Evidenz**, Reviews prüfen **Nutzerwert und Lernwert**. Negative Testergebnisse sind wertvolle Hinweise, die sichtbar bleiben müssen.

## 4. Kompetenzziele nach Anderson/Krathwohl (revidierte Bloom-Taxonomie)

**Stufen:** 1 Erinnern, 2 Verstehen, 3 Anwenden, 4 Analysieren, 5 Bewerten, 6 Erschaffen. Die Einstufung bezieht sich **immer auf beobachtbare studentische Leistung**, niemals auf die Fähigkeit des Agents.

| Skill | Lernziel – Studierende können … | Stufe | Lernnachweis |
|---|---|---|---|
| `requirements-coach` | Nutzerwert und Systemgrenze analysieren, Anforderungen vergleichen, eigene Stories/Use Cases begründet überarbeiten | 4–6 | Vorher-/Nachher-Stelle mit Begründung und ein prüfbares AC |
| `uml-review` | Beziehungen, Abläufe, Zustände oder Schnittstellen erklären und alternative Modellierung bewerten | 4–5 | Korrektur/Beibehaltung eines UML-Elements mit Gegenbeispiel |
| `architecture-review` | Verantwortlichkeiten/Kopplung analysieren und einen Schnittstellenentscheid begründen | 4–5 | Kurze Entscheidung mit Qualitätsziel und Trade-off |
| `implement-story` | relevante Methoden auf AK beziehen und Kontrollfluss/testbares Verhalten erklären | 3–4 | Zuordnung Story → Methode → Test und Peer-Erklärung |
| `test-coach` | Positiv-, Negativ- und Grenzfälle herleiten und Testaussage bewerten | 3–5 | nachvollziehbare Testfälle inkl. erwarteter Resultate |
| `debug-coach` | Fehler reproduzieren, Hypothesen gegenüberstellen und Gegenprobe interpretieren | 3–5 | Symptom → Hypothese → Beleg → Resultat |
| `model-code-review` | Modell-/Codeunterschiede erkennen und fachliche Widersprüche von zulässigen Abstraktionen unterscheiden | 4–5 | begründete Entscheidung Modell/Code/beides/unverändert |

**Erschaffen (6)** erfordert eine von Studierenden **selbst** verantwortete schöpferische Modell- oder Revisionsentscheidung. Ein generierter Referenzentwurf reicht nicht. Reflexionsfragen sind **in die sieben Skills integriert**, damit ein achter Meta-Skill nicht bloß Tokenkosten erhöht.

## 5. Lernorientierte statt produktionsoptimierte Implementierung

Code soll **verständlich, korrekt, hinreichend sicher, gut veränderbar und beobachtbar testbar** sein. Zu diesem Kursziel passen sprechende Namen, explizite Kontrollflüsse, geringe Abhängigkeitszahl, kohärente Module und wenige zweckmäßige Schnittstellen. „Größere Module“ sind **keine pauschale Empfehlung**: Zu viele Mini-Klassen erschweren das Verständnis, unübersichtliche God Classes aber ebenso. Für die Lernphase wird die **einfachste angemessene Zerlegung** bevorzugt.

Nicht notwendig sind per se Microservices, komplexe Dependency-Injection-Systeme, ORM, Event Bus oder abstrahierte Test-Infrastruktur. Solche Mittel dürfen eingesetzt werden, **wenn** eine Lernaufgabe oder ein Qualitätsziel sie begründet. Sicherheits- und Datenschutzaspekte, korrekte Fehlerbehandlung sowie die Akzeptanzkriterien dürfen nicht dem Minimalismus geopfert werden.

**Doppelte Ergebnisperspektive:**

1. **Artefaktqualität:** stimmt das Verhalten mit den freigegebenen Anforderungen überein, sind relevante Tests aussagekräftig, sind Mängel transparent?
2. **Lernqualität:** können beide Teammitglieder fachliche Entscheidung, Codepfad, Fehlerdiagnose und Testbeleg erklären?

Eine nicht feature-komplette, gut verstandene, sauber getestete Anwendung kann ein besseres SWE1-Lernergebnis sein als eine umfangreiche, unverstandene KI-Implementierung. Die fachlich vereinbarten Aufgaben und Sicherheitsanforderungen sind dennoch bindend.

## 6. Nutzungsrechte, Freigaben und zeitliche Entkopplung

Der Skill steuert Verhalten, aber **keine Prüfungsberechtigung**. Je Phase können unterschiedliche Freigaben gelten: z. B. (a) erste Personas/Szenarien ohne KI, (b) nach Abgabe Challenge erlauben, (c) nach erster eigener Story-/Use-Case-Version auch Compare erlauben, (d) Codegenerierung zu freigegebenen User Stories erlauben. Diese Staffelung muss **explizit** in Übungsblatt und `docs/SEMESTERREGELN.md` stehen.

Eine Möglichkeit ist, die studentische Erstfassung mit Git-Commit oder Abgabesnapshot zu sichern, **ohne** dass der Agent selbst commits erstellt. Nach der Challenge ist die Erstfassung immer noch identifizierbar. In benoteten Phasen braucht es ergänzende Eigenleistungen ohne KI, da Agent-Anweisungen keine Verhaltensgarantie liefern.

## 7. Tokenökonomie und didaktische Kosten

Die Strategien sind nicht als Sparen an der Prüfung, sondern als **Reduktion redundanter Kontextarbeit** zu verstehen:

- knappe globale `AGENTS.md` und nur gezielt aktivierter Skill;
- keine pauschale Aufnahme sämtlicher `docs/` oder aller `.puml`-Dateien;
- kleine Ausschnitte und kurze Challenge-Runden (3 Fragen, meist max. 2 Runden);
- erst bei vorhandener eigenständiger Erstlösung kompakter Compare-Vorschlag;
- Lernreport bis zu fünf Befunde statt Chattranskript;
- lokales Rendern, Kompilieren und Testen ohne erneuten KI-Aufruf;
- Scope statt großer unaufgeforderter Refactorings; bestehende Testwerkzeuge verwenden.

Eine fixe Tokenersparnis wird nicht garantiert. Agenten können durch zusätzliche Dateien, lange Kontexte oder automatische Tool-Aufrufe trotzdem mehr verbrauchen. Bei einer Evaluation sind **Lernertrag pro Interaktion** und Verifikation mindestens so wichtig wie Verbrauch.

## 8. Formative Auswertung und Peer Learning

| Beobachtung | Positive Evidenz | Warnsignal |
|---|---|---|
| Selbstständige Anforderungsanalyse | Team erklärt Nutzerziel, Grenze und Ausnahme | KI-Vorschlag wird ohne Prüfung kopiert |
| Modellverständnis | Studierende erläutern UML-Relation an konkretem Gegenbeispiel | nur Syntaxkorrekturen; Fachmodell bleibt unklar |
| Technisches Verständnis | beide können Kontrollfluss und Verantwortlichkeiten erklären | viele generierte Klassen, niemand kennt die Gründe |
| Testqualität | Fehler- und Grenzfall mit erwarteter Beobachtung | „alles grün“, aber Tests wurden nicht ausgeführt |
| Zusammenarbeit | zweites Teammitglied kann eine Änderung reviewen | Agent ersetzt fachliche Teamdiskussion |
| Reflexion | Befunde sind belegt, Alternativen als solche benannt | Lücken werden pauschal als „Missverständnis“ bewertet |

**Learning Check** (ca. 2 Minuten nach substantiellen Änderungen): Welches Ziel/AC war ausschlaggebend? Warum diese Modell- oder Codeentscheidung? Welcher Test würde eine Fehlinterpretation zeigen? Wo bleibt Unsicherheit?

## 9. Pilotierung und Evaluation

1. Freigabe **nur für den künstlichen Pilot** erteilen (nicht für studentische Prüfungsartefakte).
2. Im Code-Agenten `requirements-coach` mit `examples/pilot/persona-ziele-szenario.md` starten; Antworten und Fragen prüfen.
3. Erst danach `studentischer-entwurf.md` zulassen und Compare/Report bewerten.
4. UML-Review und Java-Fehlerdiagnose mit demselben Fall testen.
5. Einmal KI-Verbot simulieren; Agent darf keine konkrete Musterlösung erzeugen.
6. Stichprobe bei Studierenden: 1–2 Verständnisfragen und Peer-Erklärung; optional aggregierte Tokenstatistik und Anzahl ausgeführter Tests.

Messgrößen: Regelkonformität, **Fragequalität**, Belegbarkeit der Lernberichte, studentisches Verständnis, tatsächliche Verifikation, knappes Antwortformat. Pilotabläufe stehen in [`PILOT-SZENARIEN.md`](PILOT-SZENARIEN.md); `scripts/check_repo.py` validiert lediglich das Repo-Gerüst, **nicht** das Agent-Verhalten.

## 10. Quellenbasis und Abgrenzungen

**Kursmaterial im Projektkontext, nicht automatisch Bestandteil des Repositorys:** Übungsblatt 1 (WS 2025/26: Eigenleistung RE/UML, KI-Coding), Übungsblatt 2 (Klassendiagramm), Übungsblatt 3 (Komponenten und Coding-Umgebung), Übungsblatt 4 (Aktivitätsdiagramm und Java-Code), Übungsblatt 5 (Personas, Szenarien, strukturierte Use Cases, Stories, nichtfunktionale Anforderungen), Übungsblätter 6–8 (WS 2024/25: Kriterien, Backlog/Sprints, Aufwandsschätzung, Wireframe/Architektur). Folien „Vorgehensmodelle 2“ vom 10.12.2025: Wasserfall/V-Modell, Verifikation/Validierung, Scrum, Iteration/Inkrement, Definition of Done und Prototyping.

**Theorie:** Anderson, L. W. & Krathwohl, D. R. (Hrsg., 2001): *A Taxonomy for Learning, Teaching, and Assessing* (revidierte Bloom-Taxonomie). Sommerville, I.: *Software Engineering* (Requirements Engineering, Modellierung, Architektur und iterative Entwicklung). Diese **Challenge–Compare–Reflect-Ausprägung** mit Lernberichten und Skill-Namen ist **eine eigene didaktische Konzeption**, keine wörtlich übernommene Methode aus den Quellen.

**Technische Quellen:** [Agent Skills Specification](https://agentskills.io/specification), [VS Code – Agent Skills](https://code.visualstudio.com/docs/agent-customization/agent-skills). Nutzung und Skill-Erkennung können je nach Editor/Agent-Version variieren. Das vorliegende v2 wurde nicht innerhalb einer realen Codex-/Copilot-Sitzung pilotiert.
