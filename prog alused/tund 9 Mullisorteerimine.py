import random
arvud = list()
mitu=10
c=0
for i in range(mitu):
    arv = random.randint(1,100)
    arvud.append(arv)
print(arvud)

vahetusi = True
while vahetusi:
    vahetusi = False
    for i in range(mitu-1):
        for i in range(mitu-1):
            if arvud[i] > arvud[i+1]:
                c= arvud[i]
                arvud[i]= arvud[i+1]
                arvud[i+1]=c
                vahetusi = True
                
        
print(arvud)
        
        
    