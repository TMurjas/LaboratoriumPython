



if __name__ == '__main__':

    zad=10
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



