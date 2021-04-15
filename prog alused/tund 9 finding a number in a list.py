arvud = [1,2,4,6,7,8,9,12,14,15,16,18,19,20]
mitu = len(arvud)
algus=0
lõpp = mitu-1
otsitav = 3
for i in range(10):
    keskmine = (algus+lõpp+1)//2
    
    if arvud[keskmine] > otsitav:
        lõpp= keskmine-1
        
    elif arvud[keskmine] < otsitav:
        algus = keskmine+1
    else:
        print("Leitud!")
