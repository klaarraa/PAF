vrijednosti=[]
for i in range(10):
    br=float(input("Unesi broj:"))
    vrijednosti.append(br)
ukupno=sum(vrijednosti)
n=len(vrijednosti)
arit_sredina=ukupno/n
print("Aritmeticka sredina:",arit_sredina)

brojnik=sum((x-arit_sredina)**2 for x in vrijednosti)
nazivnik=n*(n-1)
stand_dev=(brojnik/nazivnik)**0.5
print("Standardna devijacija:",stand_dev)