# SWE1 – Übung 3, WS 2026/27

Sie überprüfen Ihre bisherigen Anforderungen und erstellen erste UML-Modelle. Arbeiten Sie im Zweierteam an Ihrer Fallstudie: **Fundbüro-Anwendung**, **Verleih-Plattform** oder **Repair-Café-Anwendung**. Ziel ist eine kleine, verständliche Lehranwendung; den [Lernrahmen und die KI-Freigaben](kurs/uebung-03.md) finden Sie in den Kurshinweisen.

Lesen Sie [Übungsblatt 3 in Moodle](https://moodle.hm.edu/pluginfile.php/2162747/mod_resource/content/0/U%CC%88bungsblatt3_SWE1_2627.pdf) selbst. Der Link ist ausschließlich für Studierende bestimmt. Geben Sie das Übungsblatt nicht als Datei oder Chat-Kontext an die KI weiter. Für den Agenten gelten die lokalen Freigaben und die Regeln in [AGENTS.md](AGENTS.md); er darf das Übungsblatt nicht abrufen.

## Einstieg in Copilot

Ein Skill ist eine Arbeitsanweisung für den KI-Agenten. Dieser kann Dateien lesen und Werkzeuge nutzen. Sie wählen die Aufgabe und die Quellen bewusst aus und prüfen das Ergebnis.

Verwenden Sie wie im Übungsblatt **Copilot im Terminal Ihrer Entwicklungsumgebung**, beispielsweise VS Code oder IntelliJ:

- Öffnen Sie den Repository-Ordner und anschließend das integrierte Terminal Ihrer IDE.
- Starten Sie die wie in Übung 1 eingerichtete Copilot CLI mit `copilot`. Beginnen Sie eine neue Sitzung und geben Sie den benötigten Skill-Befehl aus den folgenden Beispielen ein.
- Benennen Sie nur die benötigten Dateien und einen kleinen Abschnitt. Ersetzen Sie die Platzhalter durch Ihre eigenen Pfade und Angaben.

Wird ein Skill nicht erkannt, prüfen Sie die Einrichtung mit der Lehrperson.

## 1. Anforderungen erfassen

Klonen Sie diese Vorlage oder öffnen Sie den heruntergeladenen Repository-Ordner in Ihrer IDE. Wählen Sie unter [docs/01-anforderungen/](docs/01-anforderungen/) Ihre Ausgangsvision, löschen Sie die zwei anderen Visionsdateien und benennen Sie die verbleibende Datei in `vision.md` um.

Legen Sie dort Ihre selbst erarbeiteten Personas, Szenarien, User Stories und strukturierten Anwendungsfälle aus Übung 1 sowie die funktionalen und nichtfunktionalen Anforderungen einschließlich Akzeptanzkriterien aus Übung 2 ab.

## 2. Anforderungen analysieren

Notieren Sie zuerst selbst eine vermutete Unklarheit und Ihre bisherige Begründung. Starten Sie dann den [requirements-coach](.agents/skills/requirements-coach/SKILL.md) im **Challenge-Modus**, beispielsweise so:

```text
/requirements-coach
Lesen Sie nur <Pfad zum Anforderungstext> und <benötigte Kontextdatei>.
Prüfen Sie zunächst <ID oder Abschnitt>.
Unsere eigene Unsicherheit: <Frage und bisherige Begründung>.
Beginnen Sie mit einer Runde und warten Sie auf unsere Antworten.
```

Der Coach hinterfragt Verständlichkeit, Eindeutigkeit, Vollständigkeit und Überprüfbarkeit. Benennen Sie dafür die benötigte Persona und das Szenario als Kontext. Er stellt bevorzugt zwei, höchstens drei quellengestützte Fragen pro Runde. Beantworten Sie diese im Team und entscheiden Sie danach, ob Sie zu einem offenen Punkt eine weitere Runde benötigen. Beenden Sie das Review ausdrücklich, sobald Sie die ausgewählten Punkte besprochen haben. Fertige Formulierungen, Musterlösungen und Compare sind nicht freigegeben.

Dokumentieren Sie mindestens drei Erkenntnisse unter [docs/02-review/](docs/02-review/). Unterscheiden Sie tatsächliche Unklarheiten, offene Fragen und mögliche Verbesserungen. Überarbeiten Sie Anforderungen oder Akzeptanzkriterien **nur, wenn dies notwendig ist**. Dokumentieren und begründen Sie Ihre Klarstellungen nachvollziehbar und prüfen Sie deren Passung zu Ihren User Stories und Anwendungsfällen. Prüfen Sie KI-Hinweise an Ihren Quellen und begründen Sie auch abgelehnte Hinweise; KI-Kritik allein ist kein Änderungsgrund. Erklären Sie sich anschließend gegenseitig ohne KI Ihre Entscheidung und die Überprüfbarkeit der Anforderungen.

## 3. Substantive extrahieren

Beginnen Sie eine **neue Copilot-Sitzung**, damit Persona und Review-Dialog nicht als zusätzlicher Kontext vorliegen. Nutzen Sie [noun-extraction](.agents/skills/noun-extraction/SKILL.md) nur mit funktionalen Anforderungen, User Stories oder strukturierten Anwendungsfällen:

```text
/noun-extraction
Lesen Sie nur <Pfad zum Anforderungstext>, Abschnitt <ID oder Abschnitt>.
Extrahieren Sie nur aus diesem Abschnitt die verwendeten Substantive.
```

Der Skill liefert Grundformen, fachliche Mehrwortbegriffe und Fundstellen. Bei Teilausgaben nennt er den bearbeiteten und verbleibenden Umfang. Er liest keine Persona, ordnet keine Modellelemente zu und erzeugt keine UML-Diagramme. Die Spalten für studentische Einordnung und Begründung bleiben in seiner Ausgabe leer.

Prüfen Sie einige Einträge selbst am Originaltext, insbesondere Grundform, Mehrwortbegriffe und Fundstelle. Kopieren Sie die Ausgabe im Copilot-Terminal mit `/copy` und übernehmen Sie sie als Textdokument nach [docs/03-objektmodell/](docs/03-objektmodell/). Entscheiden Sie selbst, welche Begriffe ein eigenes Objekt benötigen und welche Eigenschaften anderer Objekte beschreiben.

## 4. Objektdiagramm erstellen

Wählen Sie einen konkreten Zeitpunkt innerhalb Ihres Anwendungsfalls. Modellieren Sie mindestens vier beteiligte Objekte mit Objektnamen, wichtigen Attributen, konkreten Werten und passenden Links. Ergänzen Sie bei Bedarf Rollenbezeichnungen. Prüfen Sie die fachliche Passung zu Anwendungsfall und Anforderungen. Speichern Sie das Ergebnis unter `docs/03-objektmodell/`.

## 5. Zustandsdiagramm erstellen

Wählen Sie einen fachlichen Objekttyp aus Ihrem Objektdiagramm, dessen Zustand sich im Anwendungsfall verändert. Modellieren Sie mindestens vier sinnvolle Zustände mit durch Ereignisse beschrifteten Übergängen. Ergänzen Sie einen Initialzustand, gegebenenfalls einen Endzustand und mindestens einen alternativen Ablauf. Unterscheiden Sie Zustände von den Ereignissen, die einen Zustandswechsel auslösen. Speichern Sie das Diagramm ebenfalls unter `docs/03-objektmodell/`.

Erklären Sie sich gegenseitig anhand Ihrer Quellen, welche Anforderung und welche Stelle des Anwendungsfalls in Ihren beiden Modellen sichtbar werden. Beide Diagramme einschließlich ihrer Prüfung entstehen **ohne KI-Unterstützung**. Anforderungen und Modellierungsentscheidungen außerhalb der beiden ausdrücklich freigegebenen Skill-Aufgaben bleiben Eigenleistung.

## Werkzeuge und Arbeitsstand

**Word und Miro bleiben erlaubt.** Für die KI-Analyse müssen die ausgewählten Texte als lesbarer Text vorliegen, bevorzugt als Markdown. Screenshots oder reine Bild-PDFs ersetzen diesen Text nicht. Diagramme können Sie als PDF oder Bild im Modellordner ablegen.

Sie pflegen `docs/`; der Kurs pflegt Regeln, Skills und Übungshinweise. **Vorerst werden weder Git-Commit noch Push verlangt.**
