def wynik(i):
  print("wynik")
  if i < 3:
    return 1
  elif i % 2 == 0:

    return wynik(i - 3) + wynik(i - 1) + 1
  else:

    return wynik(i - 1) % 7

print("0",wynik(0))
print("1",wynik(1))
print("2",wynik(2))
print("3",wynik(3))
print("4",wynik(4))
print("5",wynik(5))
print("6",wynik(6))
print("7",wynik(7))
print("8",wynik(8))
print("9",wynik(9))
print("10",wynik(10))
print("11",wynik(11))
print("12",wynik(12))
print("13",wynik(13))
print("14",wynik(14))
