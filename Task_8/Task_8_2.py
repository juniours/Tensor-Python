""" Написать класс “Student”, который наследует класс human, у которого среди прочих признаков есть “Количество сданных дз”. """

from random import randint

class Human():
    def __init__(self, name, age, work):
        self.name = name
        self.age = age
        self.work = work

    def get_work(self, work):
        if self.work == '':
            print(f"{self.name} получил работу!")

class Student(Human):
    def __init__(self, name, age, work, uni, count_sub_tasks):
        super().__init__(name, age, work)
        self.uni = uni
        self.count_sub_tasks = count_sub_tasks
    
    def turn_the_task(self):
        score = randint(1, 5)
        print(f"Вы получили {score}.")
        if score > 3:
            self.count_sub_tasks -= 1
            print("Предмет сдан!")
        else:
            print("Приходите на пересдачу")
        print(f"Осталось сдать {self.count_sub_tasks} предметов")

if __name__ == '__main__':
    Tom = Student('Tom', 18, '', 'BSTU', 1)
    Tom.turn_the_task()
    Tom.get_work(Tom.work)