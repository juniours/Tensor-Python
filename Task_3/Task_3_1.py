coord = [0,0]
print("Вы сейчас в начальной точке ", coord)
a = input("Куда движение? a - влево, d - вправо, w - наверх, s - вниз\n")
step = int(input("На сколько шагов? "))
if a == "a":
    for i in range(step):
        coord[0] -= 1
        print("Движение влево на 1")
if a == "d":
    for i in range(step):
        coord[0] += 1
        print("Движение вправо на 1")
if a == "w":
    for i in range(step):
        coord[1] += 1
        print("Движение вверх на 1")
if a == "s":
    for i in range(step):
        coord[1] -= 1
        print("Движение вниз на 1")
print("Вы в точке ", coord)
print("Движение завершено")