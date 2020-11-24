# УРОК 3
# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

print("Задание 1.")
print()


def if_proper_arg(var):
    """ Принимает аргумент и проверяет ввод не числового значения"""

    try:
        int(var)
    except (TypeError, ValueError):
        result = False
        print(f"Значение должно быть числом!")
    else:
        result = True
    return result


def div_function(var1, var2):
    """ Принимает два числа и проверяет наличе ошибки деления на ноль"""

    try:
        var1 = int(var1)
        var2 = int(var2)
        float(var1 / var2)
    except ZeroDivisionError:
        print("Делить на ноль нельзя!")
    return


while True:
    dividend = input("Введите делимое: ")
    if not if_proper_arg(dividend):
        continue
    while True:
        divider = input("Введите делитель: ")
        if not if_proper_arg(divider):
            continue
        else:
            break
    print("Результат деления: ", div_function(dividend, divider))
    break

# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия,
# год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные
# аргументы. Реализовать вывод данных о пользователе одной строкой.

print()
print("Задание 2. Вариант 1")
print()


def user_data(name, surname, birth_year, city, email, phone_number):
    """ Принимает данные о пользователе и выводит их в консоль в строку. """

    print(f"name: {name}, surname: {surname}, birth year: {birth_year}, city: {city}, email: {email}, phone number: "
          f"{phone_number}")
    return


user_data(name="Иван", surname="Петров", birth_year="1981", city="Москва", email="petrov@mail.ru",
          phone_number="+79119555555")

print()
print("Задание 2. Вариант 2")
print()


def user_data2(**kwargs):
    """ Принимает данные о пользователе и выводит их в консоль столбиком. """

    for key, value in kwargs.items():
        print(f"{key}: {value}")

    return


user_data2(name="Иван", surname="Петров", birth_year="1981", city="Москва", email="petrov@mail.ru",
           phone_number="+79119555555")

# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму
# наибольших двух аргументов.

print()
print("Задание 3. Вариант 1. Только цифры.")
print()


def nums_sum(my_list):
    """Принимает список ТОЛЬКО чисел (т.к. будет использоваться дальше). Возвращает сумму двух наибольших.
     Защиты от дурака нет."""

    my_list.sort()
    sum_two_nums = my_list[len(my_list) - 1] + my_list[len(my_list) - 2]
    return sum_two_nums


print(nums_sum([20, 10, 50, 45]))

print()
print("Задание 3. Вариант 2. Цифры и буквы.")
print()


def take_args(*args):
    """ Принимает любое количество аргументов, проверяет их тип и возвращает список из чисел и/или список
    из символов, в зависимости от типа принятых аргументов. Если на вход подана строка, она будет
    разложена на символы.
    !!! Предусмотрен ввод только чисел или символов. Другие типы переменных не поддерживаются.
    !!! При вводе строки в качестве аргумента, не предусмотрена обработка строки, состоящией и из числа,
    и из символов."""

    # global num_list, letter_list

    num_list = []
    letter_list = []

    print("На вход поданы следующие аргументы:", *args)

    for item in args:
        if isinstance(item, int):
            num_list.append(item)
        else:
            if len(item) > 1:
                for letter in list(item):
                    letter_list.append(letter)
            else:
                letter_list.append(item)

    return num_list, letter_list


def sum_two_max(func):
    ord_letter_list = []

    if func[0]:
        print(f"Из списка чисел: {func[0]}")
        print(f"Сумма двух максимальных равна {nums_sum(func[0])}")
        print()

    if func[1]:
        print(f"Из списка символов: {func[1]}")
        for item in func[1]:
            for letter in item:
                ord_letter_list.append(ord(letter))
        if ord_letter_list:
            print(f"Сумма двух максимальных равна {chr(nums_sum(ord_letter_list))}")
    return


sum_two_max(take_args(20, 10, 50, "a", "r", "qwer", 45))

# 4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо
# выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора
# **. Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

print()
print("Задание 4. Вариант 1. Оператор **")
print()


def my_func(x, y) -> float:
    """ Принимает действительное положительное число Х и целое отрицательное число Y. Возводит X  в
    степень Y при помощи оператора **. """
    result1 = 1 / (x ** abs(y))
    return result1


def if_num(is_float=True, is_positive=True):
    """ Осуществляет проверку корректности ввода по следующим критериям:
    - обрабатывает ошибку, если введена строка
    - является ли введенное число целым или действительным is_float = True/False
    - является ли введеное число положительным или отрицательным is_positive = True/False
    """

    text1 = "действительное" if is_float else "целое"
    text2 = "положительное" if is_positive else "отрицательное"
    var = None

    while True:
        try:
            if is_float:
                var = float(input(f"Введите {text1} {text2} число: "))
            else:
                var = int(input(f"Введите {text1} {text2} число: "))

            if is_positive:
                if var < 0:
                    print("Число должно быть положительным!")
                    continue
            else:
                if var >= 0:
                    print("Число должно быть отрицательным!")
                    continue
        except ValueError:
            print("Нужно ввести число!")
            continue
        else:
            break
    return var


print(my_func(if_num(is_float=True, is_positive=True), if_num(is_float=False, is_positive=False)))

print()
print("Задание 4. Вариант 2. Рекурсия")
print()


def my_func2(x, y):
    """ Принимает действительное положительное число Х и целое отрицательное число Y. Возводит X  в
    степень Y при помощи рекурсии. """

    if y == 1:
        result = x
        return result
    else:
        result = x * my_func(x, y - 1)
    return result


print(my_func2(if_num(is_float=True, is_positive=True), if_num(is_float=False, is_positive=False)))

print()
print("Задание 4. Вариант 3. Цикл")
print()


def my_func3(x, y):
    """ Принимает действительное положительное число Х и целое отрицательное число Y. Возводит X  в
       степень Y при помощи цикла без оператора **. """
    counter = 1
    divider_2 = 1
    while counter <= abs(y):
        divider_2 = divider_2 * x
        counter += 1
    result2 = 1 / divider_2
    return result2


print(my_func3(if_num(is_float=True, is_positive=True), if_num(is_float=False, is_positive=False)))

# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter
# должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова
# нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо
# числа вводится специальный символ, выполнение программы завершается. Если специальный символ введен
# после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после
# этого завершить программу.

print()
print("Задание 5.")
print()

exit_char = "q"
list_number_to_sum = []

while True:
    user_input = input(f"Введите строку чисел, разделенных пробелом (для выхода нажмите {exit_char}): ")
    list_number = user_input.split()

    if exit_char in list_number:
        for i in range(list_number.index(exit_char)):
            list_number_to_sum.append(int(list_number[i]))
        print(f"Сумма введенных чисел до символа {exit_char} = {sum(list_number_to_sum)}")
        # Мария, при пояснении, что нужно сделать в этом ДЗ, Вы указали, что если введен спецсимвол на выход -
        # то цифры в этой строке не должны попадать в сумму. В условии написано, что должны попадать. Я сделала,
        # как в условии. Если делать как указали Вы - то тогда нужно просто break сразу после
        # if exit_char in list_number:
        break
    else:
        for num in list_number:
            list_number_to_sum.append(int(num))
        print(f"Сумма введенных чисел = {sum(list_number_to_sum)}")

# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text. Продолжить работу над заданием.
# В программу должна попадать строка из слов, разделенных пробелом. Каждое слово состоит из латинских букв
# в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().

print()
print("Задание 6.")
print()


def int_func(string):
    """ Принимает слово, проверяет, состоит ли оно только из латинских букв, если да - возвращает его же
    с прописной первой буквой, если нет - то возвращает error. """

    counter = 0
    for letter in string:
        if 65 <= ord(letter) <= 90 or 97 <= ord(letter) <= 122:
            counter += 1
    if counter == len(string):
        string = string.title()
    else:
        string = "error"
    return string


user_text = input("Введите строку из слов, разделенных пробелами. Каждое слово должно состоять из "
                  "латинских букв в нижнем регистре: ")

# user_text = "nice авп ъghj jапро hjjпаро вапрghgh cool"
user_text = user_text.split()
for word in user_text:
    print(int_func(word), end=" ")
