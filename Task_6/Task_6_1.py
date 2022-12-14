""" Написать функцию преобразующую список строк, в список байт кодов. Написать обратную функцию. """

def bcode(l):
    """ Перевод строк в байтовые строки.
    Принимает:
        l - список строк.
    """
    for i in range(len(l)):
        try:
            l[i] = l[i].encode('utf-8')
        except AttributeError:
            l[i] = str(l[i])
            l[i] = l[i].encode('utf-8')
    return l

def strcode(b):
    """ Перевод байтовых строк в обычные.
    Принимает:
        b - список байтовых строк.
    """
    for i in range(len(b)):
        b[i] = b[i].decode('utf-8')
    return b


list_s = ['hello', '1', 45, 'привет']
print("Исходный список элементов: ", list_s)
list_s = bcode(list_s)
print("Закодированный список элементов: ", list_s)
list_s = strcode(list_s)
print("Раскодированный список строк: ", list_s)
