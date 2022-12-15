def check_passwd(p):
    if len(p) >= 6 and not p.isdigit() and not p.isalpha() and not p.isspace():
        if p.find('password') == -1 and p.find('PASSWORD') == -1 and p.find('Password') == -1:
            return True
    else: return False


passwd = input("Введите пароль.\n\
Он должен быть из 6 и более символов и содержать хотя бы одну цифру\n")
if not check_passwd(passwd):
    print("Ошибка")

# обработать ввод и исключения
# обработать ситуацию, когда в пароле есть пробел