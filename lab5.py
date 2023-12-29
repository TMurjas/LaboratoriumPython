
zad=17

if zad==1:
  def poleKola(r):
      pole=3.14*float(r**2)
      print(pole)


  licz = float(input("podaj promien koło "))
  poleKola(licz)


elif zad==2:
    def poleTrap(a,b,h):
        pole=((a+b)*h)/2
        print(pole)
        return pole


    a = float(input("podaj A "))
    b = float(input("podaj B "))
    h = float(input("podaj H "))
    pole=poleTrap(a,b,h)
    print(pole)

elif zad == 3:
    def imieWiek(a,b=20):
        print(a,b)


    print(imieWiek.__doc__)
    imie = input("podaj koło pola ")
    wiek = int(input("podaj koło pola "))
    imieWiek(imie,wiek)

elif zad == 4:
    def czyDodatnia(x):
        if (x < 0):
            print("liczba jest ujemna")
        else:
            print("liczba jest dodatnia")


    licz=int(input("podaj liczbe "))
    czyDodatnia(licz)

elif zad == 5:
   def obliczBMI(waga, wzrost):
       BMI = waga / ((wzrost/100) ** 2)
       print(BMI)


   wage = int(input("podaj wage w kg: "))
   wzrost = int(input("podaj wzrost w cm: "))

   obliczBMI(wage, wzrost)

elif zad == 6:
    def poleTruj(a,b,c):
        list = [float(a), float(b), float(c)]
        list = sorted(list)
        a = list[0]
        b = list[1]
        c = list[2]

        if (a + b) > c:
            p = (a + b + c) / 2.0
            P = (p * (p - a) * (p - b) * (p - c)) ** 0.5
            print(P)
        else:
            print("niema trujkata")

    a = ""
    b = ""
    c = ""

    while (not a.isdigit()):
        a=input("podaj bok A :")
    while (not b.isdigit()):
        b=input("podaj bok B :")
    while (not c.isdigit()):
        c=input("podaj bok C :" )

    poleTruj(a,b,c)


elif zad == 7:
    def odwrucstring(str):
        str=str[::-1]
        print(str)

    abc=input("podaj string ")
    odwrucstring(abc)
    print(abc)

elif zad == 8:
    def pow(x, n):
      if n == 1:
        return x
      else:
          if n % 3 == 0:
            k = pow(x, n // 3)
            return k * k * k
          else:
            return x * pow(x, n - 1)


    print(pow(2, 3))

elif zad == 9:
    def fib(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        return fib(n - 1) + fib(n - 2)


    print(fib(3))
elif zad == 10:
    def name(x):
        names={"Aga":"Kobieta","Monika":"Kobieta","Ola":"Kobieta",
               "Seba":"Mężczyzna","Marek":"Mężczyzna","Tomek":"Mężczyzna"}


        return names[x]


    print(name("Marek"))

elif zad == 11:
    def zmien(*x):
        max=x[0]

        for i in range(len(x)):
            if x[i]>max:
                max=x[i]
        return max

    print(zmien(5,6,10,7))


elif zad == 12:
    def rowKwa(a,b,c):
        delta=(b**2)-(4*a*c)
        print (delta)
        pierdelta=(delta**0.5)
        print(pierdelta)
        if delta<0:
            print("Delta niema rozwiazania")
            return ( )
        elif delta == 0:
            if a!=0:
              return (-b/(2*a))
            else:
              print("A nie może być 0")
              return ( )
        elif delta > 0:
            if a!=0:
              return ((-b-(pierdelta))/(a*2),(-b+(pierdelta))/(2*a))
            else:
              print("A nie może być 0")
              return ( )


    abc=rowKwa(1, 6, 5)
    print(abc)

elif zad == 13:
    def strCount(str):
        low=0
        upp=0
        el=0
        for i in range(len(str)):
          if str[i].islower():
              low+=1
          elif str[i].isupper():
              upp+=1
          else :
              el+=1

        return {"lower":low, "Upper":upp, "Rest":el}


    print(strCount(input("napisz coś ")))

elif zad == 14:
    def wspolne(list1,list2):
        new_list=[]
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i]==list2[j]:
                    new_list.append(list2[j])
        return(new_list)


    print(wspolne(["a","abc","c",1,5],["abc",1,6,"c","cda"]))

elif zad == 15:
    def nwd(a, b):
      if b > 0:
        return nwd(b, a % b)
      else:
        return a


    print(nwd(5,6))

elif zad == 16:
    def palindrom(zdanie):
        if zdanie==zdanie[::-1]:
            return "tak"

        else:
            return "nie"

    print(palindrom(input("podaj zdanie: ")))

elif zad == 17:
    def anagramami(zdanie1,zdanie2):
        zdanie1=zdanie1.lower()
        zdanie2=zdanie2.lower()
        zd1 = [*zdanie1]
        zd2 = [*zdanie2]
        zd1.sort()
        zd2.sort()

        if len(zd1)!=len(zd2):
            return "Nie"

        for i in range(len(zd1)):
            if zd1!=zd2:
                break;
                return "nie"

        return "tak"


    print(anagramami("AAbbc", "cbbaa"))








