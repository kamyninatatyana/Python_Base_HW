# УРОК 2

# 1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки
# типа данных каждого элемента. Использовать функцию type() для проверки типа. Элементы списка можно
# не запрашивать у пользователя, а указать явно, в программе.

print("Задание 1.")

my_list = [1, "apple", 3.14, [1, 2, 3, 4, 5], {4, 3, 5}, None, True]

for item in enumerate(my_list, 1):
    print(f"{item[0]}. {item[1]}: {type(item[1])}")

# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы
# с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

print()
print("Задание 2. Вариант 1.")

next_item = None
my_list = []
i = 1

while next_item != "y":
    my_list.append(input(f"Пожалуйста, введите {i}-й элемент списка: "))
    next_item = input("Закончить ввод? ('y' - да, любая другая клавиша - продолжить): ").lower()
    i += 1

print("Список до перестановки: ", my_list)

even_index = []
odd_index = []
my_list_new = []

for i in range(0, len(my_list), 2):
    even_index.append(my_list[i])

for i in range(1, len(my_list), 2):
    odd_index.append(my_list[i])

for i in range(len(odd_index)):
    my_list_new.append(odd_index[i])
    my_list_new.append(even_index[i])

if len(even_index) > len(odd_index):
    my_list_new.append(even_index[len(even_index)-1])


print("Список после перестановки: ", my_list_new)

print()
print("Задание 2. Вариант 2.")

i = 0
var_to_store = 0
counter = len(my_list)

if len(my_list) % 2 != 0:
    counter = len(my_list) - 1

while i < counter:
    var_to_store = my_list[i]
    my_list[i] = my_list[i+1]
    my_list[i+1] = var_to_store
    i += 2

print("Список после перестановки: ", my_list)

# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится
# месяц (зима, весна, лето, осень). Напишите решения через list и через dict.

print()
print("Задание 3.")

while True:
    user_month = (input("Введите номер месяца в виде целого числа от 1 до 12: "))
    if user_month.isdigit() and 12 >= int(user_month) >= 1:
        user_month = int(user_month)
        break
    else:
        print("Номер месяца необходимо указывать числом. И он не может быть меньше единицы и больше 12! ")

print()
print("Вариант 1:")

season_list = ["Зима", "Весна", "Лето", "Осень"]
months_list = [(1, 2, 12), (3, 4, 5), (6, 7, 8), (9, 10, 11)]

for months in months_list:
    if user_month in months:
        print(season_list[months_list.index(months)])

print()
print("Вариант 2:")

seasons_dict = {
                (1, 2, 12): "Зима",
                (3, 4, 5): "Весна",
                (6, 7, 8): "Лето",
                (9, 10, 11): "Осень"
                }

for months in seasons_dict:
    if user_month in months:
        print(seasons_dict[months])

print()
print("Вариант 3:")

seasons_dict = {
                "Зима": (1, 2, 12),
                "Весна": (3, 4, 5),
                "Лето": (6, 7, 8),
                "Осень": (9, 10, 11)
                }

for season, months in seasons_dict.items():
    if user_month in months:
        print(season)

# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой
# строки. Строки необходимо пронумеровать. Если слово длинное, выводить только первые 10 букв в слове.

print()
print("Задание 4.")
string = input("Введите строку из нескольких слов, разделенных пробелами: ")

for el in enumerate(string.split(), 1):
    print(f"{el[0]}. {el[1][0:10]}")

# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с
# одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
# Подсказка.
# Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

print()
print("Задание 5.")

my_list = [7, 5, 3, 3, 2]
print("Первоначальный список: ", my_list)
next_item = None

while next_item != "y":

    user_number = int(input("Введите любое натуральное (целое, положительное) число: "))

    for i in range(len(my_list)):
        if user_number <= my_list[i]:
            continue
        elif user_number > my_list[i]:
            my_list.insert(i, str(user_number))
            break

    if user_number <= my_list[len(my_list)-1]:
        my_list.append(str(user_number))

    print("Новый список теперь выглядит вот так:", my_list)

    my_list = [int(item) for item in my_list]
    next_item = input("Закончить ввод? ('y' - да, любая другая клавиша - продолжить): ")
    next_item = next_item.lower()


# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж
# хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с
# параметрами (характеристиками товара: название, цена, количество, единица измерения). Структуру нужно
# сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
#    (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
#    (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
#    (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика
# товара, например название, а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
#    “название”: [“компьютер”, “принтер”, “сканер”],
#    “цена”: [20000, 6000, 2000],
#    “количество”: [5, 2, 7],
#    “ед”: [“шт.”]
# }
#

print()
print("Задание 6.")
print()

next_item = ""
number = ""
key_name = "название"
key_price = "цена"
key_qty = "количество"
key_mu = "ед"

product_dict = {key_name: "", key_price: "", key_qty: "", key_mu: ""}
product_list = []
product_analytic = {key_name: [], key_price: [], key_qty: [], key_mu: []}

user_answer = input("Вы можете создать свою базу товаров с нуля ('n') или воспользоваться для "
                    "тестирования\nготовой базой (любая другая клавиша)? ")

if user_answer == "n":
    product_list = []

    while next_item != "y":
        number = input("Введите номер товара: ")
        name = input("Введите название товара: ")
        price = input("Введите цену товара: ")
        qty = input("Введите количество товара: ")
        mu = input("Введите единицы измерения товара: ")
        next_item = input("Завершить? - 'y', Продолжить - любая клавиша. ")
        next_item = next_item.lower()

        product_dict = dict({key_name: name, key_price: price, key_qty: qty, key_mu: mu})
        product_list.append((number, product_dict))

else:
    product_list = [
        (1, {"название": "компьютер", "цена": 20000, "количество": 5, "ед": "шт."}),
        (2, {"название": "принтер", "цена": 6000, "количество": 2, "ед": "шт."}),
        (3, {"название": "сканер", "цена": 2000, "количество": 7, "ед": "шт."})
    ]

print()
print("Старый список:")

for product in product_list:
    print(product)

for product in product_list:
    for key, value in product[1].items():
        if key in product_analytic:
            product_analytic[key].append(value)

print()
print("Новый словарь: ")
print()

for key, value in product_analytic.items():
    print(f"{key}: {value}")
