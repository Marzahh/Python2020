nimed = list()
aasta = list()
sood = list()
kaal = list()
pikkused = list()
p2kapikkude_keha_massi_indeks = list()
pikkus_meetritest = list()


luhim_p2kapoiss = 200
p2kapikkude_summa = 0


#Faili lugemine ja listideks jagamine
fail = open('p2kapikud6.txt', "r")

for rida in fail:
    rida = rida.strip()
    eesn,sugu,aast,kg,pik = rida.split()
    nimed.append(eesn)
    sood.append(sugu)
    aasta.append(int(aast))
    kaal.append(float(kg))
    pikkused.append(int(pik))
fail.close()

p2kapikku_kokku = len(nimed)

#Päkapikkude kehamassi indeksi leidmine ja tabeli printimine
for i in range(p2kapikku_kokku):
    pikkus_meetritest.append(pikkused[i]/100)
 
 
print("P2kapikku nimi","Kaal","Kehamassiindeks","Kommentaar")
print("-----------------------------------------------------")

for i in range(p2kapikku_kokku):
    p2kapikkude_keha_massi_indeks.append(kaal[i]/(pikkus_meetritest[i] * pikkus_meetritest[i] ))
    if p2kapikkude_keha_massi_indeks[i] > 30:
        print( nimed[i],kaal[i],round(p2kapikkude_keha_massi_indeks[i]),"Antud kehamassiindeksiga soovitame minna jõusaali! :)")
    if p2kapikkude_keha_massi_indeks[i] < 15:
        print(nimed[i],kaal[i],round(p2kapikkude_keha_massi_indeks[i]),"Soovitame süüa rohkem piparkooge!")
    if p2kapikkude_keha_massi_indeks[i] >18 and p2kapikkude_keha_massi_indeks[i]<= 25  :
        print(nimed[i],kaal[i],round(p2kapikkude_keha_massi_indeks[i]),"Olete surepärases vormis!:)")
print()



#Kõige lühimate päkapoisse leidmine ja väljasamine      
for i in range(p2kapikku_kokku):
    if sood[i] == "p":
        if luhim_p2kapoiss > pikkused[i]:
           luhim_p2kapoiss = pikkused[i]
    
for i in range(p2kapikku_kokku):
    if sood[i] == "p":
        if luhim_p2kapoiss == pikkused[i]:
           print("Kõige lühemad(m) päkapoissid on ", nimed[i], " pikkusega ",luhim_p2kapoiss, " cm." )
print()
        
         
#Kokku lugemineja väljastamine kõike päkapikke kes ei erine lühemast x cm
cm_erinevus_luhemast_p2kapoisist = int(input("Palun sisestage kui palju cm erinevus lühimast päkkapoisist Teid huvitab : "))          
print()

uus_maks_pikkus= luhim_p2kapoiss+cm_erinevus_luhemast_p2kapoisist
uus_min_pikkus= luhim_p2kapoiss-cm_erinevus_luhemast_p2kapoisist

luhimad_p2kapikkud_pikkused = range(uus_min_pikkus,uus_maks_pikkus+1)
luhimad_p2kapikkud_pikkused_list = list(luhimad_p2kapikkud_pikkused)

#print (luhimad_p2kapikkud_list)          
                
           
for i in range(p2kapikku_kokku):
    if pikkused[i] in luhimad_p2kapikkud_pikkused_list:
        p2kapikkude_summa = p2kapikkude_summa + 1
print("Meil on nii palju päkapikke: ", p2kapikkude_summa, ", kelle pikkus ei erine lühemast päkapoissist(",luhim_p2kapoiss,") rohkem kui ",cm_erinevus_luhemast_p2kapoisist,"cm!"  )
print()
print("See on lõpp! Aitäh antud töö kontrollimise ja huvitava aine(semestri) eest! :)")







