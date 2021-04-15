print("Programm tutvustab, kumb sisestatud arvudest on suruems ja kuvab nad")
arv1 = input("Sisesta esimene arv ")
arv2 = input("Sisesta teine arv ")

if arv1 > arv2:
    print("Esimene arv on suurem. ")
    print("suuruse järjekorras: ", arv2, arv1)
else:
    if arv1 < arv2:
        print("Teine arv on suurem. ")
        print("Suuruse järjekorras ", arv1, arv2)
