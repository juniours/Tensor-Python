def avg(*items):
    sum = items[0]
    for i in items:
        if i != items[0]:
            try:
                sum += i
            except TypeError:
                print("Типы аргументов не совпадают")
    return sum

print("Сумма элементов равна {}".format(avg("qwerty", 123)))