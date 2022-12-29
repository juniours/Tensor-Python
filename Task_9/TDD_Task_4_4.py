""" !!! Создание по принципу TDD !!!
    Создать игровой инвентарь. Должна быть возможность добавлять в него предметы и удалять предметы из него. 
    Инвентарь должен быть ограничен по весу, каждый предмет имеет свой вес. 
    Вывод предметов должен быть с названием предмета и его весом. """

inventory = {}
things = {
    "sword": 14,
    "hammer": 20,
    "shield": 25,
    "kettle": 12,
    "horse": 600
}

def add_item(dict, dict_things, name_item):
    weight = 0
    max_weight = 100
    for key, value in dict.items():
        weight += value
    if (weight + dict_things[name_item]) <= max_weight:
        dict[name_item] = dict_things[name_item]
        return True
    else: 
        print("У предмета слишком большой вес")
        return False

def del_item(dict, name_item):
    weight = 0
    if name_item in dict:
        print("Предмет {0} с весом {1} удалён".format(name_item, dict[name_item]))
        dict.pop(name_item)
        return True  
    else:
        return False

def watch(dict):
    print("Ваш инвентарь")
    for key, value in dict.items():
        print("{0}: {1}".format(key, value))


print("У Вас есть сундук с игровым инвентарём. Вы можете добавлять в него предметы и\
    удалять их. Общий вес сундука должен быть не больше 100.\n\
    Используйте его с умом.")
add_item(inventory, things, "sword")
add_item(inventory, things, "shield")
add_item(inventory, things, "horse")
del_item(inventory, "shield")
watch(inventory)
