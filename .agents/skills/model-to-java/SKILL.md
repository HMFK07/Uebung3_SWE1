---
name: model-to-java
description: Implementiert in Übung 4 nach eigenem Modellierungs-Commit zwei bis drei ausdrücklich ausgewählte fachliche Klassen plus Main.java aus einem studentischen UML-PNG in Java; keine UML-Modellierung.
---
# Vom eigenen UML-PNG zu Java

Es gelten [AGENTS.md](../../../AGENTS.md) und die [Freigabe für Übung 4](../../../kurs/uebung-04.md). Antworte kurz auf Deutsch. Die Freigaben aus Übung 3 werden nicht erweitert.

## Eingabe und Freigabe prüfen

- Ermittle die Projektwurzel einmal. Eingabe ist das selbst erstellte Bild `docs/04-klassendiagramm/klassendiagramm.png`, im Copilot-Auftrag als `@docs/04-klassendiagramm/klassendiagramm.png` angehängt. Öffne es mit der verfügbaren Bildfunktion. Wenn keine Bildverarbeitung verfügbar ist oder das Bild nicht zugänglich ist: benenne das Hindernis und halte an; keine Inhalte aus Dateinamen oder Anforderungen erschließen.
- Prüfe ausschließlich lesend mit Git, dass das PNG in einem eigenen, vom Team benannten Modellierungs-Commit auf dem aktuellen Übungsbranch enthalten ist, dieser Commit zu `HEAD` gehört und die aktuelle PNG-Fassung seit diesem Commit unverändert ist. Nutze etwa `git log --oneline -- docs/04-klassendiagramm/klassendiagramm.png`, `git merge-base --is-ancestor <Commit-ID> HEAD` und den Vergleich der Blob-IDs von `git rev-parse <Commit-ID>:docs/04-klassendiagramm/klassendiagramm.png` und `git hash-object docs/04-klassendiagramm/klassendiagramm.png`. Prüfe auch vorgemerkte Änderungen. Eine bloße uncommittete PNG-Datei genügt nicht. Bei fehlendem oder unklarem Nachweis bitte das Team um den eigenen Commit und warte; erst danach Code schreiben. Eine Commit-ID belegt keine eigenständige Urheberschaft: diese erklärt das Team selbst.
- Das Team benennt ausdrücklich zwei bis drei zusammenhängende fachliche Klassen und den Auftrag zur Umsetzung in `src/` plus `Main.java`. Fehlt die Auswahl, frage danach, ohne Klassen vorzuschlagen. Lies keine Anforderungen, Personas oder weiteren Modelle zur Ergänzung. Prüfe vorhandene Zieldateien vor Änderungen und erhalte studentischen Code außerhalb des Auftrags.

## Bild lesen, Unsicherheiten klären

Lies für den gewählten Ausschnitt Klassennamen, Attribute mit Typen und Sichtbarkeiten, Methoden mit Parametern und Rückgabetypen sowie Assoziationsnamen und Multiplizitäten an beiden Enden. Nenne den gelesenen Umfang knapp. Das ist eine technische Übertragung, kein fachliches UML-Review.

Bei unlesbaren, fehlenden oder mehrdeutigen Angaben benenne die betroffene Klasse oder Bildstelle und stelle höchstens drei gezielte Fragen pro Runde. Das gilt auch für nicht erkennbare Navigierbarkeit, nicht festgelegtes Methodenverhalten oder eine Beziehung zu einer nicht ausgewählten Klasse, die den Ausschnitt unklar macht. Warte vor der betroffenen Implementierung auf die studentische Entscheidung; rate keine Bezeichnungen, Multiplizitäten oder Fachregeln. Biete keine fachlichen Modellalternativen an. Das Team passt sein Diagramm bei Bedarf selbst ohne KI an und committet die neue PNG-Fassung vor Fortsetzung. Keine stillschweigende Modelländerung und keine zusätzlichen Klassen zur Umgehung einer Grenze.

## Eng begrenzt implementieren

- Schreibe genau die ausgewählten zwei bis drei fachlichen Klassen und `src/Main.java`, vorzugsweise als einfache Java-Dateien ohne Packages. Nur Java-Standardbibliothek und grundlegende Java-Konzepte. Keine Vererbung, Interfaces, abstrakten Klassen, Design Patterns, Datenbanken, Frameworks oder zusätzlichen Anforderungen.
- Übertrage nur modellierte Elemente und die vom Team geklärten Angaben. Einfache Konstruktoren zur Initialisierung und die Startmethode sind technische Hilfen; erfinde keine fachlichen Operationen. Erkläre nötige technische Abbildungen knapp, beispielsweise Objektreferenz oder Standardbibliotheks-Liste für eine Assoziation. Bibliothekstypen wie `String` und `ArrayList` sind keine zusätzlichen fachlichen Klassen; implementiere keine eigenen Interfaces.
- Bilde die geklärten Multiplizitäten nachvollziehbar ab. Eine Liste allein erzwingt keine Untergrenze oder Gegenrichtung; benenne solche Grenzen und setze die geklärten Regeln im erlaubten Ausschnitt um, ohne weitere Fachregeln zu erfinden. Ist ein korrektes Verhalten im freigegebenen Umfang nicht möglich, benenne den Blocker und warte auf die Entscheidung des Teams.
- `Main.java` hat `public static void main(String[] args)`, erzeugt mindestens zwei Objekte, stellt mindestens eine modellierte Beziehung her, ruft mindestens zwei Methoden auf und zeigt Ergebnisse mit `System.out.println(...)`. Nutze einfache Beispieldaten; frage nach, falls dafür fachliches Verhalten fehlt.

## Technisch prüfen und übergeben

Kompiliere und starte den Ausschnitt mit dem vorhandenen JDK, beispielsweise `javac -encoding UTF-8 src/*.java` und `java -cp src Main`. Prüfe einen normalen Ablauf und, soweit sinnvoll, einen geklärten Rand- oder Fehlerfall. Keine Abhängigkeiten installieren. Fehlt das JDK oder scheitert ein Werkzeug, berichte dies und behaupte keinen erfolgreichen Test.

Nenne geänderte Dateien, tatsächlich ausgeführte Befehle und Ergebnisse sowie verbleibende Unsicherheiten kurz. Fordere zum eigenen Vergleich von PNG und Code und zur gegenseitigen Erklärung ohne KI auf. Ändere weder PNG noch Anforderungen oder andere Modelle. Führe keinen Commit, Push oder Merge aus; Modell- und Code-Commit erstellt das Team selbst getrennt.
