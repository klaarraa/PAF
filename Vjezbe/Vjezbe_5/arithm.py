tocke = [2.1,3.2,4.4,-0.1,1.2,1.8,5.6,-2.7,6.7,3.9]
br_tocaka = len(tocke)
zbroj = sum(tocke)
aritm_sredina = zbroj/br_tocaka
print(f"Aritmeticka sredina je: {aritm_sredina}")
stand_dev = (sum((i-aritm_sredina)**2 for i in tocke)/(br_tocaka*(br_tocaka-1)))**0.5
print("Standardna devijacija:",stand_dev)