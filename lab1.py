import random
import math


def dodawanie(a, b):
    print(f"wynik: {a + b}")


def odejmowanie(a, b):
    print(f"wynik: {a - b}")


def mnozenie(a, b):
    print(f"wynik: {a * b}")


def dzielenie(a, b):
    if b == 0:
        print("nie dzielimy przez 0")
    else:
        print(f"wynik: {a / b}")


if __name__ == '__main__':

    # zad1
    print(type(1 + 2))  # dodawanie całkowite
    print(type(1 + 4.5))  # dodawanie z liczba ułamkową
    print(type(1 / 2))  # dzielenie
    print(type(4 / 2))  # dzielenie
    print(type(3 // 2))  # dzielenie całkowite
    print(type(-3 // 2))  # dzielenie całkowite
    print(type(11 % 2))  # reszta z dzielenia
    print(type(2 ** 10))  # reszta z dzielenia dwóch liczb całkowitych
    print(type(8 ** (1 / 3)))  # potęgowanie

    # zad2

    int(3.0)  # zmiana tzw żutowanie liczby zmienno przecinkowej na całkowitą
    float(3)  # zmiana tzw żutowanie liczby całkowitej na zmienno przecinkową
    float("3")  # zmiana tzw żutowanie znaku string na zmienno przecinkową
    str(12.4)  # zmiana tzw żutowanie liczby zmienno przecinkowej na ciąg znaków string
    bool(0)  # zmiana tzw żutowanie liczby całkowitej na wartość logiczną False

    # ////////////////////////////////////////////////////////////////////////////////////////
    # zad 3 + 5
    print("Podaj długość boków prostokąta")
    a = int(input("A: "))
    b = int(input("B: "))
    # c = int(input("C: "))
    print(f"pole prostokąta wynosi:{a * b}")
    5
    print(f"pole obwód wynosi:{2 * a + 2 * b}")
    '''
    x = 5
    print(x)
    print("x= ", x)
    y = input("podaj licze: ")
    z = int(input("podaj liczbę: "))


    c = x + int(y) + z
    print(f"suma: {c}")
    '''

    # ////////////////////////////////////////////////////////////////////////////////////////
    # zad 4 + 4.1 + 5
    los = random.randint(-2, 5)
    cenaPaliwa = 6.5

    odcinekDrogi = los  # float(input("Podaj Odcinek drogi w km: "))
    litryBezyny = 1 / 100
    print("przebyta droga: ", los, "km")
    print(f"cena paliwa: {(odcinekDrogi * litryBezyny) * cenaPaliwa} zł")
    print(f"zużycie paliwa: {(odcinekDrogi * litryBezyny)} l")
    # ////////////////////////////////////////////////////////////////////////////////////////
    # zad dodatkowe 1
    print("zadanie dodatkowe 1. 0=ax+b")
    x = random.randint(-2, 5)
    a = int(input("podaj liczbę A: "))
    b = int(input("podaj liczbę B: "))
    y = a * x + b
    print(f"wynik: {y}")
    # zad dodatkowe 2
    print("zadanie dodatkowe 2. pole trujkąta A,B,C")
    a = int(input("podaj liczbę A: "))
    b = int(input("podaj liczbę B: "))
    c = int(input("podaj liczbę C: "))
    p = ((a + b + c) / 2)
    pole = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print(f"wynik pola to: {pole}")
    # ////////////////////////////////////////////////////////////////////////////////////////
    # zad dodatkowe 3
    print("zadanie dodatkowe 3. kalkulator")
    odp = 0
    while (odp != 5):
        print("1. dodawanie")
        print("2. odejmowanie")
        print("3. mnożenie")
        print("4. dzielenie")
        print("5. koniec")
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

        elif (odp != 0):
            print("Niema takiej opcji ")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
