# Täisnurkse kolmnurga kohta on teada tema kaatetite pikkused. Leida kolmnurga pindala. 
import math
a = int(input("Sisesta üks kaatet"))   # omistuslause
b = int(input("Sisesta teine kaatet"))
S = a * b / 2
c = math.sqrt(a ** 2 + b ** 2)
P = a + b + c
print("Kolmnurga pindala on", S, "Kolmnurga ümbermõõt on", P)
