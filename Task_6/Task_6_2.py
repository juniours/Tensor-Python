""" Формула молекулы спирта - C2H5(OH). Из неё видно, что молекула состоит из двух атомов углерода (С), 6 атомов водорода (Н) и одного атома кислорода (О). 
    В input.txt содержится 3 натуральных числа: C, H, O – количество атомов углерода, водорода и кислорода соответственно. 
    В файл output.txt вывести максимально возможное число молекул спирта, которые могут получиться из атомов, представленных во входных данных. """

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
        print("Количество O должно быть числом")
    if (not max) and (not c) and (not h):
        if max > c:
            max = c
        if max > h:
            max = h

if not max:
    with open("output.txt", "wt") as f:
        f.write("Количество молекул спирта - "+str(max))
else:
    print("Введите значения и ")
