ridu = int(input("Mitu rida? "))
veerge = int(input("Mitu veergu? "))


arvud = list()
for r in range(ridu):
    rida = list()
    print("Sisestame",r+1,"rida...")
    for v in range(veerge):
        arv = int(input("Sisesta arv"))
        rida.append(arv)
    arvud.append(rida)
    print(arvud)

# Reasummade leidmine kasutades listi indekseid.
summad = list()
for r in range(ridu):
    summa = 0
    for v in range(veerge):
        summa = summa + arvud[r][v]
    summad.append(summa)
print(summad)

# Veerusummade leidmine - see tuleb ise lisada
summadveerud = list()
for v in range(veerge):
    summaveerud = 0
    for r in range(ridu):
        summaveerud = summaveerud + arvud[v][r]
    summadveerud.append(summaveerud)
print(summadveerud)
# Pea- ja kÃµrvaldiagonaali summade leidmine - ka see tuleb ise lisada

# Maagilisuse kontroll: kui kÃµik summad vÃµrduvad esimese summaga, on nad ka omavahel jÃ¤relikult vÃµrdsed.
on_maagiline_read = True
for r in range(len(summad)):
    if summad[0] != summad[r]:
        on_maagiline_read = False
        
on_maagiline_veerud = True
for v in range(len(summadveerud)):
    if summadveerud[0] != summadveerud[v]:
        on_maagiline_veerud = False

on_maagiline_diagonaal = True
for i in range(len(summadveerud)):
    if veerge[i] != arvud[i] and :
        on_maagiline_diagonaal = False

#Vastuse vÃ¤ljastamine
if on_maagiline_veerud and on_maagiline_read and on_maagiline_diagonaal:        # kontrolli kujul if on_maagiline == True: ei peeta heaks stiiliks.
    print("On maagiline ruut.")
else:
    print("Ei ole maagiline ruut.")