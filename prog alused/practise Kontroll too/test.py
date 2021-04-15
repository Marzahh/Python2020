a=[]
a=[1,2,3,-1,-2,-3]
mitu =len(a)

    
neg = 0
for i in range(mitu):
    if a[i] < 0:
        neg = neg + 1
        
if neg == 0:
    print("Kõik numbrid on positiivsed")
else:
    print("Kõik numbrid ei ole positiivsed")
  