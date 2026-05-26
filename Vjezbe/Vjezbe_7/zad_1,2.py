import numpy as np
import matplotlib.pyplot as plt
np.random.seed (42)
mase_ciste = np.random.normal(loc =2.06 , scale =0.05 , size =57).tolist()
mase = mase_ciste+[6.0 , 1.2 , 3.2 , 4.5 , 8.5 , 7.8 , 0.08 , 0.02]
def histogram(podaci,k):
    xmax = max(podaci)
    xmin = min(podaci)
    h = (xmax-xmin)/k
    rubovi = []
    for i in range(k+1):
        rubovi.append(xmin+i*h)
    frekvencije = []
    for i in range(k):
        donja = rubovi[i]
        gornja = rubovi[i+1]
        br=0
        for j in podaci:
            if i == k-1:
                if donja <= j <= gornja:
                    br += 1
            else:
                if donja <= j < gornja:
                    br += 1
        frekvencije.append(br)
        if i == k-1:
            print(f"[{donja:.2f}, {gornja:.2f}]:{br}")
        else:   
            print(f"[{donja:.2f}, {gornja:.2f}):{br}")    
    return rubovi,frekvencije,h
rubovi,frekvencije,h = histogram(mase_ciste, 10)
plt.bar(rubovi[:-1 ],frekvencije,width=h,align="edge",edgecolor="black")
plt.xlabel("Masa")
plt.ylabel("Frekvencija")
plt.title("Histogram za mase_ciste 1")
plt.show()
arit_sredina = np.mean(mase_ciste)
medijan = np.median(mase_ciste)
plt.figure()
frekvencije2,rubovi_hist,_ = plt.hist(mase_ciste,bins=10,edgecolor="black")
plt.axvline(arit_sredina,label="Aritmeticka sredina",color="red")
plt.axvline(medijan,label="Medijan",color="yellow")
plt.xlabel("Masa")
plt.ylabel("Frekvencija")
plt.title("Histogram mase_ciste 2")
plt.legend()
plt.show()
print("Frekvencije iz prvog zadatka:", frekvencije)
print("Frekvencije iz drugog zadatka:", frekvencije2)