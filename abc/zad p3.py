def wynik(i):
  if i < 3:
    print("wynik")
    return 1
  elif i % 2 == 0:

    return wynik(i - 3) + wynik(i - 1) + 1
  else:

    return wynik(i - 1) % 7

print(wynik(0))
print(wynik(3))
print(wynik(5))
print(wynik(7))
print(wynik(9))
print(wynik(10))