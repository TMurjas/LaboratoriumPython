
if __name__ == '__main__':
    print("1. petla for przedziały liczb")
    print("2. wyswietl *** gwiazdki")
    print("3. wyswietl pol choinki")
    print("4. wyswietl cała choinki")
    print("5. ciąg arytmetyczny")
    print("6. oblicz silnie")
    print("7. wyswietl to jest liczba")
    print("8. wyswietl pierwiastek")
    print("9. string rzeszów")
    print("10. Python jest super")

    zadanie=int(input("podaj nr zadania: "))
    if zadanie == 1:
        print("wypisz od 1 do 100")
        for x in range (100):
            print(x+1)

        print("wypisz od 100 do 0")
        for x in range(100, -1, -1):
            print(x)

        print("wypisz od 7 do 77 co 7")
        for x in range(7, 78, 7):
            print(x)

        print("wypisz od 20 do 0 co 2")
        for x in range(0, 22, 2):
            print(20-x)
########################################
    elif zadanie == 2:
        gwiazdki = int(input("podaj ile razy ma wyswietlic ***: "))
        for x in range(gwiazdki):
            for y in range(gwiazdki):
              print("* ", end="")
        print()
########################################
    elif zadanie == 3:
        gwiazdki = int(input("podaj ile razy ma wyswietlic * : "))
        star = ""
        for x in range(gwiazdki):
          star += "*"
          print(star)
########################################
    elif zadanie == 4:
        ch = int(input("Ilu stopniową choinkę mam narysować? "))
        spacja = ' '
        gwiazdka = '*'
        k = ch
        for n in range(0, ch + 1):
          i = 2 * n - 1
          print(k * spacja + i * gwiazdka)
          k = k - 1
    ########################################
    elif zadanie == 5:
         n = int(input("długosć ciągu N: "))
         a = int(input("pierwszy wyraz ciagu: "))
         r = int(input("roznica ciągu: "))

         for i in range(n):
             print(a+i*r)

    elif zadanie == 6:
         s = int(input("podaj kolejnosc silni: "))
         wynik=1
         for i in range(1,s+1):
             wynik *= i

         print(f"silnia {s}! = ",wynik)

    elif zadanie == 7:
        while (True):
            dana = input("podaj liczbe nie ujemną: ")
            if dana.isnumeric():
                dana = int(dana)
            else:
                dana = -1
            if dana>=0:
              print("to jest liczba")
              continue
            break


    elif zadanie == 8:
         dana = input("podaj liczbe nie ujemną: ")

         if dana.isnumeric():
             dana = int(dana)
         else: dana=-1

         if dana>=0:
            print(dana**0.5)
         else: print("dziękujemy za skorzystanie z naszej aplikacji'")

    elif zadanie == 9:
         tekst = "Rzeszów jest piękny"
         print(tekst[0])
         #print(tekst[6], tekst[9], tekst[12], tekst[1])
         print(tekst[6:14:3])
         print(tekst[-2])
    elif zadanie == 10:
         tekst = "Python jest super"
         print(tekst[0])
         print(tekst[-1])
         print(tekst[ : :2])
         print(tekst[1: :3])
         print(tekst[10:])
         print(tekst[::-1])

    elif zadanie == 11:
        imie=input("podaj imie: ")
        nazwisko = input("podaj nazwisko: ")
        print("Witaj ",imie, nazwisko)
        wiek = input("podaj wiek: ")
        print(f"Twój wiek to: {wiek}")
        print("Twoje inicłay to: ",imie[0]+nazwisko[0])

        str = input("podaj łancuch który wyswietle 5 razy: ")

        for i in range(5):
            print(str)

        str_1= input("podaj łancuch 1: ")
        str_2 = input("podaj łancuch 2: ")
        str_3 = str_1+" "+str_2
        print(f"twoj łancuch po połonczeniu to{str_3}")
        x=len(str_1) // 2
        y=len(str_2) // 2
        str4=str_1[:x]+" "+str_2[y:]
        print(f"poł1 i poł 2 łancucha to: {str4}")
