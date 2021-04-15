#Leida ja trükkida ekraanile kõik temperatuurid ja vastavad kuupäevad, kui temperatuur ei olnud maksimaalsest temperatuurist madalam rohkem kui x kraadi. Selle x-i peab saama sisestada kasutaja.
teste = int(input("Testide arv? "))
x = int(input("sisesta kui paplju vähem võib olla maximumist temperatuur "))


import string
for i in range(teste):
    kuupäevad = list()
    temperatuurid = list()
    fm = open("kt_2.txt","r")
    mitu = fm.readline()
    for rida in fm:
        kuupäev,temperatuur = rida.split(" ")
        kuupäevad.append(int(kuupäev))
        temperatuurid.append(int(temperatuur))
    fm.close()
    summa_paeva=0
    paeva_summa_madalam=0
    kuupaeva_summa=0
    koige_korgem=-100
    mitu_paeva_kokku=len(kuupäevad)

    for i in range(mitu_paeva_kokku):
        if temperatuurid[i] > koige_korgem:
            koige_korgem = temperatuurid[i]
            
    print(koige_korgem)         
    a=koige_korgem-x+1
    b=koige_korgem+1
    kesk_temp_wide = range(a,b,1)
    kesk_temp_wide_list = list(kesk_temp_wide)
    print (kesk_temp_wide_list)          
                
                
                
#         if temperatuurid[i] == -2: # I still neeed to put koige_korgem instead of -2
#             print(kuupäevad[i])
    

    
    for i in range(mitu_paeva_kokku):
        if temperatuurid[i] in kesk_temp_wide_list:
            print("Antud kuupäeval: ",kuupäevad[i], " oli selline temperatuur ",temperatuurid[i] )
            kuupaeva_summa = kuupaeva_summa + 1
    print("Oli nii palju paevi mis olnud listi sees ", kuupaeva_summa)
    
    
