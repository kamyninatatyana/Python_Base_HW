from Lesson_08.My_exceptions import MyExceptionZeroDivision
from Lesson_08.Date import Date
from Lesson_08.My_exceptions import MyExceptionTypeValidation
from Lesson_08.Warehouse_main import warehouse_main
from Lesson_08.Complex_numbers import ComplexNumber
# from pprint import pprint

# УРОК 8
#
# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен
# извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу
# полученной структуры на реальных данных.

print("Task 1")

print(Date.date_to_int("10-11-2001"))
Date.date_items_validation(29, 2, 2001)

# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу
# на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна
# корректно обработать эту ситуацию и не завершиться с ошибкой.

print()
print("Task 2")


def two_numbers_division():
    while True:
        try:
            dividend = float(input("Input dividend: "))
        except ValueError as err:
            print(err)
            continue
        else:
            while True:
                try:
                    divider = float(input("Input divider (nonzero!): "))
                    if divider == 0:
                        raise MyExceptionZeroDivision("Cannot be divided by zero!")
                    else:
                        return round(dividend / divider, 2)
                except (MyExceptionZeroDivision, ValueError) as err:
                    print(err)


print(two_numbers_division())

#
# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только
# чисел. Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и
# заполнять список только числами. Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не
# остановит работу скрипта, введя, например, команду “stop”. При этом скрипт завершается, сформированный
# список с числами выводится на экран.
# Подсказка: для данного задания примем, что пользователь может вводить только числа и строки. При вводе
# пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список,
# только если введено число. Класс-исключение должен не позволить пользователю ввести текст (не число)
# и отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться.
#

print()
print("Task 3")

my_list = []

while True:
    user_input = input("Input positive integer. To finish input, type 'stop': ")
    if user_input.lower() == "stop" or user_input.lower() == "'stop'":
        break
    try:
        if not user_input.isdigit():
            raise MyExceptionTypeValidation("This is not a positive integer!")
    except MyExceptionTypeValidation as my_error:
        print(my_error)
        continue
    else:
        my_list.append(user_input)

print(my_list)

# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс
# «Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники
# (принтер, сканер, ксерокс). В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
#
# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад
# и передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц
# оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.
#
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип
# данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.
#

print()
print("Tasks 4, 5, 6")

warehouse_main()


# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте
# перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры
# класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность
# полученного результата.

print()
print("Tasks 7")

complex_number1 = ComplexNumber(3, 1)
print(f"Number 1: {complex_number1}")
complex_number2 = ComplexNumber("2", "-3")
print(f"Number 2: {complex_number2}")
complex_number3 = ComplexNumber.set_param("7 + 3i")
print(f"Number 3: {complex_number3}")
complex_number4 = ComplexNumber.set_param([5, -8])
print(f"Number 4: {complex_number4}")
complex_number5 = ComplexNumber.set_param(("-10", "-4"))
print(f"Number 5: {complex_number5}")
complex_number6 = ComplexNumber.set_param(["8", "1"])
print(f"Number 6: {complex_number6}")

complex_number_err1 = ComplexNumber.set_param([4, 5, 1])
# complex_number_err1 = ComplexNumber([4, 5, 1]) Как мне поймать такую ошибку непосредственно в классе
# ComplexNumber? Как поймать ее здесь я понимаю. Но я бы хотела сделать так, чтобы если пользователь
# неправильно передал аргументы - выдавалась ошибка и программа не падала. То есть всего была одна строка кода -
# создание объекта. И если он создан неверно - выдается ошибка. Когда я встраиваю try-except
# в конструктор - ошибка все-равно появляется. Ее можно как-то поймать не здесь, а в самом классе?

print(complex_number1 + complex_number2)
print(complex_number3 + complex_number4)
print(complex_number5 + complex_number6)

print(complex_number1 * complex_number2)
print(complex_number3 * complex_number4)
print(complex_number5 * complex_number6)
