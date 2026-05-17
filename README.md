# Skills für Deutschland

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

Deutsch-first Skills für KI-Assistenten, die deutsche Arbeit in deutschen Rechts-, Wirtschafts- und Verwaltungskontexten besser erledigen sollen.

Viele öffentliche Skill-Sammlungen sind englisch, amerikanisch geprägt oder zu allgemein für deutsche Nutzer. Dieses Repository sammelt Fähigkeiten, die deutsche Quellen, deutsche Begriffe, deutsche Risiken und deutsche Arbeitsprodukte ernst nehmen.

Der erste Schwerpunkt ist Recht: Skills sollen Entwürfe, Prüfvermerke, Lückenlisten, Risikoanalysen, Vertragsvergleiche, Verhandlungsunterlagen und Entscheidungsvorlagen so vorbereiten, dass erfahrene Juristen schneller zu belastbaren Ergebnissen kommen.

Der zweite gestartete Geschäftsbereich ist `it-und-digital/` für operative Informationstechnologie und digitale Prozesse in großen Einzelhandelsunternehmen mit vielen Filialen.

Außerhalb von `recht/` gibt es Meta-Skills für die Skill-Erstellung selbst, etwa `skill-erstellung/skill-generation-best-practices`.

## Status

Das Repository ist öffentlich und steht unter der MIT-Lizenz. Beiträge sind willkommen, wenn sie den Qualitätsstandard des Projekts ernst nehmen.

Wichtig: Die Skills ersetzen keine anwaltliche Prüfung. Sie sollen KI-Assistenten zu besseren Entwürfen, Prüfstrukturen und Arbeitsprodukten führen, die von qualifizierten Personen geprüft werden müssen.

## Ziel

Ein Skill soll nicht nur erklären, was ungefähr gilt. Er soll der KI die Arbeitsweise vorgeben, die ein sehr guter deutscher Anwalt erwarten würde:

- Sachverhalt zuerst, Textbaustein zuletzt.
- Deutsche und europäische Quellen vor amerikanischen Mustern.
- Fakten, Annahmen, offene Punkte und Bewertung strikt getrennt.
- Fristen, Form, Zuständigkeit, Beweise, Anlagen und Eskalation ausdrücklich geprüft.
- Ergebnis als verwertbares Arbeitsprodukt, nicht als allgemeiner Ratgebertext.
- Keine Scheinsicherheit, keine erfundenen Fundstellen, keine generische KI-Prosa.

## Wie Skills geschrieben werden

Jeder Skill ist ein einzelner Ordner mit genau einer `SKILL.md`. Quellen, Prüfstandard und Arbeitsweise stehen direkt in dieser Datei. Es gibt keine zusätzlichen Quellenordner innerhalb eines Skills.

Frontmatter bleibt knapp:

```yaml
---
name: beschreibender-skill-name
description: Klare Trigger und Einsatzfälle, damit die KI den Skill zuverlässig lädt.
---
```

Der Body folgt grundsätzlich diesem Muster:

- `Arbeitsstandard`: Rolle, Qualitätsniveau, Grenzen und Anti-Slop-Regeln.
- `Quellen und Prüfstandard`: Quellenhierarchie und Aktualitätsvorbehalte.
- `Was Top-Arbeit von Standardarbeit unterscheidet`: konkrete Qualitätsdifferenz.
- `Fachspezifische Top-Practices`: was ein sehr guter Anwalt in genau diesem Thema anders macht.
- `Arbeitsablauf`: zwingende Prüfreihenfolge.
- `Ausgabe`: welche verwertbaren Produkte entstehen sollen.
- `Qualitätskontrolle`: kurze Review-Fragen gegen Scheinsicherheit und Lücken.

Gute Skill-Namen sind deutsch, beschreibend, kleingeschrieben und mit Bindestrichen verbunden. Ordner werden nach primärem Rechtsgebiet sortiert, nicht nach Branche, Persona oder Prompt-Anlass.

## Bereits abgedeckte Bereiche

Das Repository enthält aktuell 136 Rechts-Skills in deutschen Rechtsgebieten und anwaltlichen Arbeitsmethoden.

Stark ausgebaute Bereiche:

- `mietrecht`: Wohnraummiete, Mieterhöhung, Nebenkosten, Mängel, Kündigung, Kaution, Räumungsschutz und weitere Praxisprobleme.
- `vertragsrecht`: Vertragsprüfung, Vertragsvergleich, Redline-/Delta-Analyse, Vertragsverhandlung, Klauseln, Software, Einkauf, Online-Shop und Lieferanten.
- `technologierecht`: künstliche Intelligenz, Hochrisiko-Systeme, Grundrechtebewertung, Cyberresilienz, Datenzugang, Plattformpflichten und Produktfreigabe.
- `regelkonformitaet`: Behördenkommunikation, interne Untersuchungen, Richtlinienprüfung, Hinweisgeber, Lieferketten, Geldwäsche, Produktsicherheit und Digitalregulierung.
- `datenschutz`: Datenschutz-Folgenabschätzung, algorithmische Systeme, Auftragsverarbeitung, Betroffenenrechte, Datenpannen, Kundenprogramme und Videoüberwachung.
- `prozessrecht`: Schriftsätze, Klageerwiderung, Beweise, Anlagen, Fristen, Vergleich, Prozessrisiko und Forderungsdurchsetzung.

Weitere vorhandene Bereiche:

- Arbeitsrecht, Gesellschaftsrecht, Urheberrecht, Wettbewerbsrecht, Presserecht, Strafrecht, Baurecht, Vergaberecht, Insolvenzrecht, Kennzeichenrecht, Erbrecht, Familienrecht, Immobilienrecht, Medizinrecht, Sozialrecht, Steuerrecht, Vereinsrecht, Energierecht, Bildungsrecht, Zahlungsrecht und Geheimnisschutz.

Querschnittlich gibt es außerdem `anwaltliche-arbeitsmethoden` für Mandatsaufnahme, Mandantenmemos, Mandanten-E-Mails, Praxismemos und Risikoampeln.

Außerhalb des Rechtsbereichs ist `it-und-digital` gestartet: Kassensysteme, Filialnetzwerk, Systemausfälle, Rollouts, Warenwirtschaft, Dienstleistersteuerung, Anforderungen, Softwareauswahl, Datenflüsse, Produktdaten, Onlinehandel, Abholung in der Filiale, Filial-Apps, Zugriffsrechte, Releases, Tests, Migrationen, Dashboards, Automatisierung, künstliche Intelligenz, IT-Kosten, Informationssicherheitsvorfälle und Filialhardware.

## Was noch möglich wäre

Naheliegende nächste Ausbaustufen:

- Mehr Litigation-Skills: Berufung, einstweiliger Rechtsschutz, Beweisbeschluss, Vergleichsverhandlung vor Gericht, Kostenfestsetzung.
- Mehr Transaktionsarbeit: Kaufvertrag, Gesellschaftervereinbarung, Garantiekatalog, Closing, Post-Closing-Streit.
- Mehr Unternehmensrecht: Geschäftsführerpflichten, Gesellschafterstreit, Kapitalmaßnahmen, Unternehmensnachfolge.
- Mehr regulierte Branchen: Fintech, Gesundheit, Energie, Telekommunikation, Versicherungen, öffentliche Verwaltung.
- Mehr Kanzlei-Workflows: Aktenchronologie, Dokumentenreview, Anlagenmapping, Mandatsrisiko, Honorar- und Scope-Klärung.
- Mehr Inhouse-Workflows: Legal Intake, Vertragsfreigabeprozess, Policy Rollout, Audit-Vorbereitung, Rechtsänderungsmonitoring.
- Mehr Verbraucher- und Bürgerprobleme: Reisen, Versicherung, Bank, Telekommunikation, Kaufrecht, Handwerker, Behördenbescheide.
- Mehr Geschäftsbereiche außerhalb von Recht: Personal, Filialbetrieb, Einkauf, Supply Chain, Logistik, Immobilien und Expansion, Finanzen und Controlling, Marketing und Kunden, Onlinehandel, Customer Service, Revision, Kommunikation und Krise, Nachhaltigkeit sowie Qualität und Produktsicherheit.

## Qualitätsregeln

- Keine Skill-Datei darf bloß einen allgemeinen Ratgeber enthalten.
- Jeder Skill muss ein konkretes anwaltliches Arbeitsprodukt erzwingen.
- Jeder Skill muss sagen, was ein Top-Ergebnis von einem normalen Ergebnis unterscheidet.
- Jede Bewertung muss offene Punkte, Annahmen und fehlende Nachweise sichtbar machen.
- Dynamische Rechtsgebiete brauchen Aktualitätsprüfung und Quellenhierarchie.
- Bei deutschen Nutzern wird deutscher juristischer Stil bevorzugt: präzise, prüfungsfest, mandantenfähig.

## Struktur

Der Einstieg in die Rechts-Skills liegt unter [`recht/`](recht/). Die Unterordner entsprechen dem primären Rechtsgebiet.

Beispiele:

- `recht/vertragsrecht/vertragsversionen-vergleichen-und-aenderungen-bewerten`
- `recht/prozessrecht/schriftsatz-aus-akte-entwerfen`
- `recht/datenschutz/datenschutz-folgenabschaetzung`
- `recht/technologierecht/kuenstliche-intelligenz-systeme-klassifizieren`
- `recht/anwaltliche-arbeitsmethoden/mandantenmemo-und-entscheidungsvorlage-erstellen`
- `it-und-digital/kassensystem-stoerung-triagieren`
- `skill-erstellung/skill-generation-best-practices`

## Mitwirken

Bitte lies vor einem Beitrag [`CONTRIBUTING.md`](CONTRIBUTING.md). Neue Skills sollen echte deutsche Arbeitsprobleme lösen, sauber einsortiert sein und genau eine `SKILL.md` enthalten.

Für sicherheitsrelevante oder sensible Themen siehe [`SECURITY.md`](SECURITY.md). Bitte keine echten Mandanteninformationen, personenbezogenen Daten, Zugangsdaten oder vertraulichen Vertragsinhalte in Issues oder Pull Requests posten.

## Lizenz

Dieses Projekt steht unter der [`MIT License`](LICENSE).
