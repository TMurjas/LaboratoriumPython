import random

if __name__ == '__main__':

    zad=18
##############################################
    if zad == 1:
      lista=["Tomek","Romek","Arek","Mirek"]
      lista=sorted(lista)
      print(lista)
      lista.append("Antek")
      lista.append("Ola")
      zmienna=lista.pop()
      print(zmienna)
      lista.insert(2, "Aga")
      print(lista)
      lista = sorted(lista)
      lista.reverse()
      lista*=2
      print(lista)
##############################################
    elif zad == 2:
        tekst = "Rzeszów_jest_piękny"
        print(tekst)
        print(tekst[0])
        # print(tekst[6], tekst[9], tekst[12], tekst[1])
        print(tekst[6:14:3]+tekst[1])
##############################################
    elif zad == 3:
        tekst = "Python jest super"
        print(tekst[0])
        print(tekst[-1])
        print(tekst[::2])
        print(tekst[1::3])
        print(tekst[10:])
        print(tekst[::-1])
##############################################
    elif zad == 4:
        imie = input("podaj imie: ")
        nazwisko = input("podaj nazwisko: ")
        print("Witaj ", imie, nazwisko)
        wiek = input("podaj wiek: ")

        while (not wiek.isdigit() ):
            print("zle podany wiek sprobuj ponownie")
            wiek = input("podaj wiek: ")
            if wiek.isdigit():
                wiek=int(wiek)
                if (wiek <= 0)or(wiek>200):
                    wiek="non"
                    continue
                else:
                    break

        print(f"Twój wiek to: {wiek}")
        print("Twoje inicłay to: ", imie[0].upper() +"."+ nazwisko[0].upper()+".")

        str = input("podaj łancuch który wyswietle 5 razy: ")
        str*=5
        print(str)


        str_1 = input("podaj łancuch 1: ")
        str_2 = input("podaj łancuch 2: ")
        str_3 = str_1 + " " + str_2
        print(f"twoj łancuch po połonczeniu to{str_3}")
        x = len(str_1) // 2
        y = len(str_2) // 2
        str4 = str_1[:x] + " " + str_2[y:]
        print(f"poł1 i poł 2 łancucha to: {str4}")
##############################################
    elif zad == 5:
       zdanie=input("podaj zdanie: ")

       print(sorted(zdanie))
       alfabet=set()

       for i in range (32,97):
         alfabet.add(chr(i))
       for i in range(123, 127):
             alfabet.add(chr(i))

       zdanie=zdanie.upper()
       zdanie = set(zdanie)
       print(alfabet)
       nowyalf=alfabet-zdanie
       print(nowyalf)
##############################################
    elif zad == 6:
        zdanie = input("podaj zdanie: ")
        nowezdanie=zdanie[1::2]
        print(nowezdanie)
##############################################
    elif zad == 7:
        zdanie = input("podaj zdanie: ")
        zdanie=zdanie.lower()
        zdanie=zdanie.title()
        list = zdanie.split()
        print(list)
        strte=""
        for x in range(len(list)):
          if x>0:
            strte+=" "
          zdanieTemp=list[x]
          str=zdanieTemp[-1].upper()
          zdanieTemp = zdanieTemp[:-1]+str
          list[x]=zdanieTemp
          strte+=zdanieTemp

        print(strte)
##############################################
    elif zad == 8:
        #Napisz program, który zamieni w ciągu znaków podanym przez użytkownika każdy
        #znak, który się powtórzy na @. Zmieniony ciąg znaków wypisze na ekran.

        pass
##############################################
    elif zad == 9:
        zdanie = input("podaj zdanie: ")
        list = zdanie.split()
        zdanie=""
        for i in range(len(list)):
            if len(zdanie)<len(list[i]):
              zdanie=list[i]

        print(len(zdanie))
        print(zdanie)
##############################################
    elif zad == 10:
        zdanie = input("podaj zdanie: ")
        if zdanie==zdanie[::-1]:
            print("tak")
        else:
            print("nie")
##############################################
    elif zad == 11:
        n=" "
        while(not n.isdigit()):
          n=input("podaj n elemetow tablicy ")

        n = int(n)
        x = " "
        while (not x.isdigit()):
          x = input("podaj x elemetow w tablicy ")
        x = int(x)
        znaki=0
        list=[""]*n
        for i in range(n):
            for j in range(random.randint(1,x)):
              list[i]+=chr(random.randint(65,91))
              znaki+=1
        print("lista to",list)
        print("ilosc znaków w liscie",znaki)
        znaki = 0

        for i in range(len(list)):
            znaki += len(list[i])
        print("ilosc znaków w liscie sposub 2",znaki)
        znakiK = 0
        for i in range(len(list)):
            for j in list[i]:
                if j=="K":
                    znakiK += 1

        print("ilosc K w liscie",znakiK)

        znakiK = 0
        for i in range(len(list)):
            for j in list[i]:
                if j=="KT":
                    znakiK += 1

        print("ilosc KT w liscie",znakiK)

        s = " "
        while (not s.isdigit()):
            s = input("podaj n elemetow tablicy ")
        s = int(s)

        znakiK = 0

        for i in range(len(list)):
            if len(list[i])>s:
                znakiK += 1
        print("ilosc elemętów w liscie wiekszych od S",znakiK)

        for i in range(len(list)):
            str="a"+list[i]+"z"
            list[i]=str

        print("lista po dodaniu a i z",list)
##############################################
    elif zad == 12:
        lista=[]
        for i in range(65,91):
            lista.append(chr(i))

        print(lista)
        x=""
        while (not x.isdigit()):
          x = input("podaj n elemęty tablicy ")
        else:x = int(x)

        num=len(lista)//x
        res = len(lista) % x
        newlista=[]
        str=""
        for i in range(num):
            for j in range(x):
                str+=lista.pop(0)
            newlista.append(str)
            str = ""
        str = ""
        if res>0:
          for i in range(res):
              str+=lista.pop(0)
          newlista.append(str)
          str = ""
        print(lista)
        print(newlista)
##############################################
    elif zad == 13:

        n = " "
        while (not n.isdigit()):
            n = input("podaj n elemetow tablicy ")

        n = int(n)
        x = " "
        while (not x.isdigit()):
            x = input("podaj x elemetow w tablicy ")
        x = int(x)
        znaki = 0
        list = [""] * n
        for i in range(n):
            for j in range(random.randint(1, x)):
                list[i] += chr(random.randint(65, 91))
                znaki += 1
        krot=tuple(list)
        print("typ to",type( krot))
        print("ilosc znaków w krotce sposub 1", znaki)
        znaki = 0
        print("krotka to", krot)

        for i in range(len(krot)):
            znaki += len(krot[i])
        print("ilosc znaków w krotce sposub 2",znaki)
        znakiK = 0
        for i in range(len(krot)):
            for j in krot[i]:
                if j=="K":
                    znakiK += 1

        print("ilosc K w krotce",znakiK)

        znakiK = 0
        for i in range(len(krot)):
            for j in krot[i]:
                if j=="KT":
                    znakiK += 1

        print("ilosc KT w krotce",znakiK)

        s = " "
        while (not s.isdigit()):
            s = input("podaj n elemetow tablicy ")
        s = int(s)

        znakiK = 0

        for i in range(len(krot)):
            if len(krot[i])>s:
                znakiK += 1
        print("ilosc elemętów w krotce wiekszych od S",znakiK)
##############################################
    elif zad == 14:
        zakupy={"mleko":3,"ser":7,"piwo":4}
        print(zakupy)
        cena=0
        for i in zakupy:
          cena+=zakupy[i]
        print("cena wszystkich zakupow to: ",cena,"zł")
        ostatnirah=0
##############################################
    elif zad == 15:
        prad={"luty":100,"kwiecien":120,"czerwiec":300,"sierpien":200,"pazdziernik":50,"grudzień":500}
        srednia=0
        max=0
        min=prad["luty"]
        for i in prad:
          srednia+=prad[i]
          ostatnirah=prad[i]
          if max<prad[i]:
            max=prad[i]
          if min>prad[i]:
            min=prad[i]

        print("ostatni rachunek sposub 1 ",ostatnirah)
        ostatnirah = 0
        str=list(prad.keys())
        str=str[len(str)-1]
        ostatnirah = prad[str]
        print("ostatni rachunek sposub 2 ", ostatnirah)

        print("suma rachunków to ", srednia)
        print("najwiekszy rachunek to ", max)
        print("najmiejszy rachunek to ", min)
        srednia=(srednia//len(prad))
        print("srednia rachunków to ", srednia)

        if ostatnirah>srednia:
            print("zacznij oszczedzac!")
        elif ostatnirah<=srednia:
            print("Jesteś bezpieczny")
        else:
            print("coś poszło nie tak")
##############################################
    elif zad == 16:
        zbiurX = set()
        zbiurY = set()

        for i in range(random.randint(3, 8)):
            zbiurX.add(random.randint(0, 10))
        for i in range(random.randint(3, 8)):
            zbiurY.add(random.randint(0, 10))

        print("Zbiór X: ",zbiurX)
        print("Zbiór Y: ", zbiurY)

        if 5 in zbiurX:
            print("w zbiorze X zawiera się liczba 5")
        else:
            print("w zbiorze X nie zawiera się liczba 5")

        sumX = zbiurX-zbiurY
        sumY = zbiurY - zbiurX
        if len(sumX)==0:
            print("Zbiór X jest podzbiorem Y")
        else:
            print("Zbiór X nie jest podzbiorem Y")

        if len(sumY) == 0:
            print("Zbiór Y jest podzbiorem X")
        else:
            print("Zbiór y nie jest podzbiorem X")

        if len(sumX) == 0:
            if sumX!=sumY:
                print("Zbiór Y jest nadzbiorem X")
            else:
                print("Zbiór X i Y są sobie równe ")
        else:
            print("Zbiór Y nie jest nadzbiorem X")

        if len(sumY) == 0:
            if sumX!=sumY:
                print("Zbiór X jest nadzbiorem Y")
            else:
                print("Zbiór X i Y są sobie równe ")
        else:
            print("Zbiór X nie jest nadzbiorem Y")

        print("suma zbioru X i Y: ", zbiurX|zbiurY)
        print("różnica zbioru X - Y: ", zbiurX - zbiurY)
        print("różnica zbioru Y - X: ", zbiurY - zbiurX)
        print("iloczyn zbioru Y i X: ", zbiurX & zbiurY)
        print("iloczyn zbioru Y i X: ", zbiurX ^ zbiurY)
        print("różnica zbioru Y - X: ", zbiurY)

        maxX=0
        for i in zbiurX:
            maxX=i
        print("najwiekszy elemęt w zbiorze X to: ",maxX)

        maxY=0
        for i in zbiurY:
            maxY=i
        print("najwiekszy elemęt w zbiorze Y to: ",maxY)


        for i in zbiurX:
            PierwszaWZbiorzeX = i
            break
        print("Pierwsza liczba w zbiorzeX to: ",PierwszaWZbiorzeX)
        zbiurX.discard(PierwszaWZbiorzeX)
        print("bez Pierwszej liczba w zbiorze X to: ", zbiurX)
        zbiurY.add(PierwszaWZbiorzeX)
        print("dodanie Pierwszej liczba z zbiorze X do Zbioru Y to: ", zbiurY)

        zbiurY|=zbiurX
        print("dodanie wszystkich elemętów zbioru X do zbioru Y: ", zbiurY)
        zbiurX.clear()
        print("Czyszczenie zbioru X: ", zbiurX)
        zbiurY.clear()
        print("Czyszczenie zbioru Y: ", zbiurY)
##############################################
    elif zad == 17:
        str=input("podaj 5 liczb rozdzielone przecinkami")
        strList=str.split(",")
        liczby=[]
        for i in range(len(strList)):
            if strList[i].isdigit():
                liczby.append(int(strList[i]))

        print(strList)
        print(liczby)
        if len(liczby)<=5 and len(liczby)>0 :
            zbior=set(liczby)
            liczbaPop=zbior.pop()
            print(liczbaPop)

            if liczbaPop==max(liczby):
                print("Wylosowałeś największa liczbę w zbiorze")
                if liczbaPop==min(liczby):
                  print("i zarazem najmniejszą więc podałeś tylko 1 liczbę spryciażu")
            elif liczbaPop==min(liczby):
                print("Wylosowałeś najmniejszą liczbę w zbiorze")
            else:
                print("nic szczególnego nie wylosowałeś")
        else:
            print("Podałeś za dużo lub nie podałeś żadnej liczby")
##############################################
    elif zad == 18:
        playerSpr="o"
        playerX=0
        playerY=0

        enemySpr="X"
        enemyX=[0, 2, 2, 3]
        enemyY=[1, 3, 4, 4]

        coinSpr="*"
        coinX = [0, 2, 2, 3]
        coinY = [1, 3, 4, 4]




        enemySpr="x"
        land=[[",",",","=",",",",",",",","],
              [",",",","=",",",",",",",","],
              [",",",","|",",",",",",",","],
              [",",",","=",",",",",",",","],
              [",",",","=",",",",",",",","],
              [",",",","=",",",",",",",","]]


        while (True):
          land =   [[",", ",", "=", ",", ",", ",", ","],
                    [",", ",", "|", ",", ",", ",", ","],
                    [",", ",", "=", ",", ",", ",", ","],
                    [",", ",", "=", ",", ",", ",", ","],
                    [",", ",", "|", ",", ",", ",", ","],
                    [",", ",", "=", ",", ",", ",", ","]]
          land[enemyX[0]][enemyY[0]] = enemySpr
          land[enemyX[1]][enemyY[1]] = enemySpr
          land[enemyX[2]][enemyY[2]] = enemySpr
          land[enemyX[3]][enemyY[3]] = enemySpr

          land[playerX][playerY] = playerSpr
          land[playerX][playerY]=playerSpr
          print(f"[{land[0][0]}][{land[1][0]}][{land[2][0]}][{land[3][0]}][{land[4][0]}][{land[5][0]}]")
          print(f"[{land[0][1]}][{land[1][1]}][{land[2][1]}][{land[3][1]}][{land[4][1]}][{land[5][1]}]")
          print(f"[{land[0][2]}][{land[1][2]}][{land[2][2]}][{land[3][2]}][{land[4][2]}][{land[5][2]}]")
          print(f"[{land[0][3]}][{land[1][3]}][{land[2][3]}][{land[3][3]}][{land[4][3]}][{land[5][3]}]")
          print(f"[{land[0][4]}][{land[1][4]}][{land[2][4]}][{land[3][4]}][{land[4][4]}][{land[5][4]}]")
          action=input("type Direction to go up, down, left, right: ")

          if action=="left":
              if playerX>0:
                  playerX-=1
              else:
                  print("you hit the endge of the map")
          elif action=="right":
              if playerX < 5:
                playerX += 1
              else:
                print("you hit the endge of the map")
          elif action == "up":
              if playerY > 0:
                  playerY -= 1
              else:
                  print("you hit the endge of the map")
          elif action == "down":
              if playerY <4:
                  playerY += 1
              else:
                  print("you hit the endge of the map")
















