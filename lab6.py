import random
import math
import time

zad=4
if zad==1:
   print(f"szczesliwy numerek to : {random.randint(0, 99)}")
   iloscWGrupie=input("podaj ile osub jest w grupie: ")

   # do while
   if iloscWGrupie == "exit" or iloscWGrupie == "0" :
       exit()
   while (not iloscWGrupie.isdigit()):
       iloscWGrupie = input("podaj ile osub jest w grupie: ")
       if iloscWGrupie == "exit" or iloscWGrupie == "0" :
           exit()

   iloscWGrupie=int(iloscWGrupie)
   grupaRoczniki=[""]*iloscWGrupie

   for i in range(iloscWGrupie):
       grupaRoczniki[i]=2000+random.randint(0, 24)
   print(grupaRoczniki)
   print(f"szczęsliwy rocznik to: {grupaRoczniki[random.randint(0,iloscWGrupie-1)]}")

   print("losowanie lotto")
   losy=[""]*49
   for i in range(len(losy)):
       losy[i]=i+1

   print(f"twoje numerki to {random.sample(losy, 6)}")

elif zad == 2:
    #Oblicz: √81, 810, √2 + √3 + √6, √−5, 3√125.
    print(math.sqrt(81))
    print(math.pow(8,10))
    print(math.sqrt(2)+math.sqrt(3)+math.sqrt(6))
    #print(math.sqrt(-5))
    print("error nie może policzyć piewiastka do liczby ujemnej funkcja nie obsługuje liczb urojonych")
    print(math.pow(125, 1.0/3))
elif zad == 3:
    podajCzas=input("Podaj sekundy: ")
    # do while
    if podajCzas == "exit" or podajCzas == "0":
        exit()
    while (not podajCzas.isdigit()):
        podajCzas = input("podaj ile osub jest w grupie: ")
        if podajCzas == "exit" or podajCzas == "0":
            exit()
    czas=int(podajCzas)
    while (czas>0):
        time.sleep(1)
        czas-=1
        print(czas)

    print("czas upłynoł")

elif zad == 4:

