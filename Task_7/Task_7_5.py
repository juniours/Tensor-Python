""" Установить через pip библиотеку numpy. С помощью этой библиотеки cоздать массив 3x3 со случайными значениями, вывести его. Транспонировать его и вывести. """

import numpy as np

a = np.random.randint(0, 10, (3, 3))
x = '\n'.join([''.join(['{:3}'.format(item) for item in row]) for row in a])

# Вывод матрицы
print("Исходная матрица 3x3:")
print(x)

a = a.transpose()
x = '\n'.join([''.join(['{:3}'.format(item) for item in row]) for row in a])

# Вывод транспонированной матрицы
print("Транспонированная матрица:")
print(x)
