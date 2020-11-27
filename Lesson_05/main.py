import json
import random

# УРОК 5
# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые
# пользователем. Об окончании ввода данных свидетельствует пустая строка.

print()
print("Задание 1")
print()

with open("text_1.txt", "w", encoding="utf-8") as file:
    user_input = "y"
    count = 1
    while True:
        user_input = input(f"Введите {count}-ю строку. Для разделения слов/чисел используйте пробел. "
                           f"Чтобы закончить ввод - не вводите ничего и нажмите 'Enter': ")
        if user_input == "":
            break
        else:
            count += 1
            file.writelines(user_input + "\n")

# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

print()
print("Задание 2")
print()

# line_list = [] - можно не через счетчик, а создать список из строк и потом взять длину списка.
line_counter = 0

with open("text_1.txt", "r", encoding="utf-8") as file:
    for line in file:
        if line != "":

            print(f"Строка: '{line[0:-1]}' содержит {len(line.split())} слов(а)")
            line_counter += 1
            # line_list.append(line)

print(f"В файле всего {line_counter} строк(и)")
# print(f"В файле всего {len(line_list)} строк(и)")

# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить
# подсчет средней величины дохода сотрудников.

print()
print("Задание 3")
print()

total_salary = 0
counter = 0


with open("text_3.txt", "r", encoding="utf-8") as file:
    print(f"Зарплата меньше 20000 у сотрудников: ", end="")
    for line in file:
        surname, salary = line.split()
        salary = float(salary)
        total_salary += salary
        counter += 1
        if salary < 20000:
            print(f"{surname}, ", end="")

print()
print(f"Средняя величина дохода сотрудника: {total_salary / counter}")


# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом
# английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый
# текстовый файл.

print()
print("Задание 4")
print()

my_list = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
content = []

with open("text_4.txt", encoding="utf-8") as file_to_read:
    print("Содержимое файла до перевода:")
    for line in file_to_read:
        print(line, end="")
        content.append(line.split(" - "))

print()


for item in content:
    for key in item:
        if key in my_list:
            item[0] = my_list[key]
            item[1] = " - " + item[1]

with open("text_4w.txt", "w", encoding="utf-8") as file_to_write:
    for item in content:
        file_to_write.writelines(item)

print()
print("Содержимое файла после перевода:")
with open("text_4w.txt", "r", encoding="utf-8") as file_to_read:
    for line in file_to_read:
        print(line, end="")


# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

print()
print("Задание 5")
print()

with open("text_5.txt", "w", encoding="utf-8") as file:
    my_numbers = [random.randrange(1, 1000, random.randint(1, 100)) for _ in range(random.randint(1, 25))]
    print(my_numbers)
    file.writelines(str(my_numbers))

print(f"Сумма чисел {sum(my_numbers)}")


# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и
# наличие лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы
# для каждого предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название
# предмета и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

print()
print("Задание 6")
print()

my_dict = {}


def number_from_string(my_string):
    my_number = ""
    for item in my_string:
        if item.isdigit():
            my_number += item
        elif item == "-":
            my_number += "0"
    return my_number


with open("text_6.txt", encoding='UTF-8') as file_to_read:
    for line in file_to_read:
        subject, lecture, practice, lab = line.split()
        lecture = number_from_string(lecture)
        practice = number_from_string(practice)
        lab = number_from_string(lab)
        my_dict[subject[:-1]] = int(lecture) + int(practice) + int(lab)

for key, val in my_dict.items():
    print(f"{key} - {val}")


# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней
# прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.

print()
print("Задание 7")
print()

firm_dict = {}
result_dict = {}
content = []
average_profit_list = []


with open("text_7.txt", encoding='UTF-8') as file_to_read:
    for line in file_to_read:
        firm, form, revenue, expenses = line.split()
        result = int(revenue) - int(expenses)
        if result > 0:
            average_profit_list.append(result)
        firm_dict[firm] = result

    result_dict["average_profit"] = sum(average_profit_list) / len(average_profit_list)
    content.append(firm_dict)
    content.append(result_dict)

with open("text_7w.json", "w") as file_to_write:
    json.dump(content, file_to_write)

    for part in content:
        for k, v in part.items():
            print(json.dumps(f"{k} - {v}", indent=4, ensure_ascii=False, separators=(",", ": ")))
