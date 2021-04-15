#Ülesanne 2
#Loe ülesanne lõpuni, et teada saada, millised on algandmed ja mida küsitakse ;)
#Gümnaasiumi lõpetanud soovivad astuda TLÜsse informaatika erialale. Sissesaamisel kehtib lävend.
#Vastu võetakse kõik kandidaadid, kelle eksamitelt saadud punktisumma (nn vastuvõtupall) ületab lävendi.
#Vastuvõtupall arvutatakse eesti keele riigieksami tulemuse ning vastuvõtueksami 
#punktide põhjal. Riigieksam annab vastuvõtupalli 25% ning vastuvõtueksam 75%. 
#Vastuvõtueksam koosneb omakorda kahest osast - testist ja vestlusest, mis mõlemad on võrdse kaaluga (50/50).
#Algandmetena on teada eesti keele riigieksami (maks 100) ja vastuvõtutesti (maks 50) tulemused ning lävendi suurus.
#Kui palju peab üliõpilaskandidaat saama vestlusel punkte (maks 50), et lävend ületatud saaks?
import math
EstEks = int(input("Sisesta Eesti keele eksami punktid"))
IQEks = int(input("Sisesta IQ eksami punktid"))
Est2 = EstEks * 0.25
IQ2 = IQEks * 37.5 / 50
Vestlus1 = ((65 - (IQ2 + Est2)) * 100) / 37.5
V2 = Vestlus1 * 50 / 100
print("Üliõppilaskandidaat peab saama vestlusel minimum", V2, "punkte, et ületada lävendi" )