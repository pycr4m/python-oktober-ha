# Programmieraufgaben – Algorithmen

Dieses Repository enthält verschiedene Python-Programmieraufgaben aus dem Bereich **Algorithmen und grundlegende Programmierung**.

Das Programm stellt ein Hauptmenü bereit, über das drei verschiedene Berechnungen ausgeführt werden können:

1. Rückgeldberechnung
2. Rabattberechnung
3. Benzinrechner

---

## Aufgaben

### 1. Rückgeldberechnung

Der Benutzer gibt über die Konsole den **zu zahlenden Betrag** und den **gezahlten Geldbetrag** ein.

Das Programm berechnet anschließend, wie viel Rückgeld der Kunde erhält.

Wurde zu wenig bezahlt, gibt das Programm aus, wie viel Geld noch fehlt.

Wurde der genaue Betrag bezahlt, wird eine entsprechende Meldung ausgegeben.

Zusätzlich werden die Eingaben auf gültige Zahlenwerte überprüft. :chatgpt-content-reference{index="0"}

---

### 2. Rabattrechner

Der Benutzer gibt einen **Preis** und einen **Rabatt in Prozent** ein.

Anschließend berechnet das Programm:

- den Rabattbetrag in Euro
- den zu zahlenden Betrag nach Abzug des Rabatts

Ein Rabatt von mehr als 100 % bzw. ungültige Eingaben werden abgefangen.

Die Berechnung erfolgt nach folgender Formel:

Rabattbetrag = Preis × Rabatt / 100

Zahlbetrag = Preis − Rabattbetrag

### 3. Benzinrechner

Der Benzinrechner verwendet folgende Eingaben:
- gefahrene Strecke in Kilometern
- Literpreis
- verbrauchte Kraftstoffmenge
Aus diesen Werten berechnet das Programm:
- Verbrauch pro 100 km
- Kosten pro 100 km
- Kosten der gesamten Strecke    Eingefügtes Markdown
Die Berechnungen erfolgen nach folgenden Formeln:
Verbrauch pro 100 km =
Kraftstoffverbrauch × 100 / gefahrene Kilometer

Kosten pro 100 km =
Verbrauch pro 100 km × Literpreis

Kosten der Gesamtstrecke =
Literpreis × Kraftstoffverbrauch
