#Ülesanne 1 Summeerime
# Leia summa arvudele mingist etteantud vahemikust. Kasutaja sisestab vahemiku
# alguse ja lõpu. Programm annab vastuseks soovitud vahemikku jäävate arvude summa.
# Sisuliselt tegime selle ülesande läbi eelmisel nädalal while-tsükliga. Nüüd on kord for-tsükli käes.

rangestart = int(input("Sisesta vahemiku alguse "))
rangeend = int(input("Sisesta vahemiku lõppu "))
summa=0
for arv in range(rangestart, (rangeend+1)):
    summa = summa+arv

print("arvude summa on", summa)

