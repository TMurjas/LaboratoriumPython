
def silnia(n):
    if n==0: return 1
    else: return n*silnia(n-1)

def silnia_liczba(n):

    i=0
    while (n>silnia(i)):
        i+=1
        print(i,silnia(i))
    i-=1

    x=n
    moje_list=[]
    print("////////////////////////////////////")
    for j in range(i):
        print(x,i-j,x//silnia(i-j),x%silnia(i-j))
        moje_list.append(x//silnia(i-j))
        x=x%silnia(i-j)
    print(moje_list)



def silnia_poz(nam):
    my_list=list(map(int,str(nam)))
    suma=0
    for i in range(len(my_list)):
        suma+=my_list[i]*silnia(len(my_list)-i)
        print(my_list[i],"*",(len(my_list)-i),"! (",silnia(len(my_list)-i),") =",(my_list[i]*silnia(len(my_list)-i)))

    print("wynik=",suma)

number=1033221
print("liczba: ",number)
silnia_poz(number)
print("////////////////////////////////////")
silnia_liczba(5489)