# Ülesanne 3 Kassiklubi 
# Kassiklubi Felix vajab abiprogrammi oma kiisukeste andmete töötlemiseks. Iga kassi kohta on tekstifailis
# nimi, värvus ja saba pikkus. Viimane on eriti suure tähtsusega ;) Andmed on faili felix.txt
# Kirjuta programm, mis aitab klubi omanikul leida teda huvitavat värvi kasside keskmine sabapikkus. 
# Programm peab laskma kasutajal värvi sisestada ja reageerima ka siis adekvaatselt, kui sellist värvi loomi polegi.
# 


print("Tere! See programm tuvastab lÃ¼hema saba kassi teatud vÃ¤rvi kasside hulgast")
print()

failike=open('felix.txt', 'r', encoding = "ISO-8859-1")
nimed = list()
v2rvid = list()
sabad = list()

for rida in failike:
    nimi, v2rv, pikkus=rida.split()
    nimed.append(nimi)
    v2rvid.append(v2rv)
    sabad.append(int(pikkus))
failike.close()

kasse = len(nimed)

v2rv = input("Mis vÃ¤rvi kasside keskmine ja lÃ¼him sabapikkus sind huvitab? ")
sabasumma = 0
kassiloend = 0
lyhem = 200
for i in range(kasse):
    if v2rv.upper() == v2rvid[i].upper():             # Meetodi upper() kasutamine lubab sisestada segilÃ¤bi suur- ja vÃ¤iketÃ¤hti.
        sabasumma = sabasumma + sabad[i]
        kassiloend = kassiloend + 1
        if sabad[i] < lyhem:
            lyhem = sabad[i]

if lyhem == 200:
    print("Sinu valitud vÃ¤rvi kiisusid meil praegu ei ole.")
else:
    keskmine = sabasumma / kassiloend
    print("KÃ¼situd vÃ¤rvi kasside keskmine sabapikkus on %0.2f." % (keskmine))
    print("VÃ¤ikseimaks sabapikkuseks osutus %0d" % (lyhem))
    print("Need olid:", end=" ")
    for i in range(kasse):
        if v2rv.upper() == v2rvid[i].upper():
            if sabad[i] == lyhem:
                print(nimed[i], end = ' ')
