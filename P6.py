print('Задача 1')
from time import sleep

class TrafficLight:
    __color = {'Red': 7, 'Yellow': 2, 'Green': 2}

    def running(self):
        check=[]
        for color, t in self.__color.items():
            print(color)
            sleep(t)
            check.append(color)
        print(check)
        if check == ['Red', 'Yellow', 'Green']:
            print('Все ок')
        else:
            print('Светофор работает через жопу')
trafficLight = TrafficLight()
trafficLight.running()

print('Задача 2')
class Road:
    __len = None
    __wid = None

    def __init__(self, length, width):
        self.len = length
        self.wid = width

    def calc(self, wth, den):
        self.wth = wth
        self.den = den
        calc = self.len * self.wid * self.wth * self.den
        print('Нужно, кг: ', calc)

road1 = Road(20000, 6)
road1.calc(20, 20)

print('Задача 3')

class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')


worker1 = Position('Lena', 'Zaharova', 'TOP', 1000000, 3000)
print(worker1.get_full_name())
print(worker1.position)
print(worker1.get_total_income())


print('Задача 4')

import random

class Cars:
    name = None
    speed = None
    color = None
    is_police = False

    def __init__(self, name, speed, color, is_police = False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police


    def go(self):
        print('Машина едет')

    def stop(self):
        print('Машина повернула')

    def turn(self):
        print(random.choice(['Направо', 'Налево']))

    def show_speed(self):
        print('Скорость', self.speed)

class TownCar(Cars):
    cargo = 10
    def __init__(self, name, speed, color, cargo):
        super().__init__(name, speed, color)
        self.cargo = cargo

    def show_speed(self):
        self.speed = random.randint(0, 100)
        if self.speed>60:
            print('Превышаешь скорость, безответственный ты человек', self.speed)
        else:
            print('Умничка, ездишь правильно', self.speed)

class SportCar(Cars):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color)


class WorkCar(Cars):
    def __init__(self, name, speed, color, cargo):
        super().__init__(name, speed, color)
        self.cargo = cargo

    def show_speed(self):
        self.speed = random.randint(0, 100)
        if self.speed > 40:
            print('Превышаешь скорость, безответственный ты человек', self.speed)
        else:
            print('Умничка, ездишь правильно', self.speed)


class PoliceCar(Cars):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color, True)

car1 = Cars('Машина1', 60, 'В горошек')
print(car1.name, car1.speed, car1.color, car1.is_police)
print(car1.show_speed())
town_car1 = TownCar('Городская_машина1', 100, 'Зеленый', 30)
print(town_car1.name, town_car1.speed, town_car1.color, town_car1.cargo, town_car1.is_police)
print(town_car1.show_speed())
work_car1 = WorkCar('Рабочая_машина1', 100, 'Розовые стразики', 30)
print(work_car1.name, work_car1.speed, work_car1.color, work_car1.cargo, work_car1.is_police)
print(work_car1.show_speed())


print('Задача 5')

class Stationery:
    title = 'Name'
    def draw(self):
        print('Отрисовка')
class Pen(Stationery):
    def draw(self):
        print('Ручка')
class Pencil(Stationery):
    def draw(self):
        print('Карандаш')
class Handle(Stationery):
    def draw(self):
        print('Маркер')

my_pen = Pen()
my_pencil = Pencil()
my_handle = Handle()
my_pen.draw()
my_pencil.draw()
my_handle.draw()
