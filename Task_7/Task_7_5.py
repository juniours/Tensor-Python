import numpy as np

a = np.random.randint(0, 10, (3, 3))
x = '\n'.join([''.join(['{:3}'.format(item) for item in row]) for row in a])
print("Исходная матрица 3x3:")
print(x)
a = a.transpose()
x = '\n'.join([''.join(['{:3}'.format(item) for item in row]) for row in a])
print("Транспонированная матрица:")
print(x)