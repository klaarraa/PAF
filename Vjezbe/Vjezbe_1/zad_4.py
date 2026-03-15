def koordinate(x1,y1, x2, y2):
    if x1 == x2:
        print(f"Jednadzba pravca je x={x1}")
    else:
        k = (y2 - y1)/(x2 - x1)
        b = y1 - k * x1
        print(f"Jednadžba pravca je: y = {k}x + {b}")
x_1 = float(input("Unesi x1: "))
y_1 = float(input("Unesi y1: "))
x_2 = float(input("Unesi x2: "))
y_2 = float(input("Unesi y2: "))

koordinate(x_1, y_1, x_2, y_2)