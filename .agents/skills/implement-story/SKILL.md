---
name: implement-story
description: Plant und implementiert nur explizit beauftragte kleine Stories nach genehmigter Spezifikation, fordert Erklärungen und Tests ein und bevorzugt einfachen, gut verständlichen Code.
---
# Implement Story

**Lernziel (3–4):** Studierende ordnen Code einer Story/einem Akzeptanzkriterium zu und erklären Kontrollfluss, Verantwortlichkeiten und Tests.

## Eingang
Erforderlich: expliziter Codeauftrag, genehmigte Story/Issue, Akzeptanzkriterien, betroffene Dateien, KI-Freigabe. Falls Stack/Testbefehl fehlen: nichts erfinden.

## Coach / Challenge
Vor Änderung höchstens 2 Verständnisfragen zu geplantem Verhalten/Design, sofern nicht bereits geklärt. Vorschlag eines **maximal dreischrittigen Minimalplans**; bei wesentlichen Spezifikationslücken nicht implementieren.

## Implement / Compare
1. Nur beauftragten Umfang umsetzen; vorhandene Struktur bewahren.
2. Sprechende Namen, geradlinige Abläufe, fachlich kohärente und beobachtbar testbare Module; keine unnötigen Schichten, Muster, Abhängigkeiten, Mikroklassen oder Optimierungen.
3. Gegen Story und Akzeptanzkriterien prüfen; bei Alternativen kurz begründen, warum die einfachere genügt. Keine künstliche zweite Komplettimplementierung.
4. Tatsächliche Tests ausführen, wenn möglich; Ergebnisse und Grenzen wahrheitsgemäß berichten.

## Reflect
`Story/AC → Änderung (Datei) → Teststatus → offene Frage`. Kurze Rückfrage: *Welche Methode erfüllt welches Kriterium und wie prüfst du das?* Kein Commit/Push ohne Auftrag; Spezifikation nicht nachträglich passend machen.
