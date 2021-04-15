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
    koige_korgem=-20
    
    mitu_paeva_kokku=len(kuupäevad)
    miinus_kraadid=[]
    top_koige_korgem=[]

    for i in range(mitu_paeva_kokku):
        if temperatuurid[i] < 0:
            miinus_kraadid.append(temperatuurid[i])
            if temperatuurid[i] > koige_korgem:
                koige_korgem = temperatuurid[i]
        if temperatuurid[i] == koige_korgem:
            top_koige_korgem.append(kuupäevad[i])
            
         
    print(miinus_kraadid)
    print(koige_korgem)  
    print(top_koige_korgem)            
    
