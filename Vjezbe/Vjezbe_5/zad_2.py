def funkcija(N):
    broj = 5
    for i in range(N):
        broj += 1.0/3.0
    for i in range(N):
        broj -= 1.0/3.0
    return broj
print("N=200 :", funkcija(200))
print("N=2000 :", funkcija(2000))
print("N=20000 :", funkcija(20000))
#Rezultat nije tocno 5 zbog akumulacije pogresaka zaokruzivanja pri uzastopnom zbrajanju i oduzimanju 1/3