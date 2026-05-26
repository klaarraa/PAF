import numpy as np
np.random.seed (42)
mase_ciste = np.random.normal(loc =2.06 , scale =0.05 , size =57).tolist()
mase = mase_ciste+[6.0 , 1.2 , 3.2 , 4.5 , 8.5 , 7.8 , 0.08 , 0.02]
a = [3 , 1 , 4 , 1 , 5 , 9 , 2 , 6]
b = [3 , 1 , 4 , 1 , 5 , 9 , 2 , 6 , 5]
def medijan(podaci):
    lista = sorted(podaci)
    n = len(lista)
    if n%2 != 0:
        x = (n+1)//2
        return lista[x-1]
    else:
        x1 = n//2
        x2 = (n//2)+1
        return (lista[x1-1] + lista[x2-1])/2    
print("Medijan liste a =",medijan(a))
print("Medijan liste b =",medijan(b))
print("Medijan mase =",medijan(mase))
print("Numpy medijan liste a =",np.median(a))
print("Numpy medijan liste b =",np.median(b))
print("Numpy medijan mase =",np.median(mase))