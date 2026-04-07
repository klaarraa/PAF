import matplotlib.pyplot as plt
import numpy as np
import calculus
def kubna(x):
    return 0.5*x**3

def kubna_deriv(x):
    return 1.5*x**2

def trig(x):
    return np.sin(x)

def trig_deriv(x):
    return np.cos(x)

x,y1 = calculus.druga_metoda(kubna,-3,3,h=0.001,metoda="three-step")
x,y2 = calculus.druga_metoda(kubna,-3,3,h=0.3,metoda="two-step")
x,y3 = calculus.druga_metoda(kubna,-3,3,h=0.9,metoda="three-step")
y_analiticki=[]
for i in x:
    y_analiticki.append(kubna_deriv(i))
plt.plot(x, y_analiticki, label="Analiticka 1.5*x**2")
plt.plot(x, y1, label="Numericka h=0.001, three-step")
plt.plot(x, y2, label="Numericka h=0.3,two-step")
plt.plot(x, y3, label="Numericka h=0.9,three-step")
plt.title("Kubna funkcija")
plt.legend()
plt.tight_layout()
plt.grid()
plt.show()
x,y1 = calculus.druga_metoda(trig,-3,3,h=0.001,metoda="three-step")
x,y2 = calculus.druga_metoda(trig,-3,3,h=0.3,metoda="two-step")
x,y3 = calculus.druga_metoda(trig,-3,3,h=0.9,metoda="three-step")
y_analiticki=[]
for i in x:
    y_analiticki.append(trig_deriv(i))
plt.plot(x, y_analiticki, label="Analiticka cos(x)")
plt.plot(x, y1, label="Numericka h=0.001, three-step")
plt.plot(x, y2, label="Numericka h=0.3,two-step")
plt.plot(x, y3, label="Numericka h=0.9,three-step")
plt.title("Trigonometrijska funkcija")
plt.legend()
plt.tight_layout()
plt.grid()
plt.show()
def f(x):
    return x**2

def integral_f(x):
    return (x**3)/3
c = 0
x = np.linspace(0,3,100)
y_analiticki = []
for i in x:
    y_analiticki.append(integral_f(i)-integral_f(c))

y_donja_10 = []
y_gornja_10 = []
y_donja_50 = []
y_gornja_50 = []
for i in x:
    donja, gornja = calculus.pravokutna_metoda(f,c,i,10)
    y_donja_10.append(donja)
    y_gornja_10.append(gornja)
    donja, gornja = calculus.pravokutna_metoda(f,c,i,100)
    y_donja_50.append(donja)
    y_gornja_50.append(gornja)
y_trapez_10 = []
y_trapez_50 = []
for i in x:
    y_trapez_10.append(calculus.trapezna_metoda(f,c,i,10))
    y_trapez_50.append(calculus.trapezna_metoda(f,c,i,100))
plt.plot(x, y_analiticki, label="Analiticko rjesenje")
plt.plot(x, y_donja_10, label="Pravokutna donja, n=10")
plt.plot(x, y_gornja_10, label="Pravokutna gornja, n=10")
plt.plot(x, y_donja_50, label="Pravokutna donja, n=50")
plt.plot(x, y_gornja_50, label="Pravokutna gornja, n=50")
plt.plot(x, y_trapez_10, label="Trapezna, n=10")
plt.plot(x, y_trapez_50, label="Trapezna, n=50")
plt.title("Analiticko i numericko rjesenje integrala")
plt.legend()
plt.grid()
plt.show()