def odwroc(lista):
  if (len(lista) == 0):
    return []
  else:
    return [lista.pop()] + odwroc(lista)

mLista=[1,2,3,4,5]
mLista=odwroc(mLista)
print(mLista)


#def silnia(n):
#  if n > 1:
#    return n * silnia(n - 1)
#  return 1

#print(silnia(3))