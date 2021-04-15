# Listi sorteerimine valik-meetodil (selection sort)
# Listi pikkuse mÃ¤Ã¤rab kasutaja

import random
mitu = int(input("Mitu arvu teeme? "))
arvud = list()
for i in range(mitu):
    arvud.append(random.randint(1,100))
print("Algne massiiv:")
print(arvud)

# Miinimumi leidmisel peetakse meeles vaid indeks, kus miinimum asub. Loomulikult vÃµib lisaks teise muutujasse omistada arvu enda,
# et seda siis vÃµrdlemisel kasutada.
for i in range(mitu-1):
    min_i = i
    for j in range(i, mitu):
        if arvud[j] < arvud[min_i]:
            min_i = j
    temp = arvud[i]
    arvud[i] = arvud[min_i]
    arvud[min_i] = temp
print("Sorteeritud massiiv:")
print(arvud)