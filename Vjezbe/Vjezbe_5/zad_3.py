import numpy as np
tocke = np.array([2.1,3.2,4.4,-0.1,1.2,1.8,5.6,-2.7,6.7,3.9])
br_tocaka = len(tocke)
aritm_sredina = np.mean(tocke)
print(f"Aritmeticka sredina je: {aritm_sredina}")
stand_dev = np.sqrt(np.sum((tocke-aritm_sredina)**2)/(br_tocaka*(br_tocaka-1)))
print("Standardna devijacija:",stand_dev)