import numpy as np

def derivacija_u_tocki(f, x, h=0.00001, metoda='three-step'):
    if metoda == 'two-step':
        return (f(x + h)-f(x))/h
    else:
        return (f(x+h)-f(x-h))/(2*h)

def derivacija_na_rasponu(f, a, b, broj_tocaka=100, h=0.00001, metoda='three-step'):
    x_vals = np.linspace(a, b, broj_tocaka)
    derivacije = [(x, derivacija_u_tocki(f, x, h, metoda)) for x in x_vals]
    return derivacije

def pravokutna_aproksimacija(f, a, b, n):
    dx = (b-a)/n
    x = np.linspace(a, b - dx, n)
    donja_suma = np.sum(np.minimum(f(x), f(x + dx)))*dx
    gornja_suma = np.sum(np.maximum(f(x), f(x + dx)))*dx
    return donja_suma, gornja_suma

def trapezna_integracija(f, a, b, n):
    x = np.linspace(a, b, n + 1)
    y = f(x)
    dx = (b-a)/n
    return (dx/2)*np.sum(y[:-1] + y[1:])
