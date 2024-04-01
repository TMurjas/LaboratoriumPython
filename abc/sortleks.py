

tab=[9,1,11,2,111,101,22,232,23,4,5,3,32,33,333,44,45]
new_tab=[]
print(tab)
"""
################################################################
tab_s=[str(x) for x in tab]
tab_s.sort()
tab_s = [eval(i) for i in tab_s]
print(tab_s)

for i in range(len(tab_s)):
    for j in range(len(tab_s)):
        if (int(str(tab_s[i])[:1]) == int(str(tab_s[j])[:1])):
            if tab_s[i]<tab_s[j]:
                pom=tab_s[i]
                tab_s[i]=tab_s[j]
                tab_s[j]=pom

print(tab_s)
##################################################################
"""
tab=[9,1,11,2,111,101,22,232,23,4,5,3,32,33,333,44,45]
print(tab)
for i in range(len(tab)):
   for j in range(len(tab)):
       if (int(str(tab[i])[:1])<int(str(tab[j])[:1])):
           pom = tab[i]
           tab[i] = tab[j]
           tab[j] = pom

       elif (int(str(tab[i])[:1]) == int(str(tab[j])[:1])):
           if tab[i] < tab[j]:
              pom = tab[i]
              tab[i] = tab[j]
              tab[j] = pom

print(tab)
"""
for i in range(len(tab)):
   for j in range(len(tab)):
       if (i==int(str(tab[j])[:1])):
           new_tab.append(tab[j])

print(tab)
print(new_tab)

for i in range(len(new_tab)):
    for j in range(len(new_tab)):
        if (int(str(new_tab[i])[:1]) == int(str(new_tab[j])[:1])):
            print(new_tab[i], new_tab[j],int(str(new_tab[i])[:1]),int(str(new_tab[j])[:1]),i,j)
            if new_tab[i]<new_tab[j]:
                pom=new_tab[i]
                new_tab[i]=new_tab[j]
                new_tab[j]=pom

print(new_tab)
"""
