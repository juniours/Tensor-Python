max_weight = 100
weight = 0
inventory = {}

def add_item(dict):
    name_item = input("Введите название предмета ")
    weight_item = int(input("Введите вес предмета "))
    global weight
    for key, value in dict.items():
        weight += value
    if (weight+weight_item) <= max_weight:
        dict[name_item] = weight_item
    else: print("У предмета слишком большой вес")

def del_item(dict):
    name_item = input("Какой предмет Вы хотите удалить? ")
    print("Предмет {0} с весом {1} удалён".format(name_item, dict[name_item]))
    dict.pop(name_item)

def watch(dict):
    print("Ваш инвентарь")
    for key, value in dict.items():
        print("{0}: {1}".format(key, value))


print("У Вас есть сундук с игровым инвентарём. Вы можете добавлять в него предметы и\
    удалять их. Общий вес сундука должен быть не больше 100.\n\
    Используйте его с умом.")
act = input("Добавить элемент - команда 'добавить'\n\
    Удалить элемент - команда 'удалить'\n\
    Посмотреть инвентарь - команда 'посмотреть'\n\
    Посмотреть команды - команда 'команды'\n\
    Остановить игру - команда 'стоп'\n")
while act != 'стоп':
    if act == 'добавить': add_item(inventory)
    if act == 'удалить': del_item(inventory)
    if act == 'посмотреть': watch(inventory)
    if act == 'команды': print("Добавить элемент - команда 'добавить'\n\
    Удалить элемент - команда 'удалить'\n\
    Посмотреть инвентарь - команда 'посмотреть'\n\
    Посмотреть команды - команда 'команды'\n\
    Остановить игру - команда 'стоп'")
    act = input("Введите следующую команду\n")