def f(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return f(x-1)+f(x-2)

n = int(input("Введите номер числа в последовательности Фибоначчи\n"))
print("Число Фибоначчи равно {0} для числа с номером {1}".format(f(n), n))

# проверить ввод!!!