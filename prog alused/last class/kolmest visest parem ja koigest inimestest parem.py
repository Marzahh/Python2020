# Ülesanne 1 Odaviske võistlus
# Programmi töö aluseks on andmed odaviske võistluse tulemuste kohta. Selleks on sportlase nimi ja kolme viske tulemused. 
# Andmed on nö lihtsustatud, ehk parim vise tuleb leida kolme viske hulgast.
# Leida võitja.
# 
# Andmed on tekstifailis nimega oda_uus.txt.


fm=open("oda_uus.txt", "r", encoding = "ISO-8859-1")
voistlejad = list()
tulemused = list()
for rida in fm:
    andmed = rida.split()
    voistlejad.append(andmed[1] + " " + andmed[0])
    vise1 = float(andmed[2])
    vise2 = float(andmed[3])
    vise3 = float(andmed[4])
    pikim_vise = vise1
    if vise2 > pikim_vise:
        pikim_vise = vise2
    if vise3 > pikim_vise:
        pikim_vise = vise3
    tulemused.append(pikim_vise)
fm.close()
#print(voistlejad)
#print(tulemused)

mitu = len(tulemused)
voitja_tulemus = 0
for i in range(mitu):
    if tulemused[i] > voitja_tulemus:
        voitja_tulemus = tulemused[i]
        voitja_nimi = voistlejad[i]
print("VÃµistluse vÃµitis",voitja_nimi,"tulemusega",voitja_tulemus)
