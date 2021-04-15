import random
panus= int(input("sisesta panus"))
Score7= 0
Fail= 0
suurim=0
while panus>0:
    vise1= random.randint(1,6)
    vise2= random.randint(1,6)
    if vise1+vise2==7:
        Score7 = Score7+1
        panus=panus+4
        print("you wone",Score7,"time")
        if panus > suurim:
            suurim=panus
            print("Current max is", suurim)
            
    else:
        Fail= Fail+1
        panus=panus-1
        print("you lost",Fail,"times")
print("no more money left")
print("sinu max oli", suurim)