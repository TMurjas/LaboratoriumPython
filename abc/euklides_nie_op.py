
#def silnia(n):
#    if n==0: return 1
#    else: return n*silnia(n-1)

#print(silnia(3))

#def NWDIter(a,b):
#    while a!=b:
#        if a>b: a=a-b
#        else: b=b-a
#    return a
#print(NWDIter(12,18))
#print(NWDIter(28,24))

#def NWDIterOp(a,b):
#    while (b>0):
#        pom=b
#        b=a%b
#        a=pom
#    return a
#print(NWDIterOp(12,18))
#print(NWDIterOp(28,24))

#def NWDRek(a,b):
#    if a!=b:
#        if a>b: return NWDRek(a-b,b)
#        else: return NWDRek(a,b-a)
#    return a
#print(NWDRek(12,18))
#print(NWDRek(28,24))

#def NWDRekOp(a,b):
#    if b>0:
#        return NWDRekOp(b,a%b)
#    return a
#print(NWDRekOp(12,18))
#print(NWDRekOp(28,24))

#def nwdIIIter(a,b):
#    while b!=0:
#        temp=b
#        b=a%b
#        a=temp
#    return a

#def nwdRek(a,b):
#    if b!=0: return nwdRek(b, a%b)

#def funkcja(i):
#  if (i<3):
#    return 1
#  elif (i % 2 ==0):
#    print("wywolanie funkcji bez glownej")
#    return funkcja(i-3) + funkcja(i-1)+1
#  else:
#    print("wywolanie funkcji bez glownej")
#    return funkcja(i-1) % 7
  
#def rek(n):
#   if n>=1:
#      return


#def naBinarne(n):
#    if n>0:
#        naBinarne(n // 2)
#    print(n%2,end="")
#naBinarne(100)



#def tab_rek(n,tab):
#    if n==0:
#       return tab
#    else:
 #     pom=tab[0]
      
#      for i in range(n):
#         if pom<tab[i]:
#            pom=tab[i]
        
#      tab[n]=pom
#      return tab_rek(n-1,tab)

#def funkcja2(n):
#    if n>=1:
#      if (n==1): return 4
#      else: return (1 / (1-funkcja2(n-1)))


#public static void hanoi(char A, char B, char C, int n) {
#  if(n>0) {
#    hanoi(A,C,B,n-1);
#    System.ouit.println("moving from " + A + " to " + B);
#    hanoi(C,B,A,n-1);
# }
#}

#def hanoi(n, A, B, C):
#  if (n > 0):
#    hanoi(n - 1, A, C, B);
#    C.push(A.pop());
#    hanoi(n - 1, B, A, C);

def mojeHanoi(n, lewy, srodek, prawy):
    if (n > 0):
        mojeHanoi(n-1, lewy, prawy, srodek)
        prawy.insert(0, lewy.pop(0))
        mojeHanoi(n-1, srodek, lewy, prawy)
lewy=[1,2,3,4,5]
srodek=[]
prawy=[]
n=len(lewy)
print(lewy,srodek,prawy)
mojeHanoi(n, lewy, srodek, prawy)
print(lewy,srodek,prawy)
    
#def dobinarnej(n, b):
#   if n>1:
#      print(str((n%2)))
#      b+=str((int(n%2)))
#      print(type(b))
#      print(b,"wynik")
#      return dobinarnej(n/2,b)
#    return (b+"1")

#funkcja2
#if __name__ == '__main__':
   #print(funkcja2(1))

   #print(funkcja2(8))
   #print(funkcja2(9))
   #print(funkcja2(10))
   #print(funkcja2(100))

   #lewy=[1,2,3,4,5]
   #srodek=[]
   #prawy=[]
   #n=len(lewy)
   #print(lewy,srodek,prawy)
   #mojeHanoi(n, lewy, srodek, prawy)
   #print(lewy,srodek,prawy)


   #print(NWDIterOp(12,18))
   #print(NWDIterOp(28, 24))
   #print(nwdRekOp(12, 18))

   #n= int(input("N: "))

   #print(silnia(n))

   #a= int(input("A: "))
   #b= int(input("B: "))

   #print(NWDIter(a,b))
   #print(nwdRek(a,b))

   #print(funkcja(2))
   #print(funkcja(3))
   #print(funkcja(4))
   #print(funkcja(5))
   #print(funkcja(6))
   #print(funkcja(7))
   #print(funkcja(8))

   #naBinarne(10)

   #Zadanie 2. Napisz funkcję rekurencyjną, która odwraca elementy tablicy.
   #tablica=[1, 2, 3, 4, 5]

   #tab_rek(len(tablica),tablica)
