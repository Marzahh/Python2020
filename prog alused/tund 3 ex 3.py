# Ülesanne 3. Õnnelik seitse
# Kui suur on lootus võita mõnes õnnemängus? Selleks võib välja arvutada tõenäosuseid, aga võib ka mängu käiku simuleerida. 
# 
# Mängija veeretab kahte täringut. Kui täringutel olevate silmade summa on 7, võidab mängija näiteks 4 eurot. Kui ei ole, siis kaotab näiteks 1 eurot. Need summad võiksid olla kergesti muudetavad.
# Mängu alguses on vaja teada, kui palju raha mängu pannakse. Seejärel hakatakse veeretama ja vastavalt rahahulka suurendama või vähendama. Mäng lõppeb siis, kui raha on otsas.
# Veeretada aitab juhuslike arvude generaator. Lisaks on vaja programmi lõpus teatada, kui palju kordi jõuti täringuid veeretada ja kui suur oli vahepeal kõige suurem summa.
import random
panus = int(input("sisesta panus"))
Score7 = 0
Fail = 0
while panus > 0:
    vise1 = random.randint(1,6)
    vise2 = random.randint(1,6)
    if vise1+vise2==7:
        Score7 = Score7+1
        print("You wone",Score7, "time")
        panus=panus+4
    else:
        Fail = Fail+1
        print("You lost",Fail, "time")
        panus=panus-1
print("No more money left!")


