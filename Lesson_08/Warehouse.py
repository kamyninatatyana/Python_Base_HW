key_id_number = "id_number"
key_name = "Name"
key_year = "Prod.year"
key_unit_price = "Price, RUR"
key_quantity = "Qty"
key_location = "Location"
key_cost = "Cost"
key_unit_type = "Type"


class Warehouse:

    def __init__(self):
        self.locations_list = {1: "Warehouse", 2: "Sales", 3: "Accounting", 4: "Production"}
        self.location = "Warehouse"
        self.units_dict = {1: "printer", 2: "scanner", 3: "xerox"}
        self.key_word_list = [key_id_number, key_name, key_year, key_unit_price, key_unit_type, key_location]
        self.units_on_stock_list = [
            {key_id_number: 1, key_name: "printer", key_year: 2020, key_unit_price: 3900, key_unit_type:
                "Canon PIXMA TS304", key_location: "Warehouse"},
            {key_id_number: 2, key_name: "printer", key_year: 2019, key_unit_price: 5299, key_unit_type:
                "Pantum P2207", key_location: "Warehouse"},
            {key_id_number: 3, key_name: "scanner", key_year: 2019, key_unit_price: 5090, key_unit_type:
                "Canon CanoScan LiDE 300", key_location: "Warehouse"},
            {key_id_number: 4, key_name: "scanner", key_year: 2020, key_unit_price: 5824, key_unit_type:
                "Epson Perfection V19", key_location: "Warehouse"},
            {key_id_number: 5, key_name: "printer", key_year: 2018, key_unit_price: 8190, key_unit_type:
                "Xerox Phaser 3020BI", key_location: "Warehouse"},
        ]

    def print_line_for_unit_report(self, key_word, key):
        for unit in self.units_on_stock_list:
            if unit[key_name] == self.units_dict[key]:
                print(f"{str(unit[key_word]).ljust(20, ' ')}", end="\t")
        return

    def print_line_for_location_report(self, key_word, key):
        for unit in self.units_on_stock_list:
            if unit[key_location] == self.locations_list[key]:
                print(f"{str(unit[key_word]).ljust(20, ' ')}", end="\t")
            else:
                return

    def what_is_on_stock_by_unit(self, key):
        print()
        for key_word in self.key_word_list:
           print(f'{key_word.rjust(10, " ")}:', end="\t\t\t")
           Warehouse.print_line_for_unit_report(self, key_word, key)
           print()
        return

    def what_is_on_stock_by_location(self, key):
        print()
        for key_word in self.key_word_list:
            print(f'{key_word.rjust(10, " ")}:', end="\t\t\t")
            Warehouse.print_line_for_location_report(self, key_word, key)
            print()
        print()
        return

    def financial_report(self):
        printer_cost = 0
        scanner_cost = 0
        xerox_cost = 0

        for unit in self.units_on_stock_list:
            if unit["Name"] == "printer":
                printer_cost += int(unit["Price, RUR"])
            if unit["Name"] == "scanner":
                scanner_cost += int(unit["Price, RUR"])
            if unit["Name"] == "xerox":
                xerox_cost += int(unit["Price, RUR"])
        total_cost = printer_cost + scanner_cost + xerox_cost
        return f"There are:\nprinters on total sum of {printer_cost} RUR,\nscanners on total sum of" \
               f" {scanner_cost} RUR,\nxerox on total sum of {xerox_cost} RUR.\nTotal cost of office equipment" \
               f" is {total_cost} RUR."

    def show_what_to_transfer(self, key):
        for unit in self.units_on_stock_list:
            if key in self.units_dict:
                if unit["Name"] == self.units_dict[key]:
                    print(" ".join(map(str, unit.values())))

        unit_choice = input("Please, input id number of the unit you want to transfer: ")
        for unit in self.units_on_stock_list:
            if unit["id_number"] == int(unit_choice):
                location_choice = input("-> to transfer to Warehouse press <1>\n"
                                        "-> to transfer to Sales press <2>\n"
                                        "-> to transfer to Accounting press <3>\n"
                                        "-> to transfer to Production press <4>\n"
                                        "-> to exit menu press <5>\n")
                if location_choice == "5":
                    break
                else:
                    unit["Location"] = self.locations_list[int(location_choice)]
                    print(f"{unit['Name']} id number {unit['id_number']} is successfully transferred to "
                          f"{unit['Location']} ")
                return


class OfficeEquipment:
    def __init__(self, id_number, name, year, unit_price, location):
        self.id = id_number
        self.name = name
        self.year = year
        self.unit_price = unit_price
        self.location = location
        self.unit_dict = {key_id_number: id_number, key_name: name, key_year: year, key_unit_price: unit_price,
                          key_location: location}


class Printer(OfficeEquipment):
    def __init__(self, id_number, name, year, unit_price, location, unit_type):
        super().__init__(id_number, name, year, unit_price, location)
        self.unit_type = unit_type


class Scanner(OfficeEquipment):
    pass


class Xerox(OfficeEquipment):
    pass


