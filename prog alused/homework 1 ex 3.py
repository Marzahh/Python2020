#Ülesanne 3 Jalgrattur on oma kodust 5 km kaugusel ja liigub maja suunas kiirusega 15 km/h. Kui jalgrattur sõitmist alustab,
#stardib tema otsaesiselt kärbes lennates kiirusega 40 km/h maja suunas. Jõudnud majani pöörab ta kiirust kaotamata ümber 
#ja lendab tagasi. Jõudnud jalgratturini, pöördub ta taas ringi ja nii pendeldab õnnetu pea kaotanud kärbes ühtlase kiirusega 
#edasi-tagasi seni kuni ta maja ja ratturi otsaesise vahel oma kurva lõpu leiab. 
#Jalgratturi edasisest saatusest ajalugu vaikib. 
#Küsimus: kui pika tee läbis kärbes enne oma õnnetut lõppu. 
#NB! Lahendus peab olema universaalne, mis lubab sisestada toodud suuruste kõrval ka teistsuguseid andmeid.
import math
KärbesSpeed = int(input("Sisesta Kärbese kiirus"))
JalgratturiSpeed = int(input("Sisesta Jalgratturi kiirus"))
DistanceHome = int(input("Sisesta Kodu kaugus"))
SpeedTogether = KärbesSpeed + JalgratturiSpeed
DistanceLeftBeforeTheyMeet = DistanceHome - ((DistanceHome * 60 / KärbesSpeed) * JalgratturiSpeed / 60)
DistanceLeftInKMForK = DistanceLeftBeforeTheyMeet / SpeedTogether * KärbesSpeed
DistanceThatKärbesFlew = DistanceLeftInKMForK + DistanceHome
print("Kärbes läbis", DistanceThatKärbesFlew, "KM enne oma õnnetut lõppu" )