#Ülesanne nr. 1
#Sisesta arv ja kontrolli, kas on tegemist paarisarvu või paaritu arvuga.
#Kuidas kontrollida, kas arv on paaris või paaritu?
arv = int(input("Sisesta arv"))

if arv%2 == 0:
    print("paaris")
else:
    print("paaritu")
