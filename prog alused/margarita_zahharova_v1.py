# Variant 1 . Margarita Zahharova
taisarvunumber = int(input("Sisesta mittu täisarvu soovid sisestada "))
summa=0
arvukord =0

for arv in range(taisarvunumber):
    x = int(input("Sisesta täisarv "));
    if x%2 == 0:
        print(x, "on paaris arv")
        summa=summa+x
        
print("Paarisarvude summa on", summa)

print("Aitäh kontrollimise eest! :)")
    
