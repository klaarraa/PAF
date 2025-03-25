import matplotlib.pyplot as plt
import numpy as np
def unos_broja(ime):
    broj = input(f"Unesi {ime} koordinatu: ")
    while not broj.isdigit():
        print("Unesi ponovo broj.")
        broj = input(f"Unesi {ime} koordinatu: ")
    return float(broj)

def jednadžba_pravca(x1, y1, x2, y2, spremi=False, ime_grafa="graf.pdf"):
    a = (y2 - y1) / (x2 - x1)
    b = y1 - a * x1
    print(f"Jednadžba pravca: y = {a:.2f}x + {b:.2f}")
    x_vals = np.linspace(x1 - 2, x2 + 2, 100)
    plt.plot(x_vals, a*x_vals + b, 'b-', label=f"y = {a:.2f}x + {b:.2f}")
    plt.scatter([x1, x2], [y1, y2], color='red', label="Točke")
    plt.legend()
    plt.grid()
    if spremi:
        plt.savefig(ime_grafa)
        print(f"Graf spremljen kao '{ime_grafa}'.")
    else:
        plt.show()

x1 = unos_broja("1. x")
y1 = unos_broja("1. y")
x2 = unos_broja("2. x")
y2 = unos_broja("2. y")

while x1 == x2:
    print("Ponovo unesi koordinate")
    x2, y2 = unos_broja("2. x"), unos_broja("2. y")
    
odabir = input("Prikaz (P) ili spremanje PDF (S)? ")
if odabir == "S":
    ime_grafa = input("Unesite ime PDF-a: ").strip() + ".pdf"
    jednadžba_pravca(x1, y1, x2, y2, spremi=True, ime_grafa=ime_grafa)
else:
    jednadžba_pravca(x1, y1, x2, y2)