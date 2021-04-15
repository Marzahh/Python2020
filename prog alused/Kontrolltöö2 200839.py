#Margarita Zahharova Ül 2
kood = 200839
ÜlesanneVar = (kood%6)+ 1
print(ÜlesanneVar)



teste = int(input("Testide arv? "))

for i in range(teste+1):
    kuupäevad = list()
    temperatuurid = list()
    fm_s = open("kt_2"+str(i)+".txt","r")
    mitu = int(fm_s.readline())
    for rida in fm_s:
        kuupäev,temperatuur = rida.split(" ")
        kuupäevad.append(int(kuupäev))
        temperatuurid.append(int(temperatuur))
    fm_s.close()
    summa_paeva=0
    paeva_summa_madalam=0
    
    mitu_paeva_kokku=len(kuupäevad)
  

    for i in range(mitu_paeva_kokku):
        if kuupäevad[i] %2 == 0:
            summa_paeva = summa_paeva + temperatuurid[i]
    
    kesk_temp=round(summa_paeva/mitu_paeva_kokku)
    print("Paariskuupäevade temperatuuride keskmine on ", kesk_temp)
    
    
    for i in range(mitu):
        if temperatuurid[i] < kesk_temp:
            paeva_summa_madalam = paeva_summa_madalam + 1
    
print("Paariskuupäevade temperatuuride keskmine on ", kesk_temp, " ja ",paeva_summa_madalam," päeval oli temperatuur sellest madalam." )