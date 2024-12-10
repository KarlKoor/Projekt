import random
# funktsioon mis valib suvaka sõna sõnade valikust
def suvasõnad():
    sõnad = ["arvuti", "margus", "programmeerimine", "püüton", "voco", "nuub", "kooder", "lahendus", "suvakas", "maitea"]  # Sõnad
    return random.choice(sõnad)  # suva sõna
# funktsioon mis näitab praeguse sõna, tähed
def näita_tähti_sõnu(sõna, arvatud_tähed):
    näita = ""  # muutuja kuhu salvestatakse sõna
    for tähed in sõna:
        if tähed in arvatud_tähed:  # kui täht on õige siis näidatakse seda
            näita += tähed
        else:
            näita += "_"  # kui paned valesti tuleb alakriips
    return näita
# mängu funktsioon
def hangman():
    sõna = suvasõnad()  # suvakas sõna
    arvatud_tähed = []  # arvatud tähed
    elud = 8  # elud    
    print("Tervetuloa Hangman-i mängu!")    
    # tsükkel mis läheb tööle kui on veel elusi
    while elud > 0:
        print("\nSõna: ", näita_tähti_sõnu(sõna, arvatud_tähed))  # praegu arvatud tähed, sõna
        print("Arvatud tähed: ", arvatud_tähed)  # kõik arvatud tähed
        print(f"elusi alles: {elud}")  # elud       
        # kirjuta täht ja kõik tähed lähevad autom. väikseks
        arva = input("Sisesta üks täht: ").lower()        
        # Kontrollin kas sisestatud täht on üks täht ja kas see on tähestikus või on nr
        if len(arva) != 1 or not arva.isalpha():
            if len(arva) > 1:
                #teeme võrdluse kogu sõnaga et kui arvad et tead tervet sõna siis saad terve sõna ära arvata
                if arva == sõna:
                    print("Arvasid ära kogu sõna")
                    return                 
        # siis kui oled juba seda tähte kasutanud
        if arva in arvatud_tähed:
            print("Oled juba seda tähte kasutanud")
            continue        
        arvatud_tähed.append(arva)  # Arvatud täht läheb mällu        
        # paned vale tähe kaotad elu
        if arva not in sõna:
            elud -= 1
            print(f"Vale täht, elusid veel: {elud}")        
        # kõik tähed arvatud siis mäng läbi
        if all(tähed in arvatud_tähed for tähed in sõna):
            print(f"Naiss arvasid ära sõna oli: '{sõna}'")
            break
    else:
        # kui kaotad näed mis sõna oli
        print(f"Ürita uuesti, muide õige sõna oli: '{sõna}'")
hangman()