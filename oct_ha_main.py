def rückgeld():
#get input preis
    while True:
        while True:
            try:
                preis = float(input("Wie hoch ist der \033[1mPreis\033[0m? (in €) \t\t\t\t>>> :   ").replace(",","."))
                if preis <= 0:
                    print()
                    print("Der Preis muss größer als 0 sein!")
                    print()
                else:
                    break
            except ValueError:
                print()
                print("Der Preis muss INT oder FLOAT sein!")
                print()
# kontrolle preis korrekt?
        antwort_preis = input(f"Ist der eingegebene Preis \033[1;33m{preis:.2f}€\033[0m korrekt? (\033[1;32mJ\033[0m/\033[1;31mn\033[0m)   \t>>> :   ".replace(".",","))
        if antwort_preis == "j" or antwort_preis == "ja" or antwort_preis == "J" or antwort_preis == "Ja" or antwort_preis == "":
            break
# get input geld
    while True:
        while True:
            try:
                geld = float(input("Wie viel wurde gezahlt? (in €) \t\t\t\t>>> :   ").replace(",","."))
                if geld < 0:
                    print()
                    print("Der Preis muss 0 oder größer sein!")
                    print()
                else:
                    break
            except ValueError:
                print()
                print("Der Preis muss INT oder FLOAT sein!")
                print()
# kontrolle geld korrekt?
        antwort_geld = input(f"Ist der Zahlbetrag \033[1;33m{geld:.2f}€\033[0m korrekt? (\033[1;32mJ\033[0m/\033[1;31mn\033[0m)   \t\t>>> :   ".replace(".",","))
        if antwort_geld == "j" or antwort_geld == "ja" or antwort_geld == "J" or antwort_geld == "Ja" or antwort_geld == "":
            break

    wechselgeld = geld - preis

    if wechselgeld > 0:
        print("#########################################################")
        print("#\t\t\t\t\t\t\t#")
        print(f"#\tDein Wechselgeld beträgt \033[1;4;32m{wechselgeld:.2f}€\033[0m".replace(".",","),".   \t\t#", sep="")
        print("#\t\t\t\t\t\t\t#")
        print("#########################################################")
        print()
    elif wechselgeld < 0:
        print()
        print("#########################################################")
        print("#\t\t\t\t\t\t\t#")
        print(f"#\tEs fehlen noch \033[1;4;31m{(wechselgeld*-1):.2f}€\033[0m!\t\t\t\t#".replace(".",","))
        print("#\t\t\t\t\t\t\t#")
        print("#########################################################")
        print()
    else:
        print()
        print("#########################################################")
        print("#\t\t\t\t\t\t\t#")
        print("#\t\033[32mDer Zahlbetrag ist \033[0m\033[1;32mbeglichen\033[0m.\t\t\t#")
        print("#\t\t\t\t\t\t\t#")
        print("#########################################################")
        print()

#####################################################################################################

def rabattrechner():
    while True:
        while True:
            try:
                preis = float(input("Wie hoch ist der \033[1mPreis\033[0m? (in €) \t\t\t\t>>> :   ").replace(",","."))
                if preis <= 0:
                    print()
                    print("Der Preis muss 0 oder größer sein!")
                    print()
                else:
                    break
            except ValueError:
                print()
                print("Der Preis muss ein Positiver Float sein!")
                print()
        antwort_preis = input(f"Ist der eingegebene Preis \033[1;33m{preis:.2f}€\033[0m korrekt? (\033[1;32mJ\033[0m/\033[1;31mn\033[0m) \t>>> :   ".replace(".",","))
        if antwort_preis == "j" or antwort_preis == "ja" or antwort_preis == "J" or antwort_preis == "Ja" or antwort_preis == "":
            break

    while True:
        while True:
            try:
                rabatt = float(input("Wie hoch ist der gewährte \033[1mRabatt\033[0m? (in %) \t\t>>> :   ").replace(",","."))
                if rabatt > 100 or rabatt <= 0:
                    print("Der gewährte Rabatt muss zwischen 0 und 100 Prozent liegen!")
                else:
                    break
            except ValueError:
                print("Der gewährte Rabatt muss ein Positiver Float sein!")
        antwort_rabatt = input(f"Ist der eingegebene Rabatt \033[1;33m{rabatt:.1f}%\033[0m korrekt? (\033[1;32mJ\033[0m/\033[1;31mn\033[0m) \t>>> :   ".replace(".",","))
        if antwort_rabatt == "j" or antwort_rabatt == "ja" or antwort_rabatt == "J" or antwort_rabatt == "Ja" or antwort_rabatt == "":
            break

    rabatt_in_euro = preis * rabatt / 100
    zahlbetrag = round(preis - rabatt_in_euro,2)
    print()
    print(f"Der Zahlbetrag beträgt \033[4m{zahlbetrag:.2f}€\033[0m bei einem gewährten Rabatt von {rabatt:.1f}% ({rabatt_in_euro:.2f}€)".replace(".",","),".", sep="")
    print()

####################################################################################

def benzinrechner():
    kraftstoffverbrauch = 0
    gefahrene_km = 0
    literpreis = 0

# get gefahrene km
    while True:
        while True:
            try:
                gefahrene_km = int(input("Wie viel \033[1mKilometer\033[0m wurden insgesamt zurückgelegt? \t>>> :   "))
                if gefahrene_km < 0:
                    print("Die gefahrenen Kilometer müssen ein positiver INT sein!")
                else:
                    break
            except ValueError:
                print("Die gefahrenen Kilometer müssen ein positiver INT sein!")
# kontrolle literpreis korrekt?
        antwort_km = input(f"Sind die \033[1;33m{gefahrene_km}km\033[0m korrekt? (\033[1;32mJ\033[0m/\033[1;31mn\033[0m) \t\t\t\t>>> :   ")
        if antwort_km == "j" or antwort_km == "ja" or antwort_km == "J" or antwort_km == "Ja" or antwort_km == "":
            break

# get literpreis
    while True:
        while True:
            try:
                literpreis = float(input("Wie hoch ist der \033[1mLiterpreis\033[0m? (in €) \t\t\t>>> :   ").replace(",","."))
                if literpreis < 0:
                    print("Der Literpreis muss ein positiver Float sein!")
                else:
                    break
            except ValueError:
                print("Der Literpreis muss ein positiver Float sein!")
# kontrolle literpreis korrekt?
        antwort_literpreis = input(f"Ist der Literpreis \033[1;33m{literpreis:.2f}€\033[0m korrekt? (\033[1;32mJ\033[0m/\033[1;31mn\033[0m) \t\t>>> :   ".replace(".",","))
        if antwort_literpreis == "j" or antwort_literpreis == "ja" or antwort_literpreis == "J" or antwort_literpreis == "Ja" or antwort_literpreis == "":
            break

# get kraftstoffverbrauch
    while True:
        while True:
            try:
                kraftstoffverbrauch = int(input("Wie viel Kraftstoff wurde verbraucht? (in l) \t\t>>> :   "))
                if kraftstoffverbrauch < 0:
                    print("Der Kraftstoffverbrauch muss ein positiver INT sein!")
                else:
                    break
            except ValueError:
                print("Der Kraftstoffverbrauch muss ein positiver INT sein!")
# kontrolle kraftstoffverbrauch korrekt?
        antwort_kraftstoffverbrauch = input(f"Ist der Kraftstoffverbrauch \033[1;33m{kraftstoffverbrauch}l\033[0m korrekt? (\033[1;32mJ\033[0m/\033[1;31mn\033[0m) \t>>> :   ")
        if antwort_kraftstoffverbrauch == "j" or antwort_kraftstoffverbrauch == "ja" or antwort_kraftstoffverbrauch == "J" or antwort_kraftstoffverbrauch == "Ja" or antwort_kraftstoffverbrauch == "":
            break

    verbrauch100km = kraftstoffverbrauch * 100 / gefahrene_km
    kosten100km = verbrauch100km * literpreis
    kostengesamtstrecke = literpreis * kraftstoffverbrauch
    print()
    print("#########################################################")
    print("#\t\t\t\t\t\t\t#")
    print(f"#\tVerbrauch pro 100km\t\t:  \033[4m{verbrauch100km:.0f}l\033[0m\t\t#")
    print(f"#\tKosten pro 100km\t\t:  \033[4m{kosten100km:.2f}€\033[0m\t#".replace(".",","))
    print(f"#\tKosten der Gesamtstrecke\t:  \033[4m{kostengesamtstrecke:.2f}€\033[0m\t#".replace(".",","))
    print("#\t\t\t\t\t\t\t#")
    print("#########################################################")
    print()


"""
START ###################################################################################################
"""
print("\033[?1049h\033[H")

schleifencounter = 0

while True:
    try:
        if schleifencounter == 1:
            fortsetzen = (input("Wähle (\033[1;33mm\033[0m), um ins Hauptmenü zu gelangen\nund (\033[1;31me\033[0m), um das Programm zu beenden. (\033[1;33mM\033[0m/\033[1;31me\033[0m) \t\t>>> :   "))
            if fortsetzen == "e" or fortsetzen == "E":
                print("Auf Wiedersehen")
                print()
                break
    except ValueError:
        print(input("Wähle (\033[1;33mm\033[0m), um ins Hauptmenü zu gelangen\nund (\033[1;31me\033[0m), um das Programm zu beenden. (\033[1;33mM\033[0m/\033[1;31me\033[0m) \t\t>>> :   "))

############################################################################################################

    print("#################################################################")
    print("#\t\t\t\t\t\t\t\t#")
    print("#\tWelches Programm soll ausgeführt werden?\t\t#")
    print("#\t\t\t\t\t\t\t\t#")
    print("#\t(\033[1;33m1\033[0m) Rückgeldberechnung? --> gib \"\033[1;33m1\033[0m\" ein.\t\t#")
    print("#\t(\033[1;33m2\033[0m) Rabattberechnung?   --> gib \"\033[1;33m2\033[0m\" ein.\t\t#")
    print("#\t(\033[1;33m3\033[0m) Benzinrechner?      --> gib \"\033[1;33m3\033[0m\" ein.\t\t#")
    print("#\t(\033[1;31m4\033[0m) Beenden             --> gib \"\033[1;31m4\033[0m\" ein.\t\t#")
    print("#\t\t\t\t\t\t\t\t#")
    print("#################################################################")

    while True:
        try:
            print()
            programmauswahl = int(input("Wähle Programm \033[1;33m1\033[0m, \033[1;33m2\033[0m, \033[1;33m3\033[0m oder \033[1;31m4\033[0m zum Beenden. \t\t>>> :   "))
            if programmauswahl == 1 or programmauswahl == 2 or programmauswahl == 3 or programmauswahl == 4:
                print()
                print(f"Option {programmauswahl} wurde gewählt:")
                if programmauswahl == 1:
                    print(">>> \033[4;33mRückgeldberechnung\033[0m <<<")
                elif programmauswahl == 2:
                    print(">>> \033[4;33mRabattberechnung\033[0m <<<")
                elif programmauswahl == 3:
                    print(">>> \033[4;33mBenzinrechner\033[0m <<<")
                print()
                break
            else:
                print()
                print("Gib die Zahl:\n\t\t\033[1;33m1\033[0m (für Rückgeldberechnung)\n\t\t\033[1;33m2\033[0m (für Rabattberechnung) oder \n\t\t\033[1;33m3\033[0m (für Benzinrechner) \n\t\t\033[1;31m4\033[0m (zum Beenden) \n\tein!")
                print()
        except ValueError:
            print()
            print("Gib die \033[1;31mZahl\033[0m:\n\t\t\033[1;33m1\033[0m (für Rückgeldberechnung)\n\t\t\033[1;33m2\033[0m (für Rabattberechnung) oder \n\t\t\033[1;33m3\033[0m (für Benzinrechner) \n\t\t\033[1;31m4\033[0m (zum Beenden) \n\tein!")
            print()

    if programmauswahl == 1:
        rückgeld()
        schleifencounter = 1
    elif programmauswahl == 2:
        rabattrechner()
        schleifencounter = 1
    elif programmauswahl == 3:
        benzinrechner()
        schleifencounter = 1
    else:
        print("Auf Wiedersehen.")
        print()
        break

print("\033[?1049l")