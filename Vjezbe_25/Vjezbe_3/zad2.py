def funkcija(N):
    a = 5.0
    for _ in range(N):
        a += 1/3
    for _ in range(N):
        a -= 1/3
    return a
print("N=200 :", funkcija(200))
print("N=2000 :", funkcija(2000))
print("N=20000 :", funkcija(20000))
#razlomak 1/3 ima beskonacno decimala pa se u memoriji zapisuje kao aproksimacija zbog cega se akumuliraju pogreske i konacan rezultat odstupa od ocekivanog