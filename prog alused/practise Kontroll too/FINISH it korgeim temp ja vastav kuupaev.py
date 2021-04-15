# The text file kt_2.txt contains the temperatures for one month and the dates when such temperatures occurred. Specifically, each subsequent line contains two integers: date and temperature.
# Find and print the highest temperature on the "below-zero" days and the corresponding date. If there should be more than one day, issue all the dates. If there were no "under-zero" days, issue an appropriate notice.
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
                
        if temperatuurid[i] == -2: # I still neeed to put koige_korgem instead of -2
            print(kuupäevad[i])
                
#     print(koige_korgem) 
#     print(temperatuurid.index(koige_korgem))
#     
#     print(miinus_kraadid)
#     print(koige_korgem)  
#     print(top_koige_korgem)            
    
