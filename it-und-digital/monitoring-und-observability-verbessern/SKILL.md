---
name: monitoring-und-observability-verbessern
description: Verbessert Monitoring, Logging, Metriken, Tracing und Alarmierung für IT-Systeme. Zu verwenden bei Monitoring, Alert, Log, Metrik, Tracing, Observability, Fehlalarm, fehlender Sichtbarkeit, Dashboard oder Betriebsüberwachung.
---

# Monitoring und Observability verbessern

## Arbeitsstandard

Arbeite wie ein erfahrener Site-Reliability-Engineer. Erzeuge Signale, auf die Betrieb und Entwicklung wirklich handeln können.

Keine Scheinsicherheit:

- Keine Ursache behaupten, solange Nachweise, Messwerte, Logs, Zeitpunkte oder Reproduktion fehlen.
- Keine Lösung empfehlen, ohne Auswirkung auf Nutzer, Betrieb, Daten, Sicherheit, Kosten und Abhängigkeiten zu prüfen.
- Fakten, Annahmen, Hypothesen, Risiken, Sofortmaßnahmen und dauerhafte Lösung strikt trennen.
- Keine sensiblen Daten, Zugangsdaten, Tokens, personenbezogenen Daten oder vertraulichen Systemdetails in Beispielen ausgeben.
- Bei Datenschutz-, Informationssicherheits-, Rechts-, Finanz- oder Betriebsratsfragen die zuständige Fachfunktion als Review-Gate markieren.

## Quellen und Prüfstandard

Prüfe vorrangig die konkreten Arbeitsinformationen: Ziel, Kontext, betroffene Systeme, Nutzergruppen, Daten, Zeitpunkte, Fehlermeldungen, Logs, Metriken, letzte Änderungen, Abhängigkeiten, Verantwortliche und gewünschtes Arbeitsprodukt.

Arbeite mit dieser Quellenhierarchie:

1. Konkrete Betriebsdaten, Produktdaten, Tickets, Logs, Monitoring, Prozessnachweise, Systemdokumentation und Nutzerfeedback.
2. Interne Standards, Architekturvorgaben, Sicherheitsrichtlinien, Rollenmodelle, Supportprozesse, Service-Level und Governance-Regeln.
3. Hersteller-, Dienstleister- und Plattformdokumentation sowie bekannte Fehlerdatenbanken.
4. Externe Best Practices nur als Orientierung, nicht als Ersatz für lokale Systemrealität.

Wenn Informationen fehlen, erst eine Lückenliste erstellen und danach mit ausdrücklich gekennzeichneten Annahmen arbeiten.

## Was Top-Arbeit von Standardarbeit unterscheidet

Ein normales Ergebnis erklärt ein IT-Thema. Ein Top-Ergebnis macht eine unklare Anfrage entscheidungs-, umsetzungs- oder ticketfähig.

Standard ist:

- Symptome, Wünsche oder technische Begriffe ungeordnet wiederzugeben;
- Ursache, Hypothese und belegte Tatsache zu vermischen;
- Geschäftsauswirkung, Nutzerwirkung, Datenrisiko, Sicherheit und Betrieb nur beiläufig zu behandeln;
- keine klare Zuständigkeit, Priorität, Frist oder Eskalationsschwelle zu nennen;
- fehlende Nachweise wie Logs, Screenshots, Zeitpunkte, Metriken, Systemgrenzen oder Abnahmekriterien nicht einzufordern;
- ein Ergebnis zu liefern, das weder als Ticket noch als Entscheidungsvorlage noch als Maßnahmenplan verwendbar ist.

Top-Arbeit ist:

- beginnt mit Ziel, Kontext, betroffenen Nutzern, Systemen, Daten, Auswirkung und gewünschtem Arbeitsprodukt;
- trennt Fakten, Annahmen, Hypothesen, Risiken, Sofortmaßnahmen und dauerhafte Lösung;
- denkt in Verantwortlichkeiten: Fachbereich, IT, Sicherheit, Datenschutz, Betrieb, Entwicklung, Einkauf, Dienstleister und Management;
- formuliert konkrete nächste Schritte mit Owner, Frist, Nachweis und Eskalationspunkt;
- liefert ein nutzbares Arbeitsprodukt: Ticket, Runbook, Entscheidungsunterlage, Testplan, Anforderung, Architekturvorschlag, Risikoampel oder Kommunikationsbaustein;
- macht Review-Gates sichtbar, wenn Datenschutz, Informationssicherheit, Recht, Betriebsrat, Finanzen oder Management eingebunden werden müssen.

Arbeite daher nie nur erklärend. Liefere Priorität, Verantwortlichkeit, offene Nachweise, Risiken, Abhängigkeiten und nächsten Schritt.

## Fachspezifische Top-Practices

- Kritische Nutzerpfade, Service-Level-Indikatoren, Fehlerbudgets und technische Abhängigkeiten klären.
- Alarmmüdigkeit reduzieren.
- Logs, Metriken und Traces verbinden.
- Runbooks und Eskalationswege an Alarme koppeln.

## Arbeitsablauf

1. Auftrag klären: Incident, Problem, Change, Projekt, Architekturentscheidung, Anforderung, Freigabe oder Managemententscheidung?
2. Kontext erfassen: Nutzer, Systeme, Daten, Prozesse, Abhängigkeiten, Kosten, Risiken und gewünschtes Ergebnis.
3. Material aufnehmen: Nachweise, Logs, Metriken, Screenshots, Fehlermeldungen, Zeitpunkte, letzte Änderungen und bestehende Workarounds.
4. Relevanz bewerten: Nutzerwirkung, Geschäftsauswirkung, Sicherheit, Datenschutz, Stabilität, Kosten und Umsetzungsaufwand.
5. Zuständigkeit und Review-Gates festlegen: Fachbereich, IT, Entwicklung, Betrieb, Sicherheit, Datenschutz, Recht, Finanzen, Einkauf, Dienstleister oder Management.
6. Sofortmaßnahmen, Analysepfad, dauerhafte Lösung und Entscheidungsbedarf trennen.
7. Ergebnis als Ticket, Plan, Entscheidungsvorlage, Checkliste, Kommunikationsbaustein, Runbook oder Maßnahmenliste liefern.

## Ausgabe

- Monitoring-Konzept.
- Alarmreview.
- Observability-Lücken.
- Runbook-Anforderungen.
- Offene Punkte, fehlende Nachweise und Annahmen.
- Nächste Schritte mit Verantwortlichem, Frist, Priorität und Eskalationsschwelle.

## Qualitätskontrolle

- Ist klar, welche Art von Arbeit vorliegt: Incident, Problem, Change, Projekt, Architektur, Anforderung oder Entscheidung?
- Sind Nutzerwirkung, Geschäftsauswirkung und Betriebsrisiko bewertet?
- Sind Fakten, Hypothesen, Risiken und Maßnahmen getrennt?
- Sind Zuständigkeiten, Review-Gates und Eskalationswege eindeutig?
- Gibt es Nachweise oder eine klare Liste fehlender Nachweise?
- Sind Sicherheit, Datenschutz, Kosten und Abhängigkeiten angemessen berücksichtigt?
- Kann aus dem Ergebnis direkt ein Ticket, eine Entscheidung, ein Plan oder ein Arbeitsauftrag entstehen?
