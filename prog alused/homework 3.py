# 
# 
# Ülesanne 2 Arvu arvamise mäng
# Üks mängija mõtleb arvu etteantud piirides ja teine katsub seda ära arvata. 
# Meie ülesandes - arvuti mõtleb arvu ja inimene hakkab arvama. Arvuti vastab igale arvamisele 
# ja täpsustab, kas pakutud arv on liiga suur või liiga väike.
# 
# Kuidas arvuti arvu mõtleb? Selleks on juhuslike arvude generaator. Näiteks sobib funktsioon 
# randint(a, b).
# Funktsioon tagastab juhusliku täisarvu vahemikust [a .. b]
# Kasutamise näide: arv = randint(1,10)
# Sel juhul saab arv täisarvulise väärtuse vahemikust [1..10]
# 
# Funktsioon randint() paikneb moodulis random, mis tuleb importida ning funktsiooni käivitamisel kirjutada nime ette random.
# 
# Üldiselt juhuslike arvude "tootmiseks" tuleb generaator kõigepealt algväärtustada, milleks on funktsioon seed(). 
# See peab tagama, et programmi uuel käivitamisel tekiks teistsugune juhuslike arvude jada. Pythonis kaasneb random 
# mooduli importimisega automaatselt seed()-i ühekordne käivitamine.
# 
# Võtame ka teadmiseks, et arvude jada ei saa juhuslikum kui seed()-i iga "arvu tegemise" eel korrata. Pigem vastupidi.
# Järelikult ei ole ka import-lauset õige programmi keskele paigutada. 
# 
# Millal mäng lõpetada?
# a) arv arvatakse ära
# b) kui liiga palju arvatakse (näiteks üle 6 korra), siis programm teatab, 
# et nii rumal ikka olla ei saa, et niiiii kaua seda ühte õnnetut arvu arvata.
# 
# Kui arvuvahemik on 1 .. 100, siis mitme pakkumisega peaks arv kindlasti arvatud saama?
# 
# Kui see tehtud, tuleb terve mäng veel korduma panna - Kas soovid veel mängida? 
# NB! See tähendab uue tsükli lisamist mängutsükli ümber. Ära püüa mängutsüklit kõike tegema
# panna.
import random

from random import randint

playagain = "y"

while playagain == "y":

    a = int(input("From what number guessing  "))
    b = int(input("Untill what number guessing  "))
    maxtry = int(input("Enter max amount of human guesses  "))
    computernumber = randint(a,b)
    numberofguesses = 0
    humanguess = 0

    while humanguess != computernumber and numberofguesses < maxtry:
        humanguess = int(input("insert your number guess "))
        if humanguess == computernumber:
            print ("Correct!")
        if humanguess > computernumber:
            print ("Number is smaller")
        if humanguess < computernumber:
            print ("Number is bigger!")
        
        if humanguess != computernumber:
            numberofguesses = numberofguesses +1
            print("Try number ", numberofguesses)
            
    if numberofguesses >= maxtry:
        print("How can you be so dumb? You exceeded the amount of tryes")
    else:
        print("Good job! That's correct")

    playagain = input("Would you like to play again? y/n  Your answer: ")
    
print("thank you for playing!")




