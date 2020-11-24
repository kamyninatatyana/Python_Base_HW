# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл
# не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

from itertools import count
from itertools import cycle


def numbers():
    start_number = int(input("С какого числа будем выводить целые числа? "))
    fin_number = int(input("По достижении какого числа будем завершать цикл? "))
    for number in count(start_number, 1):
        if number > fin_number:
            return
        else:
            print(number)
    return


def repeater():
    user_input = input("Введите любой набор символов, с которым будем работать: ")
    limit = int(input("Сколько циклов повторения делаем? "))
    counter = 1
    for el in cycle(user_input):
        if counter > limit:
            return
        print(el)
        counter += 1
    return


def numbers_or_repeater():
    while True:
        what_to_do = input("Что сделать с последовательностью? - создать (1), повторить (2): ")
        if what_to_do == "1":
            start_number = int(input("С какого числа будем выводить целые числа? "))
            fin_number = int(input("По достижении какого числа будем завершать цикл? "))
            for number in count(start_number, 1):
                if number > fin_number:
                    return
                else:
                    print(number)
            return
        elif what_to_do == "2":
            user_input = input("Введите любой набор символов, с которым будем работать: ")
            limit = int(input("Сколько циклов повторения делаем? "))
            counter = 1
            for el in cycle(user_input):
                if counter > limit:
                    return
                print(el)
                counter += 1
            return
