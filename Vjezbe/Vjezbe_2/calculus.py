import numpy as np
def prva_metoda(f,x,h=0.00001,metoda="three-step"):
    if metoda == "three-step":
        return (f(x+h)-f(x-h))/(2*h)
    elif metoda == "two-step":
        return (f(x+h)-f(x))/h
    
def druga_metoda(f,a,b,h=0.00001,metoda="three-step"):
    x = np.linspace(a,b,100)
    y = []
    for i in x:
        y.append(prva_metoda(f,i,h=h,metoda=metoda))
    return x,y

def pravokutna_metoda(f,c,d,n):
    donja = 0
    gornja = 0
    if n <= 0:
        print("n mora biti pozitivan")
        return None
    if c > d:
        print("c mora biti manji od d")
        return None
    h = (d-c)/n
    for i in range(n):
        x_lijevo = c+i*h
        x_desno = c+(i+1)*h
        f1 = f(x_lijevo)
        f2 = f(x_desno)
        donja += min(f1,f2)*h
        gornja += max(f1,f2)*h
    return donja,gornja

def trapezna_metoda(f,c,d,n):
    suma = 0
    if n <= 0:
        print("n mora biti pozitivan")
        return None
    if c > d:
        print("c mora biti manji od d")
        return None
    h = (d-c)/n
    for i in range(n):
        x_lijevo = c+i*h
        x_desno = c+(i+1)*h
        suma += (f(x_lijevo)+f(x_desno))/2*h
    return suma