with open("input.txt") as f:
    c, h, o = f.read().split()
    try:
        c = int(float(c)/2)
    except ValueError:
        print("Количество С должно быть числом")
    try:
        h = int(float(h)/6)
    except ValueError:
        print("Количество H должно быть числом")
    try:
        max = int(float(o))
    except ValueError:
        print("Количество С должно быть числом")
    if not max and not c and not h:
        if max > c: max = c
        if max > h: max = h

if not max:
    with open("output.txt", "wt") as f:
        f.write("Количество молекул спирта - "+str(max))
else: print("Введите значения и ")
