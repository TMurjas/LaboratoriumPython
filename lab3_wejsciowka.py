
if __name__ == '__main__':
  print("1. liczby parzyste")
  print("2. liczba dodatnia")
  zadanie = int(input("podaj numer zadania: "))
  if zadanie == 1 :

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
  elif zadanie == 2 :
      liczba=0
      while(True):
          liczba=int(input("podaj liczbe dodatnia: "))

          if liczba>0:
              break
          else:
            print("Podałes zla liczbe sprobuj ponownie.")

      print(f"twoja dodatnia liczba to {liczba}")


