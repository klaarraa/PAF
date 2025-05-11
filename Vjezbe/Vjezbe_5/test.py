import numpy as np
import matplotlib.pyplot as plt
from calculus import (
    derivacija_u_tocki,
    derivacija_na_rasponu,
    pravokutna_aproksimacija,
    trapezna_integracija
)
def kubna(x): return x**3
def trigonom(x): return np.sin(x)

def deriv_kubna(x): return 3*x**2
def deriv_trigonom(x): return np.cos(x)

rezultat_kubna = derivacija_na_rasponu(kubna, -2, 2, broj_tocaka=100, h=0.0001, metoda='three-step')
x_kubna = [x for x, d in rezultat_kubna]
y_kubna = [d for x, d in rezultat_kubna]
rezultat_trig = derivacija_na_rasponu(trigonom, 0, 2*np.pi, broj_tocaka=100, h=0.0001, metoda='two-step')
x_trig = [x for x, d in rezultat_trig]
y_trig = [d for x, d in rezultat_trig]

plt.figure(figsize=(10, 5))
plt.plot(x_kubna, deriv_kubna(np.array(x_kubna)), label='Analitička derivacija x^3')
plt.plot(x_kubna, y_kubna, 'o', label='Numerička derivacija x^3 (three-step)', markersize=3)

plt.plot(x_trig, deriv_trigonom(np.array(x_trig)), label='Analitička derivacija sin(x)')
plt.plot(x_trig, y_trig, 'o', label='Numerička derivacija sin(x) (two-step)', markersize=3)

plt.title("Usporedba analitičke i numeričke derivacije")
plt.xlabel("x")
plt.ylabel("f'(x)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

def kvadratna(x): return x**2

a, b = 0, 3
analiticki_integral = (b**3 - a**3)/3

broj_podjela_lista = [5, 10, 50, 100]
donje_međe = []
gornje_međe = []
trapezni_rezultati = []

for n in broj_podjela_lista:
    donja, gornja = pravokutna_aproksimacija(kvadratna, a, b, n)
    trapezna = trapezna_integracija(kvadratna, a, b, n)
    donje_međe.append(donja)
    gornje_međe.append(gornja)
    trapezni_rezultati.append(trapezna)

plt.figure(figsize=(8, 5))
plt.plot(broj_podjela_lista, donje_međe, 'bo-', label='Donja među (pravokutna)')
plt.plot(broj_podjela_lista, gornje_međe, 'ro-', label='Gornja među (pravokutna)')
plt.plot(broj_podjela_lista, trapezni_rezultati, 'go-', label='Trapezna metoda')
plt.axhline(analiticki_integral, color='k', linestyle='--', label='Analitička vrijednost')

plt.title("Numerička vs. analitička integracija (x^2)")
plt.xlabel("Broj podjela")
plt.ylabel("Vrijednost integrala")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()



