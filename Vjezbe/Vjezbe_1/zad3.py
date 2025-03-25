def unos_broja(ime):
    broj = input(f"Unesi {ime} koordinatu: ")
    while not broj.isdigit():
        print("Ponovo unesi broj.")
        broj = input(f"Unesi {ime} koordinatu: ")
    return float(broj)

x1 = unos_broja("1. x")
y1 = unos_broja("1. y")
x2 = unos_broja("2. x")
y2 = unos_broja("2. y")

while x1 == x2:
    print("Ponovo unesi koordinate")
    x2 = unos_broja("2. x")
    y2 = unos_broja("2. y")
a = (y2 - y1) / (x2 - x1)
b = y1 - a * x1
print(f"Jednadžba pravca: y = {a}x + {b}")


   

