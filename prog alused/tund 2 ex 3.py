#Ostad kaupa N euro eest.
#Vastavalt Sinu poolt makstud rahale tuleb Sulle raha tagasi anda.
#Milliseid rahatähti ja kui palju tuleks tagastada?
Hind = int(input("Sisesta kauba hind"))
Rahaantud = int(input("Sisesta antud summa"))

Rahatagastuda = Rahaantud - Hind

viiesajaline = Rahatagastuda//500
if viiesajaline > 0:
    print(viisajaline, "viiesajalist")
    
kahesajaline = Rahatagastuda%500
kahesajalinetäis = kahesajaline//200
if kahesajalinetäis  >0:
    print(kahesajalinetäis, "kahesajalist")
    
sajaline = kahesajaline%200
sajalinetäis = sajaline//100
if sajalinetäis  >0:
    print(sajalinetäis, "sajalist")
    
viiekümneline = sajaline%100
viiekümnelinetäis = viiekümneline//50
if viiekümnelinetäis  >0:
    print(viiekümnelinetäis, "viiekümnelist")
    
kahekümneline = viiekümneline%50
kahekümnelinetäis = kahekümneline//20
if kahekümnelinetäis  >0:
    print(kahekümnelinetäis, "kahekümnelist")
    
ühekümneline = kahekümneline%20
ühekümnelinetäis = ühekümneline//10
if ühekümnelinetäis  >0:
    print(ühekümnelinetäis, "kümnelist")
    
viieline = ühekümneline%10
viielinetäis = viieline//5
if viielinetäis  >0:
    print(viielinetäis, "viielist")
    
kaheline = viieline%5
kahelinetäis = kaheline//2
if kahelinetäis  >0:
    print(kahelinetäis, "kahelist")
    
üheline = kaheline%2
ühelinetäis = üheline//1
if ühelinetäis  >0:
    print(ühelinetäis, "ühelist")
    
print ("DONE!")
    


