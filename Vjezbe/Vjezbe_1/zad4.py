def jednadzba_pravca(x1, y1, x2, y2):
    a=((y2-y1)/(x2-x1))
    b = (y1 - a*x1)
    print(f"Jednadzba pravca: y={a}x + {b}")
x1=float(input("Unesi 1. x koordinatu"))
y1=float(input("Unesi 1. y koordinatu"))
x2=float(input("Unesi 2. x koordinatu"))
y2=float(input("Unesi 2. y koordinatu"))

jednadzba_pravca(x1, y1, x2, y2)