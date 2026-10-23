---
name: model-code-review
description: Hinterfragt und vergleicht ein eigenständig entwickeltes, zur KI-Prüfung freigegebenes UML-Klassenmodell mit Quellcode; unterscheidet Abstraktionsunterschiede von Widersprüchen.
---
# Model–Code Review

**Lernziel (4–5):** Modell-/Codeabweichungen analysieren und begründen, ob Modell, Implementierung oder Dokumentation zu ändern ist.

## Eingang
Vorhandenes Modell, verknüpfte Anforderungen, zugehöriger Code und **Freigabe zum KI-Review der UML**. Ohne Freigabe keine Analyse der studentischen UML-Abgabe.

## Challenge
Max. 3 Fragen zu Klassen, Attributen, Operationen, Beziehungen und Modellabstraktion; Team erklärt vorliegende Unterschiede, bevor der Agent urteilt.

## Compare
Nur relevanten Ausschnitt gegenüberstellen: `Modell | Code | belegte Abweichung / legitime Freiheit | Auswirkung`. Max. 3 Einträge; Fehlerhypothese ist kein nachgewiesener Widerspruch.

## Reflect
Kurz Missverständnisse, offene Fragen und begründete Alternativen notieren. **Nie** Modell und Code automatisch synchronisieren oder Requirements zur Fehlerverdeckung ändern.

**Learning Check:** Welche Abweichung verletzt eine Anforderung und welche ist eine zulässige Implementierungsentscheidung?
