# #Leida paariskuupäevade keskmine temperatuur. Trükkida ekraanile leitud keskmine ja paaritud kuupäevad, mil temperatuur oli leitud keskmisest väiksem. Kui sellised kuupäevad puuduvad, väljastada sobiv teade. 

teste = int(input("Testide arv? "))
for i in range(teste):
    kuupäevad = list()
    temperatuurid = list()
    fm_s = open("kt_2.txt","r")
    mitu = fm_s.readline()
    for rida in fm_s:
        kuupäev,temperatuur = rida.split(" ")
        kuupäevad.append(int(kuupäev))
        temperatuurid.append(int(temperatuur))
    fm_s.close()
    summa_paeva=0
    paeva_summa_madalam=0
    
    mitu_paeva_kokku=len(kuupäevad)
  

    for i in range(mitu_paeva_kokku):
        if kuupäevad[i] % 2 ==0:
            summa_paeva = summa_paeva + temperatuurid[i]
    
    kesk_temp=round(summa_paeva/mitu_paeva_kokku)
    print("Paaris kupäevade temperatuuride keskmine on ", kesk_temp)
    
    
    for i in range(mitu_paeva_kokku):
        if kuupäevad[i] % 2 !=0:
            if temperatuurid[i] < kesk_temp:
                paeva_summa_madalam = paeva_summa_madalam + 1
                print("Antud kuupäeval: ",kuupäevad[i], " oli selline temperatuur ",temperatuurid[i])
    if paeva_summa_madalam == 0:
        print("Paaritu päevi mis olnud paaris päevade keskmisest vähem ei olnud")
    
    print("Paariskuupäevade temperatuuride keskmine on ", kesk_temp, " ja ",paeva_summa_madalam," paaritu päeval oli temperatur madalam paaris päevade keskmisest")