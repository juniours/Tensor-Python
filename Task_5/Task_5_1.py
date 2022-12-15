def check_passwd(p):
    if len(p) >= 6 and not p.isdigit() and not p.isalpha() and not p.isspace()\
        and p.find('password') == -1 and p.find('PASSWORD') == -1 and p.find('Password') == -1\
        and not (' ' in p) and any(n.isdigit() for n in p):
            return True
    else: return False


passwd = input("Введите пароль.\n\
Он должен быть из 6 и более символов и содержать хотя бы одну цифру\n")
while not check_passwd(passwd):
    print("Пароль был введён с ошибкой")
    passwd = input("Введите новый пароль\n")
print("Поздравляем! Пароль установлен!")