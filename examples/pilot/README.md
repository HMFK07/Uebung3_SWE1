# Pilotfall „Campus-Schließfach“ (künstliches Übungsmaterial)

**Nur zum Testen der Skills, ausdrücklich keine studentische Musterlösung.** Der Fall ist frei erfunden und wurde absichtlich inkonsistent gestaltet. Er gehört **nicht** zur eigentlichen Fallstudie des Teams.

## Reihenfolge für den Pilot

1. Lehrperson erklärt die **Testfreigabe nur für `examples/pilot/`**, nicht für aktuelle Kursabgaben.
2. `requirements-coach` im Challenge-Modus: **nur** `persona-ziele-szenario.md` lesen. Erwartet: Fragen und Dialog, **keine** Stories vorab.
3. Nach eigener Antwort und freigegebenem Compare-Modus: zusätzlich `studentischer-entwurf.md` lesen. Erwartet: kleiner KI-Vorschlag, Vergleich, kategorisierter Lernbericht.
4. `uml-review` auf `modell.puml`: Erwarte Rückfragen zu Systemgrenze/Multiplizität, keine automatische Änderung.
5. `debug-coach` / `test-coach`: optionales, absichtlich fehlerhaftes Java-Mini-Beispiel nutzen.

## Java-Pilot ohne zusätzliche Bibliotheken (optional JDK)

Im Ordner `examples/pilot/`:

```bash
javac SchliessfachService.java SchliessfachServiceTest.java
java SchliessfachServiceTest
```

**Erwartetes Ergebnis des Ausgangsmaterials: Test schlägt fehl** (Doppelreservierung wird fälschlich akzeptiert). Das ist ein bewusster Test-Fixpunkt und kein Beleg, dass der Agent etwas falsch gemacht hat. Den Fehler nicht heimlich löschen – Diagnose und Erklärung sind das Lernziel. Das Projekt selbst setzt **Java nicht verpflichtend** voraus.

## Kurzprompts

```text
Dies ist ein durch die Lehrperson freigegebener Pilot, keine Abgabe.
Nutze requirements-coach im Challenge-Modus. Lies ausschließlich
examples/pilot/persona-ziele-szenario.md.
Stelle maximal drei Fragen und warte auf meine Antworten.
```

```text
Compare ist für diesen Pilot freigegeben. Lies jetzt zusätzlich
examples/pilot/studentischer-entwurf.md. Gib eine kleine alternative
Skizze und maximal fünf belegte Lernpunkte. Ändere keine Dateien.
```

```text
Nutze debug-coach für SchliessfachService.java und den fehlgeschlagenen
Test. Ich weiß bisher nur, dass Doppelreservierung akzeptiert wird.
Bitte erst Hypothesen und Gegenproben, noch keine Codeänderung.
```

Die zu erwartenden Verhaltensmerkmale und Bewertungskriterien finden Lehrende unter `docs/lehrende/PILOT-SZENARIEN.md`.
