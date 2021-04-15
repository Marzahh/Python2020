# # Tekstifailis haridus.txt on andmed rahvastiku hariduse kohta erinevates linnades ja valdades. Ühes reas on valla 
# või linna nimi, üksuse liik, kõrghardusega meeste arv, meeste koguarv, kõrghardusega naiste arv ja naiste koguarv 
# (positiivsed täisarvud). Võib eeldada, et fail vastab kirjeldusele. 
# Leida omavalitsus, kus on suurim kõrgharidusega meeste protsent meeste koguarvust. Trükkida välja omavalitsuse nimi, 
# liik ja protsent. 
# Loendada, mitmes linnas on kõrghariduseta naisi rohkem kui mehi.
# Trükkida tabel nende omavalitsusüksuste andmetega (nimi, liik, kõrgharidusega inimeste arv), kus kõrgharidusega 
# inimeste arv on suurem mingist etteantud suurusest. Viimase sisestab kasutaja. Kui selliseid omavalitsusi ei ole, 
# anda sobilik teade.


#Andmete sisselugemine
nimed = []
liigid = []
k6rgh_mehed= []
mehed = []
k6rgh_naised = []
naised = []
fm = open("haridus.txt","r")
for rida in fm:
    rida = rida.strip()
    andmed = rida.split()
    nimed.append(andmed[0])
    liigid.append(andmed[1])
    k6rgh_mehed.append(int(andmed[2]))
    mehed.append(int(andmed[3]))
    k6rgh_naised.append(int(andmed[4]))
    naised.append(int(andmed[5]))
fm.close()

mitu = len(k6rgh_mehed)

#Suurima kÃµrgharidusega meeste osakaaluga omavalitsuse leidmine
maks = 0
for i in range(mitu):
    k6rgh_meeste_protsent = k6rgh_mehed[i] / mehed[i] * 100
    if maks < k6rgh_meeste_protsent:
        maks = k6rgh_meeste_protsent
        maks_koht = nimed[i] + " " + liigid[i]
print("KÃµrgeima kÃµrgharidusega meeste osakaaluga on",maks_koht, round(maks,2),"%.")
print()

#Linnade loendamine, kus on kÃµrghariduseta naisi rohkem kui mehi
naisi_rohkem = 0
for i in range(mitu):
    if liigid[i] == "linn" and mehed[i]-k6rgh_mehed[i]<naised[i]-k6rgh_naised[i]:
        naisi_rohkem = naisi_rohkem + 1
print("KÃµrghariduseta naisi oli rohkem kui mehi",naisi_rohkem,"linnas.")
print()


#Tabeli trÃ¼kkimine omavalitsustest, kus on kÃµrgharidusega inimesi rohkem kui kasutaja sisestatud piir.
kogus = int(input("Kui palju peab vÃ¤hemalt olema kÃµrgharidusega inimesi, et linn vÃµi vald tabelisse kanda "))
leitud = 0
print("%-15s %-10s %10s" % ("nimi","liik","kÃµrgharidusega"))
for i in range(mitu):
    if k6rgh_mehed[i] + k6rgh_naised[i] > kogus:
        leitud = 1
        print("%-15s %-10s %10d" % (nimed[i],liigid[i],k6rgh_mehed[i] + k6rgh_naised[i]))
if leitud == 0:
    print("Tingimustele vastavaid omavalitsusÃ¼ksusi ei leitud.")

print()
print("LÃµpp hea, kÃµik hea ;)")
