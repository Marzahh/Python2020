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
    summa_paeva_neg=0
    paeva_summa_madalam=0
    
    mitu_paeva_kokku=len(kuupäevad)
  

    for i in range(mitu_paeva_kokku):
        if temperatuurid[i] < 0:
            summa_paeva_neg = summa_paeva_neg + temperatuurid[i]
    
    kesk_temp=round(summa_paeva_neg/mitu_paeva_kokku)
    print("Negatiivse emperatuuride keskmine on ", kesk_temp)
    
    
    neg = 0
    for i in range(mitu_paeva_kokku):
        if temperatuurid[i] < 0:
            neg = neg + 1
            
    if neg == 0:
        print("Kõik numbrid on positiivsed")
    else:
        print("Kõik numbrid ei ole positiivsed")
