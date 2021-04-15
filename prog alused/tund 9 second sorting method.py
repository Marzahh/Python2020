import random
arvud = list()
mitu=10
c=0
for i in range(mitu):
    arv = random.randint(1,100)
    arvud.append(arv)
print(arvud)

for j in range(mitu-1):
    min_indeks=j
    for i in range(j,mitu):
        if arvud [min_indeks] > arvud[i]:
            min_indeks = i
    print (arvud[min_indeks])
    abi=arvud[min_indeks]
    arvud[min_indeks] = arvud[j]
    arvud[j] = abi
    

 
print(arvud)
