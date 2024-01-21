import random
import math
import time
import keyword
import datetime
import statistics
import calendar

zad=10
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
    def numOfDays(date1, date2):
        # check which date is greater to avoid days output in -ve number
            return (date1 - date2).days



    date1 = datetime.date(2023, 12, 19)
    date2 = datetime.date(2024, 1, 15)
    date3 = datetime.date(2024, 2, 12)
    print(numOfDays(date2, date1), "dni")
    print(numOfDays(date3, datetime.date.today()), "dni do kolokwium")

elif zad == 5:
    klucze=["for","print","break","done","bad"]
    for i in range(len(klucze)):
      if keyword.iskeyword(klucze[i]):
         print(klucze[i]," jest słowek kluczowym")
      else:
          print(klucze[i], " nie jest słowek kluczowym")

elif zad == 6:
    print(dir(math))
    print(dir(tuple))
    print(dir(keyword))
elif zad == 7:
    ran1 = int(input("podaj dolny przedział: "))
    ran2 = int(input("podaj górny przedział: "))
    tab=[""]*10
    for i in range(len(tab)):
        tab[i]=random.randint(ran1, ran2)
    krotka= tuple(tab)
    print(krotka)
    print(statistics.geometric_mean(krotka))
elif zad == 8:
        a, b, c = input("Podaj 3 boki trójkąta (oddzielone przecinkami): ")

        if a + b > c and a + c > b and b + c > a:
            print("Z podanych boków można zbudować trójkąt.")
            if (a ** 2 + b ** 2 > c ** 2 or
                    a ** 2 + c ** 2 > b ** 2 or
                    b ** 2 + c ** 2 > a ** 2):

                print ("Obwód wynosi:", (a + b + c))
                pole = 0.5 * (a + b + c)
                pole = math.sqrt(pole * (pole - a) * (pole - b) * (pole - c))
                print ("Pole wynosi:", pole)
        else:
            print
            "Z podanych odcinków nie można utworzyć trójkąta"
elif zad == 9:
    ran1 = int(input("podaj dolny przedział: "))
    ran2 = int(input("podaj górny przedział: "))
    liczba=random.randint(ran1, ran2)

    i=3
    while(i>0):
        print(f"masz {i} szanse")
        odp = int(input("podaj wylosowaną liczbe: "))
        if odp==liczba:
            print("Wygrałes wylosowana liczba to: ",liczba)
            break;
        elif odp>liczba:
            print("twoja liczba jest za duża")
        elif odp < liczba:
            print("twoja liczba jest za mała")
        i-=1
    else:
        print(f"Nie udało sie liczba wynosiła {liczba} spróbuj ponownie")

elif zad == 10:
    rok = int(input("podaj rok: "))
    mie = int(input("podaj miesiąc: "))
    dni = int(input("podaj dzień: "))
    date1 = datetime.date(rok, mie, dni)
    print(date1)
    print("nr tygodnia to: ",date1.strftime("%U"))

    for i in range(6):
        date2 = date1 + datetime.timedelta(days=i)
        if date2.strftime("%A")=="Sunday":
            break
    print(date2,date2.strftime("%A"))
    print(date1 + datetime.timedelta(days=14))
    print(date1 - datetime.timedelta(days=14))
    date = datetime.datetime.utcnow()
    utc_time = calendar.timegm(date.utctimetuple())
    print(utc_time)


