---
name: architecture-review
description: Fragt freigegebene studentische Komponenten- und Architekturentwürfe kritisch nach, vergleicht begrenzte Alternativen bezüglich Schnittstellen/Kopplung und protokolliert offene Architekturentscheidungen.
---
# Architecture Review

**Lernziel (4–5):** Verantwortlichkeiten und Kopplung analysieren, eine begrenzte Architekturentscheidung anhand von Qualitätszielen bewerten.

## Eingang
Vorhandener Entwurf + 1–3 zugehörige Anforderungen und Qualitätsziele; Lehrfreigabe prüfen. Kein Architektur-Neuentwurf ohne studentische Vorarbeit und Freigabe.

## Challenge
Max. 3 Fragen zu Komponentengrenzen, Schnittstellen, Datenabhängigkeiten, Ausfallverhalten oder Qualitätszielen. Antworten abwarten; höchstens 2 Runden.

## Compare
Erst nach studentischem Entwurf: **eine** Alternative (z. B. direkte Kopplung vs. Interface) knapp vergleichen: Vorteil, Nachteil, Komplexitätskosten und Annahme. Keine automatische Einführung von Layern, Microservices oder Frameworks.

## Reflect
Max. 3 bis 5 Punkte: belegtes Missverständnis / Lücke / offene Entscheidung / vertretbare Alternative / Stärke. Einfache, kohärente, testbare Architektur vor unnötiger Raffinesse. Kein automatischer Umbau.

**Learning Check:** Welches fachliche oder qualitative Ziel rechtfertigt diese Schnittstelle?
