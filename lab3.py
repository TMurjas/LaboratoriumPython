if __name__ == '__main__':
    print("1. petla for przedziały liczb")
    print("2. wyswietl *** gwiazdki")
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
        gwiazdki = int(input("podaj ile razy ma wyswietlic ***: "))
        star = ""
        space = " "
        for x in range(gwiazdki):
            for y in range(gwiazdki-x):
                space+=" "
            star += "*"
            print(space+star)
            space = " "

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
             wynik*=i

         print(f"silnia {s}! = ",wynik)

    elif zadanie == 7:
         pass

    elif zadanie == 8:
         pass

    elif zadanie == 8:
         tekst = "Rzeszów jest piękny"
         print(tekst[0])
         #print(tekst[6], tekst[9], tekst[12], tekst[1])
         print(tekst[6:14:3])
        print(tekst[-2])
    elif zadanie == 9:
         tekst = "Python jest super"
         print(tekst[0])
         print(tekst[6], tekst[9], tekst[12], tekst[1])

        #2-3 - lancuchy
        #3-6 - for


