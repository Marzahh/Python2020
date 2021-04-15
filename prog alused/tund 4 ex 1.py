# Ülesanne 1 Loendamine
# Andmeteks on üliõpilaste kontrolltöö punktid ja töö maksimaalsed punktid (kõigil ühesugune).
# Hindamisel kehtivad protsentides väljendatud piirid (A - 91%-100%, B81%-90% jne). Loendada, mitu õpilast 
# said töö eest hindeks B.
# Punktid sisestab kasutaja ja peale iga sisestust küsib programm, kas on veel töid jäänud.
# Lahendust saab laiendada järgmiselt:
# 1) loendatakse kõigi hinnete esinemine, lõpuks tehakse kokkuvõte erinevate hinnete esinemisest.
# 2) teatatakse iga töö kohta hinne

maxpunktid = int(input("sisesta max punktid"))
HinneB = 0



vastus = "j"
while vastus == "j":

    ktpunktid = int(input("sisesta KT punktid"))
    protsent = 100*ktpunktid/maxpunktid

    if protsent >= 91 and protsent <= 100:
        print("Hind A")
        
    elif protsent >= 81 and protsent <= 90:
        print("Hind B")
        HinneB = HinneB+1
        print("Hinne B said", HinneB, "õpilast")
        
    elif protsent >= 71 and protsent <= 80:
        print("Hind C")
        
    elif protsent >= 61 and protsent <= 70:
        print("Hind D")
        
    elif protsent >= 51 and protsent <= 60:
        print("Hind E")
        
    elif protsent < 50:
        print("Not Passed")
        
    vastus = input("Kas veel [j/e]?")
