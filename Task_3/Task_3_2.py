coord = [0,0]
print("Вы сейчас в начальной точке ", coord)
a = input("Куда движение? a - влево, d - вправо, w - наверх, s - вниз\n\
    Стоп-слово - стоп\n")
while a != "стоп":
    step = int(input("На сколько шагов? "))
    if a == "a": coord[0] -= step
    if a == "d": coord[0] += step
    if a == "w": coord[1] += step
    if a == "s": coord[1] -= step
    print("Вы в точке ", coord)
    a = input("Куда движение? a - влево, d - вправо, w - наверх, s - вниз\n\
    Стоп-слово - стоп\n")
print("Движение завершено")