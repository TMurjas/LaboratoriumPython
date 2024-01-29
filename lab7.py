import pandas as pd

data = {
'nr_albumu':["w12345","w32145","w12645","w41332"],
'Imię': ['Anna', 'Jan', 'Katarzyna', 'Tomasz'],
'Nazwisko': ['abc', 'cda', 'war', 'Mur'],
'Wiek': [22, 21, 24, 35],
'Ocena': [3.0, 3.0, 5.0, 4.0]}

df = pd.DataFrame(data)

print(df)
print("\n")
print(df[df["Ocena"]>4])
print("\n")
print(df.query("Ocena >4"))
print("\n")
for row in df.itertuples():
    if row.Ocena>4.0:
        print(row.Ocena,row.Imię)

print("\n")
print(df.sort_values("Wiek"))
print("\n")
print(df.groupby("Ocena").get_group(4))
print("\n")
print(df.groupby("Ocena").get_group(3))
print("\n")
print(df.groupby("Ocena")["Wiek"].mean())

datapop = {
'nr_albumu':["w12645","w32145"],
'Imię': ['Katarzyna', 'Jan'],
'Nazwisko': ['abc', 'cda',],
'Ocena': [4.0, 5.0]}
dfpop = pd.DataFrame(datapop)
print(dfpop)

print(pd.merge(df,dfpop,on='nr_albumu',how='outer'))
df.to_csv("data.csv")

new_data=pd.read_csv("data.csv")
print("\n")
print(new_data)
print("\n")
lisdfst_row = {"nr_albumu":"w42345",'Wiek':45, 'Imię':"ads", 'Nazwisko':'ddds', 'Ocena':5}
new_data.loc[len(new_data)] = lisdfst_row
print(new_data)
print("\n")

for i in range(3,5):
    if len(df.groupby("Ocena").get_group(i)) == 1:
        print(df.groupby("Ocena").get_group(i))

print("\n")

ile=0
for index, row in new_data.iterrows():
    if row["Ocena"]==5:
        ile+=1

print("ile studentów ma ocenę równą 5:",ile)