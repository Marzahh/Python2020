kordajad1 = (1,2,3,4,5,6,7,8,9,1)
kordajad2 = (3,4,5,6,7,8,9,1,2,3)
kuud = ("jaanuar","feb","march","april","mai","juuni","jul","aug","sept","okt","nov","dets")
ik = "49603112748"
kuu = int(ik[3:5])
print(kuud[kuu-1])
summa = 0

for i in range(10):
    summa = summa + int(ik[i])* kordajad1[i]
    
jagatud11summa = summa%11

if jagatud11summa != 10:
     print("Kontroll number  ei ole 10 ja on õige 1 kord")

elif jagatud11summa == 10:
    summa = 0
    for i in range (10):
          summa = summa + int(ik[i])* kordajad2[i]
    
    jagatudsummajääk = summa%11

    if jagatudsumma != 10:
         print("Kontroll number on õige teine kord")
         print(jagatudsummajääk)
    elif jagatudsumma == 10:
        print("Kontrollinumber on 0")
        print(jagatudsummajääk)

    
    


# jagatud11summa = summa%11
# if jagatud11summa == 1 and ik[10:11]:
#     print("Kontroll number on 1 ja õige")
#     
# else print("vale")
#     
# print(summa)
# print(jagatud11summa)
#     
    
    
# print(i, ik[i], kordajad1[i])
