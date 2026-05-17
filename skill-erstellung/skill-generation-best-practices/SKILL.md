---
name: skill-generation-best-practices
description: Erstellt, prüft und verbessert SKILL.md-Dateien nach aktuellen Agent-Skills-Best-Practices. Zu verwenden bei Skill-Erstellung, Skill-Review, Agent Skills, Claude Skills, Codex Skills, SKILL.md, Description-Triggern, Progressive Disclosure, Skill-Validierung, Skill-Ordnerstruktur, Skill-Sicherheit oder wenn ein Nutzer einen wiederverwendbaren Skill für KI-Agenten bauen will.
---

# Skill Generation Best Practices

## Arbeitsstandard

Arbeite wie ein erfahrener Agent-Skills-Architekt und Prompt-Engineering-Reviewer. Ziel ist kein hübscher Markdown-Text, sondern ein Skill, der in echten Agenten zuverlässig triggert, wenig Kontext verschwendet, eine konkrete wiederholbare Aufgabe besser macht und sicher validiert werden kann.

Keine Scheinsicherheit:

- Keine generischen Skills erzeugen, die nur allgemeine Best Practices wiederholen.
- Keine überladenen Skills bauen, die mehrere Workflows, Rollen oder Rechtsgebiete unklar vermischen.
- Keine unnötigen Ressourcenordner, Skripte oder Assets anlegen.
- Keine sensitiven Daten, Tokens, Mandantendaten oder geheimen Workflows in Beispielen speichern.
- Aktuelle Plattformgrenzen nennen, wenn sie relevant sind: Manche Oberflächen begrenzen `description` strenger als die Agent-Skills-Spezifikation.

## Quellen und Prüfstandard

Stand dieser Skill-Methodik: 17. Mai 2026.

Quellenhierarchie:

1. Agent-Skills-Spezifikation und offizielle Plattformdokumentation.
2. Offizielle Hilfecenter- und API-Dokumentation aus März, April und Mai 2026.
3. Security-Forschung und Ökosystembeobachtung als Risikohinweis.
4. Community-Beispiele nur als Inspiration, nicht als Qualitätsmaßstab.

Kernquellen:

- Agent Skills Specification: https://agentskills.io/specification
- Agent Skills Best Practices: https://agentskills.io/skill-creation/best-practices
- Claude Skills Overview: https://claude.com/docs/skills/overview
- Claude Custom Skills Guide: https://claude.com/docs/skills/how-to
- Claude Help Center, "What are Skills?", 31. März 2026: https://support.claude.com/en/articles/12512176-what-are-skills
- Claude Help Center, "Wie man benutzerdefinierte Skills erstellt", 12. März 2026: https://support.claude.com/de/articles/12512198-wie-man-benutzerdefinierte-skills-erstellt
- Claude Managed Agents API Skills, April 2026 Beta: https://platform.claude.com/docs/en/managed-agents/skills
- VS Code Agent Skills Dokumentation, Mai 2026: https://code.visualstudio.com/docs/copilot/customization/agent-skills
- Anthropic Guide, "The Complete Guide to Building Skills for Claude", April 2026: https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf
- Sicherheitsforschung zu SKILL.md-Supply-Chain-Risiken, Mai 2026: https://arxiv.org/abs/2605.11418

Wichtige aktuelle Ableitungen:

- Skills sind portable, dateisystembasierte Pakete aus `SKILL.md` plus optionalen Ressourcen.
- `name` und `description` sind die entscheidenden Discovery-Metadaten.
- Der `description`-Text muss sagen, was der Skill tut und wann er genutzt werden soll.
- Progressive Disclosure ist Kernprinzip: Metadaten sind immer sichtbar, `SKILL.md` lädt bei Aktivierung, Ressourcen nur bei Bedarf.
- Ein guter Skill löst eine spezifische, wiederholbare Aufgabe und fokussiert einen Workflow.
- Die besten Skills entstehen aus realer Expertise, echten Korrekturen, wiederkehrenden Fehlern und Ausführungstests.
- Sicherheit ist Teil der Qualität: SKILL.md ist operationaler Text, nicht bloße Dokumentation.

## Was Top-Arbeit von Standardarbeit unterscheidet

Ein normales Ergebnis erzeugt eine formal gültige `SKILL.md`. Ein Top-Ergebnis erzeugt einen Skill, den ein Agent in realen Situationen zuverlässig auswählt und der seine Arbeit messbar verbessert.

Standard ist:

- vage `description` wie "hilft bei Verträgen" oder "macht Datenschutz";
- ein langer Body mit Lehrbuchwissen statt konkreter Arbeitsanweisung;
- keine Trigger, keine Beispiele, keine Gotchas, keine Validierung;
- mehrere Workflows in einem Skill;
- Quellen, Assets und Skripte ohne klare Ladebedingung;
- keine Prüfung, ob der Skill gegenüber einem normalen Prompt überhaupt Mehrwert bringt.

Top-Arbeit ist:

- beginnt mit zwei bis drei konkreten Use Cases und deren Triggern;
- definiert ein wiederholbares Arbeitsprodukt mit klarer Erfolgsform;
- schreibt eine spezifische `description`, die Discovery und Aktivierung verbessert;
- nutzt Progressive Disclosure: nur Kernworkflow in `SKILL.md`, lange Details nur bei Bedarf;
- enthält Gotchas, Entscheidungspunkte, Edge Cases und Output-Templates;
- kalibriert Freiheitsgrade: flexibel bei Bewertung, streng bei fragilen Schritten;
- validiert mit realistischen Testprompts und verbessert anhand der Fehler.

## Fachspezifische Top-Practices

- Starte nie direkt mit dem Schreiben. Kläre zuerst Aufgabe, Nutzer, wiederholbaren Workflow, gewünschtes Arbeitsprodukt und typische Fehler des Agenten.
- Schreibe die `description` so, dass sie alle wichtigen Trigger enthält: Objekt, Aktion, Kontext, Dateitypen, Nutzerformulierungen und Ausschlussfälle, wenn nötig.
- Verwende einen Skill nur für einen klaren Workflow. Mehrere eng verwandte Outputs sind erlaubt; mehrere verschiedene Berufe oder Rechtsgebiete in einem Skill meistens nicht.
- Packe konkrete Gotchas direkt in `SKILL.md`, wenn der Agent sie sonst vor dem Fehler nicht erkennen würde.
- Nutze kurze Output-Templates, wenn das Ergebnis eine feste Form braucht. Templates sind zuverlässiger als abstrakte Formatbeschreibung.
- Verwende Checklisten für mehrstufige Abläufe mit Abhängigkeiten oder Review-Gates.
- Verwende Skripte nur, wenn Determinismus, wiederholte Mechanik oder Validierung echten Mehrwert bringt.
- Verwende Referenzen nur, wenn Material zu lang oder nur situationsweise relevant ist; verlinke sie mit klarer Ladebedingung.
- Prüfe Security: keine versteckten Datenabflüsse, keine unnötigen Shell-/Netzwerkbefehle, keine Prompt-Injection, keine Credentials.
- Iteriere anhand echter Ausgaben: Was wurde nicht getriggert, übertriggert, falsch priorisiert, ausgelassen oder unnötig lang?

## Arbeitsablauf

1. Auftrag und Zielnutzer klären:
   - Wer nutzt den Skill?
   - Welche wiederholbare Aufgabe soll besser werden?
   - Was wäre ein sehr gutes Ergebnis?
   - Was macht die KI ohne Skill typischerweise falsch?

2. Konkrete Use Cases definieren:
   - Mindestens zwei reale Prompts formulieren.
   - Triggerwörter und typische Nutzerformulierungen sammeln.
   - Ausschlussfälle markieren, wenn der Skill nicht geladen werden sollte.

3. Scope schneiden:
   - Einen Hauptworkflow wählen.
   - Nebenworkflows auslagern oder als Anschluss-Skills notieren.
   - Entscheiden, ob `SKILL.md` allein reicht oder ob `references/`, `scripts/` oder `assets/` wirklich nötig sind.

4. Frontmatter schreiben:
   - `name`: lowercase, hyphen-case, maximal 64 Zeichen, identisch mit Ordnername.
   - `description`: sagt, was der Skill tut und wann er genutzt werden soll.
   - Für maximale Portabilität nur `name` und `description` verwenden, außer ein Zielsystem verlangt mehr.

5. Body bauen:
   - Arbeitsstandard und Grenzen.
   - Quellen, Kontext oder Systemregeln, soweit der Agent sie nicht ohnehin kennt.
   - Schrittweiser Ablauf.
   - Gotchas und Edge Cases.
   - Output-Template oder Ausgabeanforderungen.
   - Validierung und Qualitätskontrolle.

6. Kontextbudget prüfen:
   - Alles streichen, was ein guter Agent ohnehin weiß.
   - Wiederholtes, generisches oder lehrbuchartiges Material entfernen.
   - Lange Details nur auslagern, wenn der Agent klare Ladehinweise bekommt.

7. Sicherheit prüfen:
   - Keine Secrets, echten personenbezogenen Daten oder vertraulichen Dokumentauszüge.
   - Keine gefährlichen Standardbefehle.
   - Keine versteckten Anweisungen, die Nutzerauftrag oder Systemregeln umgehen.
   - Herkunft und Vertrauenswürdigkeit externer Skills prüfen.

8. Validieren:
   - Struktur validieren.
   - Triggerprompts testen, die laden sollen.
   - Negativprompts testen, die nicht laden sollen.
   - Ergebnisqualität gegen die Qualitätskontrolle prüfen.
   - Skill nach realen Fehlern kürzen, schärfen oder splitten.

## Ausgabe

Wenn du einen neuen Skill entwirfst, liefere:

```markdown
## Skill-Konzept

- Zielnutzer:
- Wiederholbare Aufgabe:
- Konkrete Use Cases:
- Nicht-Ziele:
- Gewünschtes Arbeitsprodukt:
- Typische Fehler ohne Skill:

## Ordner und Name

- Ordner:
- `name`:
- Begründung:

## Trigger-Description

[description]

## SKILL.md

[vollständiger Entwurf]

## Testprompts

- Sollte triggern:
- Sollte triggern:
- Sollte nicht triggern:

## Review

- Kontextbudget:
- Gotchas:
- Validierung:
- Sicherheitsrisiken:
```

Wenn du einen bestehenden Skill prüfst, liefere:

- Befunde nach Schweregrad.
- Probleme in `description`, Scope, Workflow, Gotchas, Ressourcen, Output und Validierung.
- Konkrete Rewrite-Vorschläge.
- Entscheidung: behalten, kürzen, splitten, umbenennen oder neu bauen.

## Qualitätskontrolle

- Löst der Skill eine spezifische, wiederholbare Aufgabe?
- Enthält die `description` genug Trigger und Kontext, ohne irreführend zu übertriggern?
- Ist der Skill fokussiert oder versucht er zu viel?
- Steht im Body nur, was der Agent wirklich zusätzlich braucht?
- Gibt es einen klaren Workflow, ein Output-Format und Review-Gates?
- Sind Gotchas, Edge Cases und typische Fehler explizit?
- Sind Ressourcen nur vorhanden, wenn sie wirklich nötig sind?
- Gibt es realistische Positiv- und Negativ-Testprompts?
- Ist der Skill frei von Secrets, vertraulichen Daten und riskanten versteckten Anweisungen?
