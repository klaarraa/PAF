import numpy as np
import matplotlib.pyplot as plt
def  jednoliko_gibanje(F,m, dt=0.01, T=10):
    a = F/m
    t = np.arange(0,T,dt)
    x=0
    v=0
    polozaj = []
    brzina = []
    akc = []
    for i in range(len(t)):
        v = v + a * dt
        x = x + v * dt
        polozaj.append(x)
        brzina.append(v)
        akc.append(a)
    plt.plot(t, polozaj)
    plt.title("Graf ovisnosti polozaja o vremenu")
    plt.xlabel("t [s]")
    plt.ylabel("x [m]")
    plt.show()
    plt.plot(t, brzina)
    plt.title("Graf ovisnosti brzine o vremenu")
    plt.xlabel("t [s]")
    plt.ylabel("v [m/s]")
    plt.show()
    plt.plot(t, akc)
    plt.title("Graf ovisnosti akceleracije o vremenu")
    plt.xlabel("t [s]")
    plt.ylabel("a [m/s^2]")
    plt.show()