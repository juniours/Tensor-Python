""" Написать класс “animals” (животные), который включает общие признаки и поведения животных. 
    От “animals” наследовать класс “mammals” (млекопитающие), который включает общие признаки и поведения млекопитающих. 
    От “mammals” наследовать “human” (человек), “cat”(кот), “dog”(собака), у каждого свои признаки и поведения"""


class Animals:
    def __init__(self, title, age):
        self.title = title
        self.age = age
    
    def give_brith(self):
        print(f"Был рождён новый {self.title}! Не забудьте его покормить")


class Mammals(Animals):
    def __init__(self, title, age):
        super().__init__(title, age)

    def give_milk(self):
        print("Ребёнок покормлен")

    def give_brith(self):
        print(f"Рожден новый {self.title}. Покормите его скорее!")
        self.give_milk()

class Human(Mammals):
    def __init__(self, title, age, name, gender, work):
        super().__init__(title, age)
        self.name = name
        self.gender = gender
        self.work = work

    def get_work(self, work):
        if self.work == '':
            print(f"{self.name} получил работу!")

    def give_brith(self, gender):
        if self.gender == 'woman':
            print(f"Рожден новый {self.title}. Покормите его скорее!")
            self.give_milk()

class Cat(Mammals):
    def __init__(self, title, age, name, breed):
        super().__init__(title, age)
        self.name = name
        self.breed = breed

    def say(self, str):
        if str.lower().find('meow') or str.lower().find('мяу'):
            print(f"{self.name} издала звук ", str)
        else:
            print("Кошки умеют только мяукать")

class Dog(Mammals):
    def __init__(self, title, age, name, breed):
        super().__init__(title, age)
        self.name = name
        self.breed = breed
    
    def guard(self):
        print("Вас охраняют")
    
    def rest(self):
        print(f"{self.name} отдыхает")


Anna = Human('homo_sapiense', 32, 'Anna', 'woman', 'worker')
Anna.give_brith(Anna.gender)
Tom = Human('homo_sapiense', 35, 'Tom', 'man', '')
Tom.get_work(Tom.work)
Bead = Cat('cat', 2, 'Бусинка', 'Мей-кун')
Bead.say("meow мяу")
Jack = Dog('dog', 5, 'Jack', 'немецкая овчарка')
Jack.guard()
Jack.rest()
