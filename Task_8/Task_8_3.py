""" * Перегрузить операторы сравнения так, чтобы студенты сравнивались по количеству сданных ими дз """

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
    S1 = Student('Tom', 18, '', 'BSTU', randint(1, 10))
    S2 = Student('Jack', 19, '', 'BSTU', randint(1, 10))
    print(f"Уважаемый {S1.name}!")
    S1.turn_the_task()
    print(f"Уважаемый {S2.name}!")
    S2.turn_the_task()
    if S1.count_sub_tasks < S2.count_sub_tasks:
        print(f"{S1.name} учится лучше {S2.name}")
    elif S1.count_sub_tasks > S2.count_sub_tasks:
        print(f"{S2.name} учится лучше {S1.name}")
    else:
        print(f"{S1.name} и {S2.name} учатся одинаково")
        
    S1.get_work(S1.work)