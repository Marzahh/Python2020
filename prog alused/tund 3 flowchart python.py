print("Programm tuvastab, kumb sisestatud arvudest on suruems ja kuvab nad suuruse järjekorras.")
arv1 = input(int("Sisesta esimene arv "))
arv2 = input(int("Sisesta teine arv "))

if arv1 > arv2:
    print("Esimene arv on suurem.")
    print("Suuruse järjekorras: ", arv2, arv1)
else:
    if arv1 < arv2:
        print("Teine arv on suurem.")
        print("Suuruse järjekorras ", arv1, arv2)
    else:
        print("Arvud on võrdsed.")