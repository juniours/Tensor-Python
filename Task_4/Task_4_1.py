""" Сортировка списка методом пузырька """

l = []
l = input("Введите значения списка через пробел: ").split()
l = [int(i) for i in l ]
print("Сортируем")
for i in range(len(l)-1):
   for i in range(len(l)-i-1): 
        if l[i] > l[i+1]:
            l[i], l[i+1] = l[i+1], l[i]
print("Список отсортирован методом пузырька: " + str(l)[1:-1])
