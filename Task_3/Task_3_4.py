import math as m

a = complex(input("Введите коэффициент a\n"))
b = complex(input("Введите коэффициент b\n"))
c = complex(input("Введите коэффициент c\n"))
print("Решим уравнение: {:-.2f}*z^2{:+.2f}*z{:+.2f} = 0".format(a,b,c))
D = b ** 2 - 4*a*c
print(D)
if D.imag == 0:
    if D.real > 0:
        z1 = complex((-b.real+m.sqrt(D.real))/(2*a), -b.imag/(2*a))
        z2 = complex((-b.real-m.sqrt(D.real))/(2*a), -b.imag/(2*a))
        if z2.imag == 0 or z1.imag == 0:
            print("Корни {:.2f}, {:.2f}".format(z1.real, z2.real))
        else:
            print("Корни {:.2f}{:+.2f}j, {:.2f}{:+.2f}j".format(z1.real,\
            z1.imag, z2.real, z2.imag))
    if D.real == 0:
        x = -b/(2*a)
        print("Корень %.2f" % x)
    if D.real < 0:
        z1 = complex((-b.real+m.sqrt(-D.real))/(2*a), -b.imag/(2*a))
        z2 = complex((-b.real-m.sqrt(-D.real))/(2*a), -b.imag/(2*a))
        print("Корни {:.2f}{:+.2f}j, {:.2f}{:+.2f}j".format(z1.real,\
            z1.imag, z2.real, z2.imag))
else:
    print(round(D.imag))
    for i in range(round(m.sqrt(abs(round(D.imag))))):
        if i != 0 and int((D.imag)/2) % i == 0:
            b1 = i ** 2 - D.real
            if int((D.imag)/2) % m.sqrt(b1) == 0:
                a1 = i
                b2 = m.sqrt(b1)
                if D.imag < 0:
                    b2 *= -1
                break
    print("D =  {:.2f}{:+.2f}j".format(a1, b2))
    z1 = complex((-b.real+a1)/(2*a), (-b.imag + b2)/(2*a))
    z2 = complex((-b.real-a1)/(2*a), (-b.imag - b2)/(2*a))
    print("Корни {:.2f}{:+.2f}j, {:.2f}{:+.2f}j".format(z1.real,\
            z1.imag, z2.real, z2.imag))
