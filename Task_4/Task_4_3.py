""" Заполнить два случайных набора чисел. Вывести оба набора. Указать какие элементы:
    1. входят одновременно в оба;
    2. входят только в первое, но не входят во второе;
    3. входят только во второе, но не входят в первое;
    4. входят в первое или во второе, но не в оба из них одновременно."""

from random import randint

count = randint(1, 10)
set_1 = set()
set_2 = set()
for i in range(count):
    set_1.add(randint(0,10))

count = randint(1, 10)
for i in range(count):
    set_2.add(randint(0,10))

print("Первое множество: ", str(set_1)[1:-1])
print("Второе множество: ", str(set_2)[1:-1])

if (len(set_1.intersection(set_2)) == 0):
    print("Множества не имеют общих элементов")
else:
    print("Элементы, которые входят в оба множества: ",str(set_1.intersection(set_2))[1:-1])

if (len(set_1.difference(set_2)) == 0):
    print("Все элементы первого множества входят во второе")
else:
    print("Элементы первого множества,\
        которые не входят во второе множество: ",str(set_1.difference(set_2))[1:-1])

if (len(set_2.difference(set_1)) == 0):
    print("Все элементы второго множества входят в первое")
else:
    print("Элементы второго множества,\
        которые не входят в первое множество: ",str(set_2.difference(set_1))[1:-1])

if (len(set_1.symmetric_difference(set_2)) == 0):
    print("Элементы какого-то из множеств полностью входят в другое")
else:
    print("Не совпадающие элементы множеств: ",\
          str(set_1.symmetric_difference(set_2))[1:-1])
