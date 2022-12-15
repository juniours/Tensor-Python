def avg(*items):
    sum = items[0]
    for i in items:
        if i != items[0]:
            sum += i
    return sum

print("Сумма элементов равна {}".format(avg("qwe","12")))

# проверка, чтобы все элементы были одного типа. мб можно в функции так не колхозить