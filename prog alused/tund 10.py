import math
def Lõigupikkus(x1,y1,x2,y2):
    kaugus_ruut = (x1-x2)**2 + (y1-y2)**2
    raad = math.sqrt(kaugus_ruut)
    return raad



def Ringipindala(raad):
    raadiusruudus = raad**2
    tulemusP = raadiusruudus * 3.14
    return tulemusP
    
xk = input("Sisesta xk ")
yk = input("Sisesta yk ")
xj = input("Sisesta xj ")
yj = input("Sisesta yj ")

#raadiuse leidmine
raadius = Lõigupikkus(xk,yk,xj,yj)
print = ("Radius on ", raadius)


#ringi pindala leidmine
pindala = Ringipindala(raadius)
print = ("Pindala on ", pindala)

#tulemuse trükkimine