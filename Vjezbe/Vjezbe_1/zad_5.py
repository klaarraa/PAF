import matplotlib.pyplot as plt
import numpy as np
def koordinate(x1,y1, x2, y2):
    x_tocke = [x1, x2]
    y_tocke = [y1, y2]
    if x1 == x2:
        print(f"Jednadzba pravca je x={x1}")
        x = [x1, x2]
        y = [y1, y2]
        
    else:
        k = (y2 - y1)/(x2 - x1)
        b = y1 - k * x1
        print(f"Jednadžba pravca je y = {k}x + {b}")
        x = np.linspace(x1,x2,100)
        y = k*x + b

    plt.plot(x,y)
    plt.scatter(x_tocke,y_tocke)
    plt.xlabel("x os")
    plt.ylabel("y os")
    plt.title("Graf ovisnosti funkcije y o varijabli x")
    prikaz = input("Zelis li prikaz grafa ili ga spremit kao pdf?")
    if prikaz == "prikaz":
        plt.show()
    elif prikaz == "pdf":
        ime = input("Unesi ime pod kojime zelis spremiti graf: ")
        plt.savefig(ime)

x_1 = float(input("Unesi x1: "))
y_1 = float(input("Unesi y1: "))
x_2 = float(input("Unesi x2: "))
y_2 = float(input("Unesi y2: "))

koordinate(x_1, y_1, x_2, y_2)