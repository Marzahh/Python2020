summa = 0
keskmine = 0
pikkused = list()
nimed = []
mittukorda = int(input("sisesta mittu inimest tuleb"))


for i in range(mittukorda):
    nimi = input("Nimi ")
    nimed.append(nimi)
    pikkus = int(input("Pikkus "))
    pikkused.append(pikkus)
print(nimed)
print(pikkused)




summa = 0

for i in range(mittukorda):
    summa = summa + pikkus

print(summa)

keskmine = summa/mittukorda

print("keskmine on ", keskmine)

loendur = 0

for i in range(mittukorda):
    if pikkused[i] < keskmine:
        loendur= loendur+1
        print(nimed[i], pikkused[i])
        
        
print(loendur, " arvu on väiksem kui keskmine ", keskmine)       
        
        
pikim=0
for i in range(mittukorda):
    if pikkused[i] > pikim:
        pikim = pikkused[i]
        pikima_nimi = nimed[i]
        
print("Pikkema nimi on ", pikima_nimi, "ja tema pikkus on", pikim)
        
luhikesem=0
for i in range(mittukorda):
    if pikkused[i] > luhikesem:
        luhikesem = pikkused[i]
        luhikesema_nimi = nimed[i]
print("Lühema nimi on ", luhikesema_nimi, "ja tema pikkus on", luhikesem)
    

    

