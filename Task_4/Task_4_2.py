print("Для остановки напишите 'стоп'")
colours = {}
c_name = input("Введите название цвета ")
while c_name != 'стоп':
    c_rgb = tuple(input("Какой у него цвет в RGB? Введите три числа через пробел").split())
    colours[c_name] = c_rgb
    c_name = input("Введите название цвета ")
for key, value in colours.items():
    print("{0}: {1}".format(key, value))