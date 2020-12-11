from Lesson_08.Warehouse import Warehouse, Printer, Scanner, Xerox, key_id_number, key_name, key_location, key_year, \
    key_unit_type, key_unit_price

print("Welcome to Office equipment warehouse programme!")

warehouse = Warehouse()


def is_digit(text, is_digit=True):
    """Запрашивает от пользователя ввод информации (определяется фразой, переданной в переменную text)
    и В зависимости от флага (is_digit = True - для чисел и False - если проверка не требуется) проверяет
    ее на корректность введенного типа данных. Если тип данных введен верно - возвращает введенное значение,
    если ошибка - сообщает об этом и запрашивает ввод снова до тех пор, пока не будут введены корретные
    данные. """

    while True:
        param = input(f"Indicate {text}: ")
        if is_digit:
            if not param.isdigit():
                print("Use numbers!")
            else:
                break
        else:
            break
    return param


def attributes_input(location="Warehouse"):
    """ Запрашивает от пользователя параметры для вводимой единицы офисной техники (определяется названием,
    переданным в переменную name), присваивает Warehouse для location по умолчанию и возвращает все собранные
    значения."""

    id_number = len(warehouse.units_on_stock_list) + 1
    year = is_digit("production year", is_digit=True)
    unit_price = is_digit("unit price in RUR", is_digit=True)
    unit_type = is_digit("unit type", is_digit=False)
    return id_number, year, unit_price, unit_type, location


def unit_input():
    """Пользователь выбирает вид орг.техники. Создается экземпляр класса соответствующего вида, словарь с
    атрибутами этого экземпляра и добавляется в общий список всех созданных экземпляров"""

    while True:
        name_choice = input('Press:  <1> - for printer\n'
                            '\t\t<2> - for scanner\n'
                            '\t\t<3> - for xerox\n'
                            '\t\t<4> - for exit\n')
        if name_choice == "1":
            name = "printer"
            id_number, year, unit_price, unit_type, location = attributes_input()
            printer = Printer(id_number, name, year, unit_price, location, unit_type)
            printer.unit_dict = {key_id_number: id_number, key_name: name, key_year: year, key_unit_price: unit_price,
                                 key_unit_type: unit_type, key_location: location}
            warehouse.units_on_stock_list.append(printer.unit_dict)
            break
        elif name_choice == "2":
            name = "scanner"
            id_number, year, unit_price, unit_type, location = attributes_input()
            scanner = Scanner(id_number, name, year, unit_price, location)
            scanner.unit_dict = {key_id_number: id_number, key_name: name, key_year: year, key_unit_price: unit_price,
                                 key_unit_type: unit_type, key_location: location}
            warehouse.units_on_stock_list.append(scanner.unit_dict)
            break
        elif name_choice == "3":
            name = "xerox"
            id_number, year, unit_price, unit_type, location = attributes_input()
            xerox = Xerox(id_number, name, year, unit_price, location)
            xerox.unit_dict = {key_id_number: id_number, key_name: name, key_year: year, key_unit_price: unit_price,
                               key_unit_type: unit_type, key_location: location}
            warehouse.units_on_stock_list.append(xerox.unit_dict)
        elif name_choice == "4":
            break
        else:
            print("Your input is incorrect. Please follow the instruction in menu.")
    return


def choose_unit_report():
    """ Предлагает пользователю выбора вид орг.техники, для которого необходимо создать отчет. И выдает
    информацию об всех единицах этого вида орг.техники, находящися в организации."""
    while True:
        menu_choice_3lev = input("-> for printers on stock report press <1>\n"
                                 "-> for scanners on stock report press <2>\n"
                                 "-> for xerox on stock report press <3>\n"
                                 "-> to exit the programme press <4>\n")
        if menu_choice_3lev == "4":
            break
        else:
            warehouse.what_is_on_stock_by_unit(int(menu_choice_3lev))
    return


def choose_location_report():
    while True:
        menu_choice_3lev = input("-> for stock report for Warehouse press <1>\n"
                                 "-> for stock report for Sales press <2>\n"
                                 "-> for stock report for Accounting press <3>\n"
                                 "-> for stock report for Production press <4>\n"
                                 "-> to exit menu press <5>\n")
        if menu_choice_3lev == "5":
            break
        else:
            warehouse.what_is_on_stock_by_location(int(menu_choice_3lev))
    return


def warehouse_main():
    while True:
        menu_choice = input("Please, make your choice:\n"
                            "-> to input new equipment press <1>\n"
                            "-> to check what is on stock press <2>\n"
                            "-> to transfer equipment press <3>\n"
                            "-> to exit the programme press <4>\n")

        if menu_choice == "4":
            print("Thank you. Good bye.")
            break
        elif menu_choice == "1":
            unit_input()
        elif menu_choice == "2":
            while True:
                menu_choice_2lev = input("-> for report by unit press <1>\n"
                                         "-> for report by location press <2>\n"
                                         "-> for financial report press <3>\n"
                                         "-> to exit menu press <4>\n")
                if menu_choice_2lev == "4":
                    break
                elif menu_choice_2lev == "1":
                    choose_unit_report()
                elif menu_choice_2lev == "2":
                    choose_location_report()
                elif menu_choice_2lev == "3":
                    print(warehouse.financial_report())
        elif menu_choice == "3":
            menu_choice_2lev = input("-> to transfer printer press <1>\n"
                                     "-> to transfer scanner press <2>\n"
                                     "-> to transfer xerox press <3>\n"
                                     "-> to exit menu press <4>\n")
            if menu_choice_2lev == "4":
                break
            else:
                warehouse.show_what_to_transfer(int(menu_choice_2lev))
    return
