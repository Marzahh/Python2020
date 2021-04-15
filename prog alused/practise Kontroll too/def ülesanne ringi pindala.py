# LÃµppeesmÃ¤rk on leida ringi pindala, kui ringi kohta on antud kahe punkti koordinaadid:
# keskpunkt ja suvaline punkt joonel.
# Lahendus tuleb teha kahet funktsiooni kasutades - Ã¼ks leiab kahe punkti vahelise kauguse
# ja teine raadiuse jÃ¤rgi ringi pindala.

import math

def RingiPindala(r):
    """Funktsiooni argumendiks on raadius, funktsioon tagastab ringi pindala."""
    pindala = math.pi * r ** 2
    return pindala


def PunktideKaugus(x1,y1,x2,y2):
    """Funktsiooni argumentideks on kahe punkti koordinaadid: esimenes punkti x ja y ning
    teise punkti x ja y.
    Tagastatakse punktide-vaheline kaugus."""
    kaugus = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return kaugus
  
# peaprogramm
x1 = float(input("Ringi keskpunkti koordinaadi x vÃ¤Ã¤rtus: "))
y1 = float(input("Ringi keskpunkti koordinaadi y vÃ¤Ã¤rtus: "))
x2 = float(input("Joonepunkti koordinaadi x vÃ¤Ã¤rtus: "))
y2 = float(input("Joonepunkti koordinaadi y vÃ¤Ã¤rtus: "))
raadius = PunktideKaugus(x1,y1,x2,y2)
print("Ringi raadius on",raadius)
pindala = RingiPindala(raadius)
print("Ringi pindala on",pindala)
