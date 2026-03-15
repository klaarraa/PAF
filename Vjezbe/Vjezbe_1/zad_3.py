x1 = input("Unesi x1: ")
while not x1.replace(".","",1).isdigit():
    print("Ponovi unos")
    x1 = input("Unesi x1: ")

y1 = input("Unesi y1: ")
while not y1.replace(".","",1).isdigit():
    print("Ponovi unos")
    y1 = input("Unesi y1: ")

x2 = input("Unesi x2: ")
while not x2.replace(".","",1).isdigit():
    print("Ponovi unos")
    x2 = input("Unesi x2: ")

y2 = input("Unesi y2: ")
while not y2.replace(".","",1).isdigit():
    print("Ponovi unos")
    y2 = input("Unesi y2: ") 

x1 = float(x1)
y1 = float(y1)
x2 = float(x2)
y2 = float(y2)

if x1 == x2:
    print(f"Jednadzba pravca je x={x1}")
else:
    k = (y2 - y1)/(x2 - x1)
    b = y1 - k * x1
    print(f"Jednadžba pravca je: y = {k}x +{b}")