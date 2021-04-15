rangestart = int(input("Sisesta vahemiku alguse "))
rangeend = int(input("Sisesta vahemiku lõppu "))

inimeseguess = 0
while inimeseguess != arvutiarv:
    arvutiarv = randint(1,10)
    inimeseguess = int(input("insert your number guess "))
    if arvutiarv == inimeseguess:
        print("Õige!")
    if arvutiarv > inimeseguess:
        print("arvuti arv on suurem!")
    if arvutiarv < inimeseguess:
        print("arvuti arv on väiksem!")


