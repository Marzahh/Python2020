teste = int(input("Testide arv? "))
x = int(input("sisesta kui paplju vähem või rohkem võib olla arv "))


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
    
    mitu_paeva_kokku=len(kuupäevad)

    for i in range(mitu_paeva_kokku):
        summa_paeva = summa_paeva + temperatuurid[i]
    
    kesk_temp=round(summa_paeva/mitu_paeva_kokku)
    print("Temperatuuride keskmine on ", kesk_temp)
    
    a=kesk_temp-x
    b=kesk_temp+x
    kesk_temp_wide = range(a,b,1)
    kesk_temp_wide_list = list(kesk_temp_wide)
    print (kesk_temp_wide_list)
    
    for i in range(mitu_paeva_kokku):
        if temperatuurid[i] in kesk_temp_wide_list:
            print("Antud kuupäeval: ",kuupäevad[i], " oli selline temperatuur ",temperatuurid[i] )
            kuupaeva_summa = kuupaeva_summa + 1
    print("Oli nii palju paevi mis olnud listi sees ", kuupaeva_summa)
    
    
