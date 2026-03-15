import numpy as np
vrijednosti=[]
for i in range(10):
    br=float(input("Unesi broj: "))
    vrijednosti.append(br)
x = np.array(vrijednosti)
n = len(x)

arit_sr= np.mean(x)
print("Aritmeticka sredina:",arit_sr)
brojnik = np.sum((x - arit_sr) ** 2)
stand_dev = np.sqrt(brojnik/(n * (n - 1)))
print("Standardna devijacija:",stand_dev)