# Übung 4 – Klassendiagramm und Java, WS 2026/27

Grundlage ist das aktuelle [Übungsblatt 4](Übungsblatt4_SWE1_2627.pdf), Aufgaben 1–5. Für die Git-Schritte gelten das [Git-Zusatzblatt](Git_Anlage_Übungsblatt4_SWE1_2627.pdf) und die ergänzte [Anleitung zur Git-Teamarbeit](git-teamarbeit.md). Die Freigaben aus [Übung 3](uebung-03.md) bleiben unverändert. Die Aufgaben gelten für Fundbüro, Verleih-Plattform und Repair-Café.

## 1. Teamstand vorbereiten

Sichern Sie zuerst die bisherigen Ergebnisse im eigenen Team-Repository. Übernehmen Sie vor jeder Übung die aktuelle Lehrvorlage in `main` und erstellen Sie danach gemeinsam einen Übungsbranch, beispielsweise `uebung-04-team`. Die genauen Befehle und Stopps bei Problemen stehen in der Git-Anleitung.

## 2. Klassendiagramm eigenständig erstellen

**Die fachliche UML-Modellierung, ihre Prüfung und alle Modellierungsentscheidungen erfolgen ohne KI-Unterstützung.** Auch der Java-Skill darf kein Modell vorschlagen, vervollständigen oder fachlich bewerten.

Leiten Sie aus Ihrem Objektdiagramm aus Übung 3 zunächst einen zentralen Ausschnitt Ihres Anwendungsfalls mit **drei bis vier fachlich wichtigen Klassen** ab:

1. Beginnen Sie nur mit Klassennamen und einfachen binären Assoziationen. Übernehmen beziehungsweise überarbeiten Sie die Beziehungsnamen selbst. Keine Vererbung, Aggregation oder Komposition.
2. Tragen Sie an beiden Assoziationsenden Multiplizitäten ein und begründen Sie diese für eine ausgewählte Assoziation anhand Ihres Anwendungsfalls.
3. Erstellen Sie eine Kopie der ersten Fassung. Ergänzen Sie wichtige Attribute mit Datentypen und Sichtbarkeiten sowie fachlich sinnvolle Methoden mit Sichtbarkeit, Rückgabetyp (`void`, wenn kein Rückgabewert) und gegebenenfalls Parametern. Prüfen Sie die Verantwortlichkeiten selbst.

Nutzen Sie nur bisher behandelte Grundlagen der objektorientierten Programmierung. Vererbung, Interfaces, abstrakte Klassen und Design Patterns sind ausgeschlossen.

## 3. Lesbares PNG sichern – vor Copilot

Exportieren Sie das detaillierte Diagramm aus Ihrem Modellierungswerkzeug nach:

`docs/04-klassendiagramm/klassendiagramm.png`

Prüfen Sie selbst, dass sich das PNG öffnen lässt und Klassennamen, Attribute, Methoden, Beziehungsnamen und Multiplizitäten vollständig lesbar sind. Schneiden Sie Werkzeugleisten und große leere Ränder ab; vermeiden Sie unnötig große Bilder. Bewahren Sie auch die erste Fassung und Ihre Begründung im Modellordner auf.

Erstellen Sie **selbst einen Modellierungs-Commit auf dem Übungsbranch**, bevor Sie Copilot einsetzen. Beispiel im normalen IDE-Terminal:

```bash
git status
git add docs/04-klassendiagramm/
git diff --cached
git commit -m "Eigenes Klassendiagramm fuer Uebung 4"
git push origin uebung-04-team
```

Prüfen Sie vor dem Commit die vorgemerkten Dateien. Modell und spätere Implementierung müssen in getrennten Commits nachvollziehbar bleiben.

## 4. Ausgewählten Ausschnitt mit Copilot implementieren

Erst nach dem Modellierungs-Commit ist KI für die Java-Implementierung freigegeben. Starten Sie im Projektordner eine **neue Copilot-CLI-Sitzung** mit `copilot`. Wählen Sie selbst **zwei bis drei zusammenhängende fachliche Klassen** aus Ihrem PNG aus; dazu kommt `Main.java`. Der Ausschnitt darf kleiner als Ihr vollständiges Diagramm sein.

Beispielauftrag; ersetzen Sie die Klassennamen und nennen Sie Ihren Modellierungs-Commit:

```text
/model-to-java
Lies @docs/04-klassendiagramm/klassendiagramm.png als Bild.
Mein eigener Modellierungs-Commit ist <Commit-ID>.
Implementiere <KlasseA>, <KlasseB> und Main.java in src/.
Nur modellierte Elemente, einfache Assoziationen und Java-Grundlagen.
Verwende nur die Java-Standardbibliothek, keine Vererbung oder Frameworks.
```

Kontrollieren Sie in Copilot, ob die Datei als **Bildanlage** erkannt wird. Ein Dateipfad allein garantiert keine Bildverarbeitung. Falls das PNG nicht zugänglich ist, holen Sie technische Hilfe; lassen Sie keine Ersatzmodellierung aus Anforderungen erzeugen.

Der [Skill model-to-java](../.agents/skills/model-to-java/SKILL.md) darf nur den ausgewählten Ausschnitt umsetzen. Keine zusätzlichen fachlichen Klassen oder Anforderungen, keine Interfaces, abstrakten Klassen, Design Patterns, Datenbanken oder Frameworks. Eine grafische Oberfläche und eine vollständige Fallstudienimplementierung sind nicht erforderlich. Bei unlesbaren oder mehrdeutigen Angaben benennt der Skill die Unsicherheit und wartet auf Ihre Entscheidung. Änderungen am Diagramm nehmen ausschließlich Sie selbst ohne KI-Modellierung vor; sichern Sie eine geänderte Modellfassung erneut vor der Fortsetzung.

## 5. Starten, prüfen und erklären

`src/Main.java` enthält `public static void main(String[] args)`. Erzeugen Sie mindestens zwei Objekte, stellen Sie mindestens eine modellierte Beziehung her, rufen Sie mindestens zwei Methoden auf und geben Sie nachvollziehbare Ergebnisse mit `System.out.println(...)` aus.

Starten Sie das Programm in Ihrer IDE oder mit einem installierten JDK im normalen Terminal (für einfache Dateien ohne Package-Deklaration):

```bash
java -version
javac -version
javac -encoding UTF-8 src/*.java
java -cp src Main
```

Die entstehenden `.class`-Dateien werden bereits durch `.gitignore` ausgeschlossen. Es werden keine Build-Werkzeuge oder zusätzlichen Bibliotheken benötigt.

Vergleichen Sie selbst Klassen, Attribute, Methoden, Beziehungen und besonders gelesene Bezeichnungen und Multiplizitäten mit dem PNG. Prüfen Sie einen normalen Ablauf und, soweit sinnvoll, einen Rand- oder Fehlerfall. Erklären Sie sich gegenseitig **ohne KI**, wie die Objekte verbunden sind, was die Methoden bewirken und ob der Code dem Diagramm entspricht.

Sichern Sie den geprüften Java-Code in einem **weiteren Commit**, pushen Sie ausschließlich zum Team-Repository und erstellen Sie einen Pull Request nach `main`. Das andere Teammitglied prüft ihn vor dem Merge. Wählen Sie eine Merge-Art, die Modell- und Code-Commit getrennt erhält; kein Squash. Aktualisieren Sie anschließend beide lokalen `main`-Branches gemäß Git-Anleitung. Im zusammengeführten Stand müssen das PNG und die Java-Klassen einschließlich `src/Main.java` vorliegen. Copilot führt keinen Commit, Push oder Merge automatisch aus.
