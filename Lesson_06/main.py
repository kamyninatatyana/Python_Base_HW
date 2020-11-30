import time
from termcolor import colored, cprint
import random

# УРОК 6
# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running
# (запуск). Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
# красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго
# (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно
# осуществляться только в указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав
# экземпляр и вызвав описанный метод.
#
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить
# соответствующее сообщение и завершать скрипт.

print()
print("Task 1")
print()

duration_dict = {"red": 7, "yellow": 2, "green": 5}


def counter(duration, color):
    for k in range(duration, 0, -1):
        print(colored(duration, f"{color}"))
        time.sleep(1)
        duration -= 1


class TrafficLight:
    __color = [["red", "yellow"], ["green", "yellow"]]

    def running(self):
        for pack in self.__color:
            for color in pack:
                print(colored(f"The traffic light is {color}!", f"{color}"))
                duration = duration_dict.get(color)
                counter(duration, color)


a = TrafficLight()
a.running()


# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать
# защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * число см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т

print()
print("Task 2")
print()


class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_weight_calc(self, density, thickness):
        asphalt_weight_calc = self._length * self._width * density * thickness
        if asphalt_weight_calc > 1000:
            print(f"You'll need {asphalt_weight_calc/1000} tons of asphalt to cover the road of"
                  f" {self._length}m length and {self._width}m width.")
        else:
            print(
                f"You'll need {asphalt_weight_calc} kg of asphalt to cover the road of {self._length}m length"
                f" and {self._width}m width.")
        return asphalt_weight_calc


a = Road(5000, 20)
a.asphalt_weight_calc(25, 5)


# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position
# (должность), income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий
# элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность)
# на базе класса Worker. В классе Position реализовать методы получения полного имени сотрудника
# (get_full_name) и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы
# экземпляров).

print()
print("Task 3")
print()


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": int(wage), "bonus": int(bonus)}


class Position(Worker):

    def get_full_name(self):
        print(f"Employee: {self.name} {self.surname}")
        return

    def get_total_income(self):
        print(f"Total income: {self._income['wage'] + self._income['bonus']} RUR.")
        return


position1 = Position("Ivan", "Ivanov", "Head of the Department", 100000, 15000)
position2 = Position("Petr", "Petrov", "Economist", 50000, 5000)

position1.get_full_name()
position1.get_total_income()

position2.get_full_name()
position2.get_total_income()


# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
# is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина
# поехала, остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar,
# PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость
# автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше
# 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите
# результат. Выполните вызов методов и также покажите результат.

print()
print("Task 4")
print()


class Car:
    def __init__(self, max_speed, color, name, is_police):
        self.max_speed = max_speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        print(f"{self.color} {self.name} goes straight.")
        return

    def stop(self):
        print(f"{self.color} {self.name} has stopped.")
        return

    def turn(self, direction):
        print(f"{self.color} {self.name} turns {direction}.")
        return

    def show_speed(self, speed):
        print(f"The speed of {self.color} {self.name} is {speed} km/h.")
        return


class TownCar(Car):
    def show_speed(self, speed):
        if speed > self.max_speed:
            print("Speed limit exceeded.")
        else:
            super().show_speed(speed)


class WorkCar(Car):
    def show_speed(self, speed):
        if speed > self.max_speed:
            print("Speed limit exceeded.")
        else:
            super().show_speed(speed)


class SportCar(Car):
    pass


class PoliceCar(Car):
    def show_speed(self, speed):
        if speed > self.max_speed:
            super().show_speed(speed)
            print("Police car drives any speed it wants.")
        else:
            super().show_speed(speed)


town_car1 = TownCar(60, "White", "Ford Focus", False)
town_car1.go()
town_car1.stop()
town_car1.turn("right")
town_car1.show_speed(random.randint(1, town_car1.max_speed * 2))

print()

work_car1 = WorkCar(40, "Yellow", "Excavator", False)
work_car1.go()
work_car1.stop()
work_car1.turn("left")
work_car1.show_speed(random.randint(1, work_car1.max_speed * 2))

print()

sport_car1 = SportCar(200, "Red", "Ferrari", False)
sport_car1.go()
sport_car1.stop()
sport_car1.turn("zigzag")
sport_car1.show_speed(random.randint(1, sport_car1.max_speed * 2))

print()

police_car1 = PoliceCar(120, "White", "Lada", True)
police_car1.go()
police_car1.stop()
police_car1.turn("left")
police_car1.show_speed(random.randint(1, police_car1.max_speed * 2))

# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название)
# и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen
# (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и
# проверить, что выведет описанный метод для каждого экземпляра.

print()
print("Task 5")
print()


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Start rendering.")


class Pen(Stationery):
    def draw(self):
        cprint(f"This is a {self.title}.", "grey", "on_white")


class Pencil(Stationery):
    def draw(self):
        cprint(f"This is a {self.title}.", "blue", "on_yellow")


class Handle(Stationery):
    def draw(self):
        cprint(f"This is a {self.title}.", "green", "on_cyan")


pen1 = Pen("Pen")
pencil1 = Pencil("Pencil")
handle1 = Handle("Handle")

pen1.draw()
pencil1.draw()
handle1.draw()
