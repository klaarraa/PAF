import numpy as np
malo_n = [99.8, 100.1, 99.9, 100.2, 100.0]
np.random.seed(42)
veliko_n = np.random.normal(loc=100.0, scale=0.2, size=10000).tolist()
def devijacije(lista):
    n = len(lista)
    x_sred = sum(lista)/n
    sigma_n = np.sqrt(sum((x-x_sred)**2 for x in lista)/n)
    s = np.sqrt(sum((x-x_sred)**2 for x in lista)/(n-1))
    sigma_x = s/np.sqrt(n)
    return x_sred,sigma_n,s,sigma_x

x_sred,sigma_n,s,sigma_x = devijacije(malo_n)
print(f"malo_n: x_sred: {x_sred}, sigma_n: {sigma_n}, s: {s}, sigma_x: {sigma_x}")
x_sred,sigma_n,s,sigma_x = devijacije(veliko_n)
print(f"veliko_n: x_sred: {x_sred}, sigma_n: {sigma_n}, s: {s}, sigma_x: {sigma_x}")
#a) Kako se mijenja s kada povećamo broj mjerenja, a kako σx¯? S ostaje priblizno isti jer opisuje rasprsenost podataka, a sigmax se smanjuje
#b)  Kolika je relativna razlika između σn i s za mali, a kolika za veliki skup? Za mali skup podataka razlika je veca jer razlika izmedu dijeljenja s n i n-1 postaje znacajna
#c) np.std() po defaultu dijeli s n, kada je to ispravno koristiti? Kad analiziramo cijeli skup podataka, a ne samo neki uzorak