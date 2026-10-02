# Benötigt einmalig:  pip install customtkinter
import customtkinter as ctk

ctk.set_appearance_mode("dark")        # "dark", "light" oder "system"
ctk.set_default_color_theme("blue")    # "blue", "green" oder "dark-blue"

SCHRIFT = "Segoe UI"
ORANGE = "#ff9f1c"   # Farbe der Reiter-Beschriftung

# Farben der Ergebnis-Anzeige (hell, dunkel)
FARBEN = {
    "ok": ("#1a7f37", "#4ade80"),        # grün
    "fehlt": ("#c62828", "#ff5252"),     # rot (Fehlbetrag)
    "warnung": ("#b45309", "#facc15"),   # gelb (falsche Eingabe)
}


# ---------------------------------------------------------------
# Hilfsfunktionen (Eingabe lesen und Ausgabe formatieren)
# ---------------------------------------------------------------

def zahl_lesen(text, name, mindestens=0, groesser_als=None, hoechstens=None):
    """Wandelt einen Text in eine Zahl um (Komma oder Punkt erlaubt)."""
    text = text.strip().replace(",", ".")
    if text == "":
        raise ValueError(f"{name}: Bitte einen Wert eingeben.")
    try:
        wert = float(text)
    except ValueError:
        raise ValueError(f"{name}: Bitte eine Zahl eingeben.")

    if mindestens is not None and wert < mindestens:
        raise ValueError(f"{name}: Der Wert darf nicht kleiner als {mindestens} sein.")
    if groesser_als is not None and wert <= groesser_als:
        raise ValueError(f"{name}: Der Wert muss größer als {groesser_als} sein.")
    if hoechstens is not None and wert > hoechstens:
        raise ValueError(f"{name}: Der Wert darf nicht größer als {hoechstens} sein.")
    return wert


def zahl(wert):
    return f"{wert:.2f}".replace(".", ",")


def euro(betrag):
    return f"{zahl(betrag)} €"


# ---------------------------------------------------------------
# Berechnungen (bekommen die Eingaben als Text, geben Text zurück)
# ---------------------------------------------------------------

def rueckgeld(werte):
    preis = zahl_lesen(werte["preis"], "Preis")
    geld = zahl_lesen(werte["geld"], "Gezahlter Betrag")
    wechselgeld = round(geld - preis, 2)

    if wechselgeld > 0:
        return f"Dein Wechselgeld beträgt {euro(wechselgeld)}.", "ok"
    elif wechselgeld < 0:
        return f"Es fehlen noch {euro(-wechselgeld)}.", "fehlt"
    return "Der Zahlbetrag ist beglichen.", "ok"


def rabatt(werte):
    preis = zahl_lesen(werte["preis"], "Preis")
    prozent = zahl_lesen(werte["rabatt"], "Rabatt", groesser_als=0, hoechstens=100)
    rabatt_in_euro = preis * prozent / 100
    zahlbetrag = round(preis - rabatt_in_euro, 2)
    return (f"Der Zahlbetrag beträgt {euro(zahlbetrag)}\n"
            f"bei einem Rabatt von {zahl(prozent)} % (= {euro(rabatt_in_euro)}).", "ok")


def benzin(werte):
    km = zahl_lesen(werte["km"], "Gefahrene Kilometer", groesser_als=0)
    literpreis = zahl_lesen(werte["literpreis"], "Literpreis")
    liter = zahl_lesen(werte["liter"], "Kraftstoffverbrauch")

    verbrauch100km = liter * 100 / km
    kosten100km = verbrauch100km * literpreis
    kosten_gesamt = literpreis * liter
    return (f"Verbrauch pro 100 km: {zahl(verbrauch100km)} l\n"
            f"Kosten pro 100 km: {euro(kosten100km)}\n"
            f"Kosten der Gesamtstrecke: {euro(kosten_gesamt)}", "ok")


# ---------------------------------------------------------------
# Oberfläche
# ---------------------------------------------------------------

class RechnerTab(ctk.CTkFrame):
    """Ein Reiter mit Eingabefeldern, Button und Ergebnis-Karte."""

    def __init__(self, master, felder, berechnen):
        super().__init__(master, fg_color="transparent")
        self.berechnen = berechnen
        self.eingaben = {}

        for schluessel, beschriftung, platzhalter in felder:
            ctk.CTkLabel(self, text=beschriftung, font=(SCHRIFT, 16), anchor="w").pack(
                fill="x", padx=20, pady=(14, 2))
            eintrag = ctk.CTkEntry(self, height=44, corner_radius=12,
                                   font=(SCHRIFT, 18), placeholder_text=platzhalter)
            eintrag.pack(fill="x", padx=20)
            eintrag.bind("<Return>", lambda event: self.ausfuehren())  # Enter = Berechnen
            self.eingaben[schluessel] = eintrag

        ctk.CTkButton(self, text="Berechnen", height=48, corner_radius=12,
                      font=(SCHRIFT, 18, "bold"), command=self.ausfuehren).pack(
            fill="x", padx=20, pady=(22, 10))

        karte = ctk.CTkFrame(self, corner_radius=14, fg_color=("gray85", "gray17"))
        karte.pack(fill="both", expand=True, padx=20, pady=(4, 20))
        self.ergebnis = ctk.CTkLabel(karte, text="Das Ergebnis erscheint hier.",
                                     font=(SCHRIFT, 17), justify="left", anchor="nw",
                                     wraplength=440, text_color="gray60")
        self.ergebnis.pack(fill="both", expand=True, padx=16, pady=14)

        next(iter(self.eingaben.values())).focus()

    def ausfuehren(self):
        werte = {schluessel: eintrag.get() for schluessel, eintrag in self.eingaben.items()}
        try:
            text, art = self.berechnen(werte)
            self.ergebnis.configure(text=text, text_color=FARBEN[art])
        except ValueError as fehler:
            self.ergebnis.configure(text=f"⚠ {fehler}", text_color=FARBEN["warnung"])


def main():
    fenster = ctk.CTk()
    fenster.title("Rechner")
    fenster.geometry("640x680")
    fenster.minsize(540, 600)

    ctk.CTkLabel(fenster, text="Rechner", font=(SCHRIFT, 30, "bold")).pack(pady=(22, 8))

    reiter = ctk.CTkTabview(fenster, corner_radius=16, text_color=ORANGE,
                            segmented_button_selected_color="#1e1e1e",
                            segmented_button_selected_hover_color="#2a2a2a")
    reiter._segmented_button.configure(font=(SCHRIFT, 20, "bold"), height=44)
    reiter.pack(fill="both", expand=True, padx=20, pady=(0, 10))

    seiten = [
        ("Rückgeld",
         [("preis", "Preis (€)", "z. B. 6,60"), ("geld", "Gezahlt (€)", "z. B. 8,99")],
         rueckgeld),
        ("Rabatt",
         [("preis", "Preis (€)", "z. B. 80"), ("rabatt", "Rabatt (%)", "z. B. 15")],
         rabatt),
        ("Benzin",
         [("km", "Gefahrene Kilometer", "z. B. 1200"),
          ("literpreis", "Literpreis (€)", "z. B. 2,70"),
          ("liter", "Verbrauch (Liter)", "z. B. 90")],
         benzin),
    ]
    for name, felder, funktion in seiten:
        seite = reiter.add(name)
        RechnerTab(seite, felder, funktion).pack(fill="both", expand=True)

    ctk.CTkButton(fenster, text="Beenden", height=40, corner_radius=12, font=(SCHRIFT, 15),
                  fg_color="transparent", border_width=2, text_color=("gray20", "gray80"),
                  command=fenster.destroy).pack(pady=(0, 18))

    fenster.mainloop()


if __name__ == "__main__":
    main()