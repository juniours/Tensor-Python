a = float(input("Введите коэффициент a\n"))
b = float(input("Введите коэффициент b\n"))
c = float(input("Введите коэффициент c\n"))
print("Решим уравнение: {:-.2f}*z^2{:+.2f}*z{:+.2f} = 0".format(a,b,c))
D = b ** 2 - 4*a*c
if D > 0: 
    z1 = (-b+D)/(2*a)
    z2 = (-b-D)/(2*a)
    print("Корни %.2f" % z1, ", %.2f" % z2)
if D == 0:
    z = -b/(2*a)
    print("Корень %.2f" % z)
if D < 0:
    print("Корней нет")