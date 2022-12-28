""" !!! Версия без пользовательского ввода !!!
    Написать функцию, принимающую строку-пароль. Функция должна проверить подходит ли этот пароль условиям и вернуть True - если подходит; False - если не подходит. 
    Условия:
         - Должен быть не менее 6 символов;
         - Должен содержать хотя бы одну цифру;
         - Не должен состоять только из цифр;
         - Не должен содержать слово “password” в любом регистре.
"""


def check_passwd(p):
    if len(p) >= 6 and not p.isdigit() and not p.isalpha() and not p.isspace()\
        and (p.lower().find('password') == -1)\
        and not (' ' in p) and any(n.isdigit() for n in p):
            return True
    else: return False


if check_passwd("passwd"):
    print("Пароль был введён с ошибкой")
else:
    print("Поздравляем! Пароль установлен!")
