# Ülesanne 2 Hindamine
# Uudne hindamissüsteem punktide, cm, ja sekundite teisendamisel hinneteks on järgmine: 
# Hinde panemise aluseks ei ole hindaja "absoluutne tõde", vaid hinnatavate õpilaste hulgast
# parim tulemus, mis on 100%. Ülejäänute hinne leitakse protsendi järgi järgmiselt: 
# hinne "5" 91-100%, hinnne "4" 81-90% jne ning läbikukkunud alla 51%.
# Koosta õpetaja tööd lihtsustav programm, mis pakub tulemuste järgi hinde. 
# 
# Failis tulemused_mn.txt on kõrgushüppes saadud tulemused, laste nimed ja sugu (M/N).  
# Trüki välja hinde kolm saanud laste nimed ja tulemused. Loe ka kokku, mitu 3 pandi. 
# Hindamine toimub poiste ja tüdrukute arvestuses oma parima järgi.


#Programm avab tekstifaili, loeb andmed ja esitab hindega neli laste nimed ja tulemused
#Muutujad:
#massiivid: eesnimed, perenimed, sood, tulemused.
#naismaks, tÃ¼drukute maksimum tulemus
#meesmaks, poiste maksimum tulemus
#meesmitu, loendab mitu poissi said hinde kolm
#naismitu, loendab mitu tÃ¼drukut said hinde kolm

naismaks = 0
meesmaks = 0
meesmitu = 0
naismitu = 0
eesnimed = list()
perenimed = list()
sood = list()
tulemused = list()
print("Leian kÃµrgushÃ¼ppe tulemused hindega kolm")

fail = open('tulemused_mn.txt', "r", encoding = "ISO-8859-1")
#Loeb failist ja kirjutab listidesse
for rida in fail:
    rida = rida.strip()
    eesn,pern,tulemus,sugu = rida.split()
    eesnimed.append(eesn)
    perenimed.append(pern)
    sood.append(sugu)
    tulemused.append(int(tulemus))
fail.close()

kokku = len(tulemused)   
#TsÃ¼klis leitakse maksimum vÃ¤Ã¤rtused
for r in range(kokku):
    if sood[r] == "N":
        if naismaks < tulemused[r]:
            naismaks = tulemused[r]
    elif sood[r] == "M":
        if meesmaks < tulemused[r]:
            meesmaks = tulemused[r]         

print("Poisid hindega kolm:")
#TsÃ¼kkel leiab ja prindib poisid hindega kolm
for r in range(kokku):
    if sood[r] == "M" and (meesmaks*0.8) >= tulemused[r] and (meesmaks*0.71) <= tulemused[r]:
        meesmitu += 1
        print(eesnimed[r], perenimed[r], tulemused[r],"cm")

print("Poisse kokku hindega kolm on %d." % (meesmitu))


#TÃ¼drukute osa on sarnane
