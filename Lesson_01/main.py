import datetime
import time

# Урок 1
# 1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя
# несколько чисел и строк и сохраните в переменные, выведите на экран.

print()
print("Задание 1.")

name = input("Как Вас зовут? ")
print(f"Здравствуйте,{name}!")

number_1 = float(input("Введите первое число: "))
number_2 = float(input("Введите второе число, отличное от нуля: "))

print(f"Результат деления {number_1} на {number_2} равен {number_1 / number_2:.2f}")

# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в
# формате чч:мм:сс. Используйте форматирование строк.

print()
print("Задание 2.")
user_time = int(input(f"{name}, пожалуйста, введите время в секундах и мы представим его в формате "
                      f"чч:мм:cc: "))

print("Вариант 1.")

hours = user_time // (60 ** 2)
minutes = (user_time - hours * 60 ** 2) // 60
seconds = user_time - hours * 60 ** 2 - minutes * 60

print("%02d:%02d:%02d" % (hours, minutes, seconds))
print(f"{hours:02}:{minutes:02}:{seconds:02}")

print()
print("Вариант 2.")

print(str(datetime.timedelta(seconds=user_time)))

print()
print("Вариант 3.")
print(time.strftime("%H:%M:%S", time.gmtime(user_time)))

print()
print("Вариант 4.")
minutes, seconds = divmod(user_time, 60)
hours, minutes = divmod(minutes, 60)
print("%02d:%02d:%02d" % (hours, minutes, seconds))

# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл
# число 3. Считаем 3 + 33 + 333 = 369.

print()
print("Задание 3.")

while True:
    user_number = (input(f"{name}, пожалуйста, введите любое положительное число: "))
    if int(user_number) >= 0:
        break

print(f"Сумма {user_number} + {user_number}{user_number} + {user_number}{user_number}{user_number} = "
      f"{(int(user_number) + int(user_number * 2) + int(user_number * 3))}")

# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения
# используйте цикл while и арифметические операции.

print()
print("Задание 4. Вариант 1.")

user_input = input(f"{name}, пожалуйста, введите целое положительное число и мы найдем в нем самую большую цифру: ")

i = 0
max_number = 0
while i < len(user_input):
    if int(user_input[i]) > max_number:
        max_number = int(user_input[i])
    i += 1
print("В Вашем числе максимальная цифра:", max_number)

print()
print("Задание 4. Вариант 2.")

max_number = 0
user_input = int(user_input)

while user_input != 0:
    if max_number < (user_input % 10):
        max_number = user_input % 10
        user_input = user_input // 10
    else:
        user_input = user_input // 10

print("В Вашем числе максимальная цифра:", max_number)

# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым
# результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность
# выручки (соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы и определите
# прибыль фирмы в расчете на одного сотрудника.

print()
print("Задание 5.")

revenue = int(input(f"{name}, пожалуйста, введите выручку фирмы в рублях: "))
expenses = int(input("Пожалуйста, введите издержки фирмы в рублях: "))
result = revenue - expenses
result_to_write = "убытком"
if result > 0:
    result_to_write = "прибылью"
elif result == 0:
    result_to_write = "нулевым результатом"
print("Фирма завершила период с", result_to_write, "в", result, "руб.")

if result > 0:
    print("Рентабельность по выручке за период составила: %.2f" % (result / revenue * 100), "%")
    employees_number = int(input("Пожалуйста, введите количество сотрудников: "))
    print(f"Прибыль фирмы в расчете на 1 сотрудника составила: {result / employees_number:.2f} руб.")

# 6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a
# километров. Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b
# километров. Программа должна принимать значения параметров a и b и выводить одно натуральное число
# — номер дня. Например: a = 2, b = 3. Результат: 1-й день: 2 2-й день: 2,2 3-й день: 2,42
# 4-й день: 2,66 5-й день: 2,93 6-й день: 3,22. Ответ: на 6-й день спортсмен достиг результата — не
# менее 3 км.

print()
print("Задание 6.")
print()

a = int(input(f"{name}, пожалуйста, введите, сколько км спортсмен пробежал в 1-день: "))
b = int(input("Пожалуйста, введите, протяженность финальной дистанции в км: "))
day_number = 1
print("Результат:")
print("День", day_number, ":", a, "км.")

while a < b:
    day_number += 1
    a = a * 1.1
    print("День", day_number, ": %.2f км." % a)

print("Ответ: спортсмен достиг результата на", day_number, "день.")
