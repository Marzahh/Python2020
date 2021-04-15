from random import randint

arvud=list()
N=101
loendur= N * [0]
#arv = randint(1, 1000)
loend=0

for i in range(1000):
    arv = randint(0, N-1)
    arvud.append(arv)
    
for i in range(1000):
    loendur[arvud[i]] = loendur[arvud[i]] +1


for i in range(N):
    print(i,"-",loendur[i])
    
    
    

   
    
     
    