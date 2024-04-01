def fubF(x,n):
    #print(x,n)
    if n==1:
        #print(x)
        return x
    elif n % 3 ==0:
        k=fubF(x,n // 3)
        #print(k*k*k)
        print("2")
        return k*k*k
    else:
        #print(x*fubF(x,n-1))
        print("1")
        return x*fubF(x,n-1)


fubF(4,9)
