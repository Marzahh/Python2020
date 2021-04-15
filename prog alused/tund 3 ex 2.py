#Ülesanne nr 2 Jaguvus
#Sisestatakse 2 arvu. Kontrollitakse, kas suurem arv jagub väiksema arvuga
#ja väljastatakse sellekohane vastus. Programm peab ise aru saama, kumb arv suurem on.
#Kuidas kontrollida jaguvust?

arv1 = int(input("Sisesta arv 1 "))
arv2 = int(input("Sisesta arv 2 "))

if arv1 > arv2:
    if arv1%arv2 == 0:
        print("Arv 1 on suurem ja jagub arv 2")
    else:
        print("Esimene arv ei jagu teise arvuga ja on suurem")

if arv2 > arv1:
    if arv2%arv1 == 0:
        print("Arv 2 on suurem ja jagub arv 1")
    else:
        print("Teine arv ei jagu esimese arvuga ja on suurem")
    


