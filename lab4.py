import random



if __name__ == '__main__':

    zad=15
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
    elif zad==2:
        tekst = "Rzeszów_jest_piękny"
        print(tekst)
        print(tekst[0])
        # print(tekst[6], tekst[9], tekst[12], tekst[1])
        print(tekst[6:14:3]+tekst[1])
##############################################
    elif zad==3:
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

    elif zad == 8:
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

    elif zad == 14:
        zakupy={"mleko":3,"ser":7,"piwo":4}
        print(zakupy)
        cena=0
        for i in zakupy:
          cena+=zakupy[i]
        print("cena wszystkich zakupow to: ",cena,"zł")

    elif zad == 15:
        prad={"luty":100,"kwiecien":120,"czerwiec":300,"sierpien":200,"pazdziernik":50,"grudzień":500}
        srednia=0
        max=0
        min=prad["luty"]
        print(min)
        for i in prad:
          srednia+=prad[i]

          if max<prad[i]:
            max=prad[i]
          if min>prad[i]:
            min=prad[i]

        print("suma rachunków to ", srednia)
        print("najwiekszy rachunek to ", max)
        print("najmiejszy rachunek to ", min)
        srednia=(srednia//len(prad))
        print("srednia rachunków to ", srednia)




