""" !!! Версия без пользовательского ввода !!!
    Написать функцию, принимающую сколько угодно параметров (в том числе и 0) и возвращающую их сумму. 
"""

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
