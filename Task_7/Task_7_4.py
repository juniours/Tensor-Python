import os
import platform

print("Название операционной системы хоста: ", platform.system())
if os.name == 'nt':
    print("С какой платформой работает хост: Windows")
else:
    print("С какой платформой работает хост: ", os.name)
print("Пользователь, под которым реализован вход: ", os.getlogin())
print("Список файлов и директорий в папке: ", os.listdir(path='.'))