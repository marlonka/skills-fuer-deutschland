# Skills für Deutschland

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

Deutsch-first Skills für KI-Assistenten. Dieses Repository sammelt wiederverwendbare `SKILL.md`-Anweisungen für reale deutsche Arbeitsprobleme: juristische Prüfungen, anwaltliche Arbeitsprodukte, IT- und Digitalprozesse, Unternehmensarbeit und später weitere Fachbereiche.

Der Anspruch ist nicht "guter Prompt", sondern ein belastbarer Arbeitsmodus: Die KI soll wissen, welche Rolle sie einnehmen soll, welche Quellen und Prüfschritte zählen, wo typische Fehler liegen und wie ein verwertbares Ergebnis aussieht.

## Status

Das Repository ist öffentlich, MIT-lizenziert und im Aufbau.

Aktueller Stand:

- `187` Skills insgesamt.
- `136` Rechts-Skills unter `recht/`.
- `50` IT- und Digital-Skills unter `it-und-digital/`.
- `1` Meta-Skill zur Skill-Erstellung unter `skill-erstellung/`.

Wichtig: Die Skills ersetzen keine anwaltliche, technische oder fachliche Verantwortung. Sie verbessern Entwürfe, Prüfstrukturen, Reviews und Entscheidungsvorlagen. Kritische Ergebnisse müssen von qualifizierten Personen geprüft werden.

## Was dieses Repo anders macht

Viele Skill-Sammlungen sind englisch, US-geprägt oder zu allgemein. Dieses Repository ist für deutsche Nutzer gebaut:

- deutsche Begriffe, deutsche Arbeitsprodukte, deutsche Risiken;
- deutsches und europaeisches Recht, wo Recht betroffen ist;
- klare Rollen statt generischer "du bist Experte"-Sätze;
- konkrete Pruefschritte statt Ratgebertext;
- sichtbare Annahmen, offene Punkte, Nachweise und Review-Gates;
- ein Ergebnis, das in Kanzlei, Rechtsabteilung, IT, Compliance oder Fachbereich weiterverwendet werden kann.

## Strukturprinzip

Skills werden nach fachlicher Ordnung einsortiert, nicht nach Prompt-Laune oder Branche.

Beispiele:

- Rechtsarbeit liegt unter `recht/<rechtsgebiet>/<skill-name>/SKILL.md`.
- IT- und Digitalarbeit liegt unter `it-und-digital/<skill-name>/SKILL.md`.
- Meta-Skills liegen unter `skill-erstellung/<skill-name>/SKILL.md`.

Jeder Skill-Ordner enthält genau eine Datei:

```text
bereich/
  skill-name/
    SKILL.md
```

Keine `references/`, keine zusätzlichen README-Dateien im Skill-Ordner, keine verstreuten Quellen. Alles, was der jeweilige Skill für seinen Arbeitsmodus braucht, steht in seiner einen `SKILL.md`.

## Wie ein guter Skill geschrieben ist

Ein Skill muss eine spezifische, wiederholbare Aufgabe besser machen. Er ist kein Lexikonartikel und keine Sammlung allgemeiner Best Practices.

Pflichtstandard:

- `name`: lowercase, hyphen-case, identisch mit dem Ordnernamen.
- `description`: klarer Triggertext mit Aufgabe, Kontext und typischen Nutzerformulierungen.
- `Arbeitsstandard`: Rolle, Qualitätsniveau, Grenzen.
- `Quellen und Prüfstandard`: relevante Quellenhierarchie und Aktualitätslogik.
- `Was Top-Arbeit von Standardarbeit unterscheidet`: konkrete Differenz zwischen normalem Output und exzellenter Facharbeit.
- `Fachspezifische Top-Practices`: die nicht offensichtlichen Muster, die sehr gute Praktiker tatsächlich beachten.
- `Arbeitsablauf`: zwingende Reihenfolge.
- `Ausgabe`: verwertbare Ergebnisform.
- `Qualitätskontrolle`: kurze Prüffragen gegen Lücken, Scheinsicherheit und falsche Prioritäten.

Minimaler Header:

```yaml
---
name: beschreibender-skill-name
description: Erstellt oder prüft ein konkretes Arbeitsprodukt für klar benannte Einsatzfälle und Trigger.
---
```

## Qualitätslinie

Ein Skill ist erst gut, wenn ein sehr guter Praktiker sagen würde: "Das erspart mir echte Arbeit, weil die KI schon in der richtigen Denkstruktur startet."

Das bedeutet:

- keine generischen Sicherheitsblöcke, die in jedem Skill gleich klingen;
- keine erfundenen Normen, Fundstellen, Ursachen oder technischen Gewissheiten;
- keine pauschalen Entwarnungen;
- keine "AI slop"-Formulierungen;
- keine künstliche Vollständigkeit, wenn Sachverhalt, Logs, Dokumente oder Nachweise fehlen;
- keine Vermischung von Fakten, Annahmen, Hypothesen, Bewertung und Empfehlung;
- keine Skills, die mehrere unterschiedliche Berufe oder Workflows unklar zusammenwerfen.

## Abgedeckte Bereiche

Unter `recht/` sind bereits viele deutsche Rechtsgebiete und anwaltliche Arbeitsmethoden angelegt, unter anderem Datenschutz, Technologierecht, Vertragsrecht, Mietrecht, Prozessrecht, Arbeitsrecht, Wettbewerbsrecht, Urheberrecht, Gesellschaftsrecht, Compliance-nahe Themen und anwaltliche Querschnittsarbeit.

Unter `it-und-digital/` sind allgemeingültige Skills für IT-Betrieb, Incident- und Problem-Management, Anforderungen, Releases, Architektur, Schnittstellen, Daten, Cloud, Security, Migration, Dokumentation, Support, Produktarbeit, Automatisierung und IT-Steuerung angelegt.

Unter `skill-erstellung/` liegt ein Meta-Skill, der beim Erstellen, Pruefen und Verbessern neuer Skills helfen soll.

## Was als Nächstes sinnvoll ist

Naheliegende Ausbaupfade:

- weitere Kanzlei- und Inhouse-Workflows: Aktenchronologie, Dokumentenreview, Anlagenmapping, Mandatsrisiko, Legal Intake, Vertragsfreigabe;
- weitere Unternehmensbereiche: Personal, Einkauf, Supply Chain, Logistik, Finanzen, Controlling, Marketing, Kundenservice, Revision, Immobilien, Expansion, Nachhaltigkeit;
- weitere regulierte Branchen: Gesundheit, Energie, Finanzen, Telekommunikation, Versicherung, öffentliche Verwaltung;
- weitere Bürger- und Verbraucherprobleme: Reisen, Bank, Versicherung, Telekommunikation, Kaufrecht, Handwerker, Behördenbescheide.

## Validierung

Lokale Strukturprüfung:

```powershell
python scripts\validate_skills.py
```

Der Validator prüft unter anderem:

- parsebares YAML-Frontmatter;
- nur `name` und `description`;
- Ordnername entspricht Skill-Name;
- genau eine `SKILL.md` je Skill-Ordner;
- Pflichtabschnitte vorhanden;
- ausreichende Trigger-Description.

## Mitwirken

Bitte vor einem Beitrag [`CONTRIBUTING.md`](CONTRIBUTING.md) lesen. Neue Skills sollen echte deutsche Arbeitsprobleme lösen, sauber einsortiert sein und den Qualitätsstandard sichtbar erhöhen.

Für sensible oder sicherheitsrelevante Themen gilt [`SECURITY.md`](SECURITY.md). Keine echten Mandantendaten, personenbezogenen Daten, Zugangsdaten, Tokens oder vertraulichen Dokumentinhalte in Issues oder Pull Requests posten.

## Lizenz

Dieses Projekt steht unter der [`MIT License`](LICENSE).
