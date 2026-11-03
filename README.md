# SWE1 – Übung 3, WS 2026/27

Ihr überprüft eure bisherigen Anforderungen und erstellt erste UML-Modelle. Arbeitet im Zweierteam an eurer Fallstudie: **Fundbüro-Anwendung**, **Verleih-Plattform** oder **Repair-Café-Anwendung**. Ziel ist eine kleine, verständliche Lehranwendung; den [Lernrahmen und die KI-Freigaben](kurs/uebung-03.md) findet ihr in den Kurshinweisen.

Maßgeblich sind [Übungsblatt 3](https://docs.google.com/document/d/1lnprAB5V6oSyTlOZC8MchO9pPu3UpWEvFekyI5NcVGg/edit) und die allgemeinen Regeln in [AGENTS.md](AGENTS.md).

## Einstieg in Copilot

Ein Skill ist eine Arbeitsanweisung für den KI-Agenten. Dieser kann Dateien lesen und Werkzeuge nutzen. Ihr wählt die Aufgabe und die Quellen bewusst aus und prüft das Ergebnis.

Der folgende Einstieg beschreibt **GitHub Copilot in VS Code**:

- Öffnet den Repository-Ordner in VS Code und meldet euch bei Copilot an.
- Öffnet den Copilot-Chat und beginnt einen neuen Chat. Tippt `/` und wählt den benötigten Skill aus der Liste.
- Nennt nur die benötigten Dateien und einen kleinen Abschnitt. Ersetzt die Platzhalter in den folgenden Startprompts durch eure eigenen Pfade und Angaben.

Fehlen die Skills im Menü, prüft die Einrichtung mit der Lehrperson. Für andere IDEs, etwa IntelliJ, muss die Erkennung in der verwendeten Copilot-Version ebenfalls geprüft werden.

## 1. Anforderungen erfassen

Wählt unter [docs/01-anforderungen/](docs/01-anforderungen/) eure Ausgangsvision, löscht die zwei anderen Visionsdateien und benennt die verbleibende Datei in `vision.md` um.

Legt dort eure selbst erarbeiteten Personas, Szenarien, User Stories und strukturierten Anwendungsfälle aus Übung 1 sowie die funktionalen und nichtfunktionalen Anforderungen einschließlich Akzeptanzkriterien aus Übung 2 ab.

## 2. Anforderungen analysieren

Notiert zuerst selbst eine vermutete Unklarheit und eure bisherige Begründung. Startet dann den [requirements-coach](.agents/skills/requirements-coach/SKILL.md) im **Challenge-Modus**, beispielsweise so:

```text
/requirements-coach
Lies nur <Pfad zum Anforderungstext> und <benötigte Kontextdatei>.
Prüfe zunächst <ID oder Abschnitt>.
Unsere eigene Unsicherheit: <Frage und bisherige Begründung>.
Beginne mit einer Runde und warte auf unsere Antworten.
```

Der Coach stellt bevorzugt zwei, höchstens drei quellengestützte Fragen pro Runde. Beantwortet sie im Team; entscheidet danach, ob ihr zu einem offenen Punkt eine weitere Runde benötigt. Beendet das Review ausdrücklich, sobald ihr die ausgewählten Punkte besprochen habt. Fertige Formulierungen, Musterlösungen und Compare sind nicht freigegeben.

Dokumentiert mindestens drei Review-Erkenntnisse und eure Entscheidungen unter [docs/02-review/](docs/02-review/). Überarbeitet selbst mindestens zwei Anforderungen oder Akzeptanzkriterien und begründet die Klarstellungen. Prüft KI-Hinweise an euren Quellen und begründet auch abgelehnte Hinweise; KI-Kritik allein ist kein Änderungsgrund. Erklärt euch anschließend ohne KI, warum eure Änderung sinnvoll und überprüfbar ist.

## 3. Substantive extrahieren

Beginnt einen **neuen Chat**, damit Persona und Review-Dialog nicht als zusätzlicher Kontext vorliegen. Nutzt [noun-extraction](.agents/skills/noun-extraction/SKILL.md) nur mit funktionalen Anforderungen, User Stories oder Use Cases:

```text
/noun-extraction
Lies nur <Pfad zum Anforderungstext>, Abschnitt <ID oder Abschnitt>.
Extrahiere nur aus diesem Abschnitt die verwendeten Substantive.
```

Der Skill liefert Grundformen, fachliche Mehrwortbegriffe und Fundstellen. Bei Teilausgaben nennt er den bearbeiteten und verbleibenden Umfang. Er liest keine Persona, ordnet keine Modellelemente zu und erzeugt keine UML-Diagramme. Die Spalten für studentische Einordnung und Begründung bleiben in seiner Ausgabe leer.

Prüft einige Einträge selbst am Originaltext, insbesondere Grundform, Mehrwortbegriffe und Fundstelle. Übernehmt die Liste nach [docs/03-objektmodell/](docs/03-objektmodell/) und wertet sie eigenständig fachlich aus.

## 4. Objektdiagramm erstellen

Wählt einen konkreten Zeitpunkt innerhalb eures Anwendungsfalls. Modelliert mindestens vier beteiligte Objekte mit Objektnamen, wichtigen Attributen, konkreten Werten und passenden Links. Prüft die fachliche Passung zu Anwendungsfall und Anforderungen. Speichert das Ergebnis unter `docs/03-objektmodell/`.

## 5. Zustandsdiagramm erstellen

Wählt einen fachlichen Objekttyp aus eurem Objektdiagramm. Modelliert mindestens vier sinnvolle Zustände mit durch Ereignisse beschrifteten Übergängen. Ergänzt einen Initialzustand, gegebenenfalls einen Endzustand und mindestens einen alternativen Ablauf. Speichert das Diagramm ebenfalls unter `docs/03-objektmodell/`.

Erklärt euch gegenseitig anhand eurer Quellen, welche Anforderung und welche Stelle des Anwendungsfalls in euren beiden Modellen sichtbar werden. Beide Diagramme einschließlich ihrer Prüfung entstehen **ohne KI-Unterstützung**. Anforderungen und Modellierungsentscheidungen außerhalb der beiden ausdrücklich freigegebenen Skill-Aufgaben bleiben Eigenleistung.

## Werkzeuge und Arbeitsstand

**Word und Miro bleiben erlaubt.** Für die KI-Analyse müssen die ausgewählten Texte zusätzlich als lesbarer Text vorliegen, bevorzugt als Markdown. Screenshots oder reine Bild-PDFs ersetzen diesen Text nicht. Diagramme könnt ihr als PDF oder Bild im Modellordner ablegen.

Ihr pflegt `docs/`; der Kurs pflegt Regeln, Skills und Übungshinweise. **Vorerst werden weder Git-Commit noch Push verlangt.**
