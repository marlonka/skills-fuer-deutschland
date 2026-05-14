# Contributing

Danke für dein Interesse an `skills-fuer-deutschland`.

Dieses Repository sammelt deutschsprachige Skills für KI-Assistenten. Der Qualitätsanspruch ist hoch: Ein Skill soll nicht nur erklären, sondern ein wiederverwendbares Arbeitsmuster liefern, das deutsche Nutzer bei echten Aufgaben deutlich besser unterstützt.

## Was gute Beiträge leisten

Ein guter Beitrag:

- löst ein reales deutsches Problem;
- ist deutsch-first und nicht aus US-Templates übersetzt;
- enthält konkrete Arbeitsprodukte, etwa Prüfvermerk, Entwurf, Risikoampel, Fragenliste, Synopse oder Maßnahmenplan;
- trennt Fakten, Annahmen, offene Punkte und Bewertung;
- erklärt, was ein Top-Ergebnis von einem normalen Ergebnis unterscheidet;
- vermeidet Scheinsicherheit, erfundene Quellen und generische KI-Prosa.

## Skill-Struktur

Jeder Skill liegt in einem eigenen Ordner und enthält genau eine Datei:

```text
recht/<rechtsgebiet>/<skill-name>/SKILL.md
```

Innerhalb eines Skill-Ordners sollen keine zusätzlichen README-, Quellen- oder Hilfsdateien liegen. Quellen und Prüfstandard stehen direkt in der jeweiligen `SKILL.md`.

Frontmatter:

```yaml
---
name: skill-name-in-hyphen-case
description: Klare Trigger und Einsatzfälle.
---
```

Der Ordnername muss exakt dem `name` im Frontmatter entsprechen.

## Schreibstandard

Eine `SKILL.md` sollte diese Abschnitte enthalten:

- `Arbeitsstandard`
- `Quellen und Prüfstandard`
- `Was Top-Arbeit von Standardarbeit unterscheidet`
- `Fachspezifische Top-Practices`
- `Arbeitsablauf`
- `Ausgabe`
- `Qualitätskontrolle`

Schreibe knapp, konkret und mandatsnah. Der Skill soll der KI eine Arbeitsweise aufzwingen, nicht einen allgemeinen Lexikonartikel liefern.

## Einordnung

Ordner werden nach primärem Rechtsgebiet sortiert, nicht nach Branche, Persona oder Anlass.

Beispiele:

- Einzelhandels-Mietvertrag: `recht/mietrecht/...`
- KI im Bewerbungsprozess: `recht/arbeitsrecht/...` oder `recht/datenschutz/...`, je nach Schwerpunkt.
- Vertragsversionen vergleichen: `recht/vertragsrecht/...`
- Behördenschreiben beantworten: `recht/regelkonformitaet/...`

Wenn ein Thema mehrere Rechtsgebiete berührt, wähle das Rechtsgebiet, in dem ein deutscher Anwalt den Skill zuerst suchen würde.

## Validierung

Vor einem Pull Request bitte prüfen:

```powershell
$skills = Get-ChildItem -Path recht -Recurse -Filter SKILL.md | ForEach-Object { $_.DirectoryName }
foreach ($skill in $skills) {
  python "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" $skill
}
```

Zusätzlich sollte jeder Skill-Ordner nur eine `SKILL.md` enthalten und keine Hilfsdokumente.

## Rechtlicher Hinweis

Beiträge dürfen keine individuelle Rechtsberatung ersetzen. Skills sollen Arbeitsentwürfe und Prüfstrukturen liefern, die von qualifizierten Personen geprüft werden müssen.
