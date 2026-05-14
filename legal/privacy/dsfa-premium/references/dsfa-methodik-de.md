# DSFA-Methodik Deutschland

## Zweck

Diese Referenz beschreibt eine deutsche Premium-Arbeitsweise für Datenschutz-Folgenabschätzungen (DSFA) nach Art. 35 DSGVO. Ziel ist ein mandantenfähiger Entwurf, der Sachverhalt, Recht, Technik und Risiko nachvollziehbar verbindet.

## Inhaltsverzeichnis

1. Prüfungslogik
2. Schwellwertanalyse
3. Sachverhaltsmodell
4. Notwendigkeit und Verhältnismäßigkeit
5. Risikomodell
6. Maßnahmenplan
7. Art.-36-Prüfung
8. Musterstruktur
9. Typische deutsche Hochrisiko-Konstellationen

## 1. Prüfungslogik

Eine starke DSFA beantwortet vier Fragen:

1. Was genau wird mit welchen Daten über welche Personen getan?
2. Warum ist die Verarbeitung rechtlich, fachlich und technisch erforderlich?
3. Welche Risiken entstehen für Rechte und Freiheiten natürlicher Personen?
4. Welche Maßnahmen senken diese Risiken auf ein vertretbares Niveau?

Arbeite nicht vom gewünschten Ergebnis rückwärts. Beginne beim Verarbeitungsvorgang, prüfe dann Pflicht, Verhältnismäßigkeit, Risiken, Maßnahmen und Restrisiko.

## 2. Schwellwertanalyse

Eine DSFA ist insbesondere naheliegend, wenn mehrere Risikofaktoren zusammenkommen:

- systematische Bewertung persönlicher Aspekte,
- Profiling, Scoring oder automatisierte Entscheidung,
- umfangreiche Verarbeitung sensibler Daten,
- Beschäftigtendaten mit Kontroll-, Leistungs- oder Verhaltensbezug,
- Video-, Audio- oder Standortüberwachung,
- neue oder schwer durchschaubare Technologien,
- Datenzusammenführung aus verschiedenen Quellen,
- Verarbeitung vulnerabler Gruppen,
- große Reichweite, lange Speicherfristen oder schwer reversibler Schaden,
- Ausschluss, Benachteiligung oder erhebliche Beeinträchtigung durch Fehlentscheidungen.

Formuliere das Ergebnis nicht nur als "DSFA erforderlich". Begründe, welche konkreten Faktoren die Schwelle tragen.

## 3. Sachverhaltsmodell

Eine belastbare DSFA braucht mindestens diese Bausteine:

- Verantwortlicher, Auftragsverarbeiter, gemeinsame Verantwortliche.
- Verarbeitungsvorgang mit Systemgrenzen.
- Zwecke und ausdrücklich ausgeschlossene Zwecke.
- Datenkategorien, besondere Kategorien und abgeleitete Daten.
- Betroffenengruppen.
- Datenquellen und Erhebungsweg.
- Empfänger und Schnittstellen.
- Drittlandtransfers und Transferinstrumente.
- Speicherfristen, Löschregeln und Protokolldaten.
- Rollen- und Berechtigungskonzept.
- technische Architektur auf verständlichem Niveau.

Wenn diese Informationen fehlen, erstelle keine endgültige DSFA. Erstelle einen strukturierten Entwurf mit Annahmen und offenen Punkten.

## 4. Notwendigkeit und Verhältnismäßigkeit

Prüfe in dieser Reihenfolge:

1. Legitime und konkretisierte Zwecke.
2. Passende Rechtsgrundlage je Zweck.
3. Geeignetheit der Verarbeitung zur Zweckerreichung.
4. Erforderlichkeit: Gibt es mildere, weniger invasive Mittel?
5. Angemessenheit: Stehen Nutzen und Eingriff in einem vertretbaren Verhältnis?
6. Datenschutzgrundsätze: Datenminimierung, Speicherbegrenzung, Transparenz, Integrität, Vertraulichkeit.
7. Betroffenenrechte und praktische Durchsetzbarkeit.

Bei KI-Systemen zusätzlich prüfen:

- Trainings-, Validierungs- und Produktivdaten trennen.
- Input-, Output- und Logdaten getrennt betrachten.
- Halluzinationen, Bias, Fehlklassifikationen und menschliche Übersteuerung berücksichtigen.
- Keine unkontrollierte Zweckänderung durch Wiederverwendung von Daten.
- Modellanbieter, Hosting, Telemetrie und Drittlandrisiken sichtbar machen.

## 5. Risikomodell

Bewerte Risiken aus Sicht der betroffenen Person. Unternehmensrisiken sind nur relevant, soweit sie Betroffenenrisiken erklären.

Empfohlenes Raster:

- Risikoereignis: Was kann passieren?
- Ursache: Wodurch kann es passieren?
- Betroffenenschaden: Welche Folge entsteht für Personen?
- Eintrittswahrscheinlichkeit: niedrig, mittel, hoch.
- Schadensschwere: niedrig, mittel, hoch.
- Bruttorisiko: vor zusätzlichen Maßnahmen.
- bestehende Maßnahmen.
- zusätzliche Maßnahmen.
- Restrisiko: nach Maßnahmen.
- Verantwortlicher und Frist.

Typische Risikoereignisse:

- unberechtigter Zugriff,
- fehlerhafte oder diskriminierende Entscheidung,
- unzutreffende Profilbildung,
- Kontrollverlust über sensible Daten,
- Zweckentfremdung,
- Intransparenz,
- mangelnde Ausübung von Betroffenenrechten,
- Überwachungseffekt,
- Re-Identifikation,
- Drittlandzugriff ohne wirksame Schutzmechanismen.

## 6. Maßnahmenplan

Maßnahmen müssen operationalisierbar sein. Gute Maßnahmen haben Owner, Frist, Wirksamkeitskriterium und Bezug zum Risiko.

Beispiele für Maßnahmengruppen:

- Technisch: Verschlüsselung, Zugriffstrennung, Pseudonymisierung, Logging, Löschautomation, Mandantentrennung, Monitoring.
- Organisatorisch: Rollenmodell, Schulung, Freigabeprozess, Vier-Augen-Prinzip, Incident-Prozess, regelmäßige Reviews.
- Rechtlich: AVV, Joint-Controller-Vereinbarung, Transfer Impact Assessment, Datenschutzhinweise, Betriebsvereinbarung.
- KI-spezifisch: Human-in-the-loop, Bias-Tests, Drift-Monitoring, Prompt-/Output-Logging mit Löschkonzept, Sperrlisten für sensible Inputs, Modellkarten.

Vermeide Maßnahmen ohne Prüfpunkt. "Mitarbeiter werden sensibilisiert" ist schwach. Besser: "Pflichtschulung vor Systemzugriff, jährliche Wiederholung, dokumentierte Teilnahmequote, Stichprobenprüfung in Quartalsreviews."

## 7. Art.-36-Prüfung

Am Ende ausdrücklich entscheiden:

- Bleibt trotz Maßnahmen ein hohes Risiko für Rechte und Freiheiten?
- Wenn ja: Vorabkonsultation der zuständigen Aufsichtsbehörde vorbereiten.
- Wenn nein: begründen, warum die Restrisiken akzeptabel sind und welche Nachkontrolle vorgesehen ist.

Eine hohe Eingriffsintensität kann auch bei guten TOMs eine Eskalation rechtfertigen, wenn Fehlentscheidungen schwerwiegend, schwer erkennbar oder schwer korrigierbar sind.

## 8. Musterstruktur

Für einen DSFA-Bericht:

1. Executive Summary
2. Auftrag, Prüfungsmaßstab und Quellen
3. Beschreibung des Verarbeitungsvorgangs
4. DSFA-Pflicht und Schwellwertanalyse
5. Notwendigkeit und Verhältnismäßigkeit
6. Risiken für Betroffene
7. bestehende und zusätzliche Schutzmaßnahmen
8. Restrisiko und Entscheidung
9. Art.-36-Prüfung
10. offene Punkte und nächste Schritte
11. Anlagen: Datenfluss, TOMs, Verträge, Informationspflichten, Löschkonzept

Für eine Schwellwertanalyse:

1. Kurzfazit
2. Sachverhalt
3. Risikofaktoren
4. Gegenargumente
5. Empfehlung
6. benötigte Informationen

## 9. Typische deutsche Hochrisiko-Konstellationen

- KI-gestütztes Bewerber-Screening oder Performance-Management.
- Videoüberwachung in öffentlich zugänglichen Bereichen oder am Arbeitsplatz.
- Gesundheitsdaten, biometrische Daten oder Daten über Kinder.
- Betrugsprävention, Bonitätsprüfung, Scoring und Sperrlisten.
- Standorttracking von Beschäftigten oder Kunden.
- Large-scale CRM-/Marketing-Profiling mit Datenanreicherung.
- GenAI-Assistenten mit vertraulichen Kunden-, Mandanten-, Patienten- oder Beschäftigtendaten.
- Systeme, bei denen Betroffene Entscheidungen kaum erkennen, verstehen oder anfechten können.
