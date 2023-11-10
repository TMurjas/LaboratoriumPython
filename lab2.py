import math
import random



def wiek(age):
    if (age < 4) and (age >= 0):
        print("wejsciówka jest darmowa")
    elif (age <= 18) and (age >= 4):
        print("wejsciówka kosztuje 10zł")
    elif age > 18:
        print("wejsciówka kosztuje 20 zł")
    else:
        print("nie prawidłowe dane podaj wiek w pełnych liczbach")


def dodawanie(a, b):
    print(f"wynik: {a + b}")


def odejmowanie(a, b):
    print(f"wynik: {a - b}")


def mnozenie(a, b):
    print(f"wynik: {a * b}")

def potegi(a, b):
    print(f"wynik: {a ** b}")


def dzielenie(a, b):
    if b == 0:
        print("nie dzielimy przez 0")
    else:
        print(f"wynik: {a / b}")

def rownaniekwadratowe(a, b, c):
    delta = b ** 2 - 4 * a * c
    print(f"delta to {delta}")
    if a != 0:
        if delta < 0:
           print("niema rozwiazania")
        elif delta == 0:
           print("delta ma 1 rozwiazanie")
           print(f" rozwiazanie delty to X= {-b/2*a}")
        elif delta > 0:
           print("delta ma 2 rozwiazania")
           print(f" rozwiazanie delty to X1 {-b-delta ** (1/2)/2*a}")
           print(f" rozwiazanie delty to X2 {-b+delta ** (1 / 2) / 2 * a}")
    else:
        print(f"rownanie nie jest kwadratowa i ma jedno rozwiazanie{-c/b}")



if __name__ == '__main__':
    print("1.Cena biletów")
    print("2.kalkulator z deltą")
    print("3.pętla while od mniejszej do większej liczby tylko z liczbami pażystymi")
    print("4.funkcja z petlą i krokiem o 0.5")
    print("5.sortowanie liczb")
    print("6.sprawdz wlekość litery")
    print("7.Funkcje X")
    print("8.czy pada deszcz")
    print("9.Zmiana litery z małej na dużą i z dużej na małą")
    print("10.petla nieskonczona")
    print("11. srednia dla studentów")


    zadanie=int(input("podaj numer zadania: "))
################################################

# 1.Cena biletów
    if zadanie == 1:
        wiek(int(input("podaj wiek ")))
################################################

# 2.kalkulator z deltą
    elif zadanie == 2:

        print("zadanie dodatkowe 3. kalkulator")
        odp = 0
        while (odp != 7):
            print("1. dodawanie")
            print("2. odejmowanie")
            print("3. mnożenie")
            print("4. dzielenie")
            print("5. potegowanie")
            print("6. rownanie kwadratowe")
            print("7. koniec")
            odp = int(input("podaj opcje: "))
            if (odp == 1):
                print("Dodawanie: ")
                a = int(input("A: "))
                print("dodac: ")
                b = int(input("B: "))
                dodawanie(a, b)
            elif (odp == 2):
                print("odejmowanie: ")
                a = int(input("A: "))
                print("odjac: ")
                b = int(input("B: "))
                odejmowanie(a, b)
            elif (odp == 3):
                print("mnozenie: ")
                a = int(input("A: "))
                print("pomnozyc przez: ")
                b = int(input("B: "))
                mnozenie(a, b)
            elif (odp == 4):
                print("dzielenie: ")
                a = int(input("A: "))
                print("podzielic przez: ")
                b = int(input("B: "))
                dzielenie(a, b)
            elif (odp == 5):
                print("potegowanie: ")
                a = int(input("A: "))
                print("do potęgi: ")
                b = int(input("B: "))
                potegi(a, b)
            elif (odp == 6):

                print("równanie kwadratowe: ")
                a = float(input("A: "))
                b = float(input("B: "))
                c = float(input("C: "))
                rownaniekwadratowe(a, b, c)

            elif (odp != 0):
                print("Niema takiej opcji ")
################################################

# 3.pętla while od mniejszej do większej liczby tylko z liczbami pażystymi
    elif zadanie == 3:
        a = int(input("podaj pierwszą liczbe "))
        b = int(input("podaj drugą liczbe "))

        if a > b:
            k = a
            p = b
        elif b > a:
            k = b
            p = a
        else:
            print("nie licze bo liczby są rowne")
            k = a
            p = b

            p-=1

        if a != b:
             while (p <= k):
               p += 1
               if p % 2:
                 continue
               print(p)

             else:
                print("end")
################################################

# 4.funkcja z petlą i krokiem o 0.5
    elif zadanie == 4:
        p = -4
        k = 4
        skok = 0.5
        while p<=k:
            y = 2*p**2-5*p-8
            print("dla x=", p, "rozwiazanie wynosi: ", y)
            p += skok
################################################

# 5. Sortowanie liczb
    elif zadanie == 5:
        tablicaLiczb = []
        liczba=int(input("Podaj ile liczb chcesz posortować "))
        for i in range(liczba):
            tablicaLiczb.append(int(input(f"{i+1}. liczba: ")))
        print("tablica wejsciowa: ", tablicaLiczb)
        for i in range(liczba):
            for j in range(liczba):
                if tablicaLiczb[j] > tablicaLiczb[i]:
                    liczbaPom = tablicaLiczb[i]
                    tablicaLiczb[i] = tablicaLiczb[j]
                    tablicaLiczb[j] = liczbaPom

        print("tablica wyjsciowa: ",tablicaLiczb)
################################################

# 6. sprawdz wlekość litery
    elif zadanie == 6:
      litera = input("podaj jedną litere: ")
      if litera.islower():
          print("podana litera jest z małej litery")
      elif litera.isupper():
          print("podana litera jest z dużej")
      else:
          print("błąd, nie może okreslic")
################################################

# 7. Funkcje X
    elif zadanie == 7:
        x = int(input("podaj jedną litere: "))
        if x < 0:
           print(f"dla x < 0 a(x) = -3*x = {-3*x}")
        elif x == 0:
           print("dla x = 0 a(x) = 0")
        elif x > 0:
           print(f"dla x > 0 a(x) = 2*x = {2*x}")

        if x >= 1:
           print(f"dla x >= 1 b(x) = x*x = {x*x}")
        elif x < 1:
           print(f"dla x < 1  b(x) = x = {x}")

        if x < 2:
           print(f"dla x < 2 c(x) = x-4 = {x-4}")
        elif x == 2:
           print(f"dla x = 2 c(x) = 8")
        elif x > 2:
           print(f"dla x > 2 c(x) = 2+x = {2+x}")
################################################

# 8. czy pada deszcz
    elif zadanie == 8:
        deszcz  = input("czy pada deszcz podaj. tak lub nie : ")
        autobus = input("czy jest autobus. tak lub nie : ")

        deszcz  = True if deszcz  == "tak" else False
        autobus = True if autobus == "tak" else False

        if deszcz and autobus:
            print("Weź parasol Dostaniesz się na uczelnie")
        elif deszcz and not autobus:
            print("Nie dostaniesz się na uczelnię")
        elif not deszcz and autobus:
            print("Dostaniesz się na uczelnie, Miłego dnia i pięknej pogody")
################################################

# 9. Zamiana małej litery an dużą
    elif zadanie == 9:
      litera = input("podaj jedną litere: ")
      if litera.islower():
          print(f"podana litera była mała została zamieniona na duża '{litera.upper()}'")
      elif litera.isupper():
          print(f"podana litera była dużą została zamieniona na małą '{litera.lower()}'")
      else:
          print("błąd, nie może okreslic")
################################################

# 10.petla nieskonczona
    elif zadanie == 10:
        while (True):
            koniec=int(input("podaj liczbe całkowitą (ujemną jesli chcesz wyjsc z pętli): "))
            if koniec<0:
                break;
################################################

# 11. srednia dla studentów
    elif zadanie == 11:
        #student=[]
        n = int(input("Podaj liczbe studentów: "))
        #for i in range(liczba):
        #    student.append(random.randint(50, 100))
        srednia=0
        i=0
        while (True):
            if i == n:
               break
            studentPunkty=int(input(f"podaj punkty studenta {i+1} z przedziału od 0 do 100: "))
            if studentPunkty>100 or studentPunkty<0:
               continue
            i+=1
            srednia+=studentPunkty
        srednia /= i
        print(f"srednia wynosi {srednia}")
