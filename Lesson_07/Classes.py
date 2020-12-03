from abc import ABC, abstractmethod


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        output = ""
        for raw in self.matrix:
            for column in raw:
                output += '%+4s' % str(column)
            output = f"{output}\n"
        return output

    def matrix_corrector(self, other):
        """ Принимает две матрицы и выравнивает по количеству строк и количеству элементов в строке,
            добавляя в матрицу с меньшим количеством элементов нули. Работает для списка в списке с
            1 уровнем вложения: [[],[], ..., []]."""

        while len(self.matrix) != len(other.matrix):
            if len(self.matrix) > len(other.matrix):
                other.matrix.append([0])
            elif len(self.matrix) < len(other.matrix):
                self.matrix.append([0])
            else:
                break

        for i in range(len(self.matrix)):
            if len(self.matrix[i]) > len(other.matrix[i]):
                while len(self.matrix[i]) > len(other.matrix[i]):
                    other.matrix[i].append(0)
            elif len(self.matrix[i]) < len(other.matrix[i]):
                while len(self.matrix[i]) < len(other.matrix[i]):
                    self.matrix[i].append(0)
            else:
                continue
        return

    def __add__(self, other):
        for i in range(len(self.matrix)):
            for j in range(len(other.matrix[i])):
                self.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return Matrix.__str__(self)


class Clothes(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def material_consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    def material_consumption(self):
        material_consumption = round(float(self.size / 6.5 + 0.5), 2)
        print(f"Material consumption to make {self.name} - {material_consumption} m.")
        return material_consumption


class Suit(Clothes):
    def __init__(self, name, height):
        super().__init__(name)
        self.height = height

    def material_consumption(self):
        material_consumption = round(float(2 * self.height + 0.3), 2)
        print(f"Material consumption to make {self.name} - {material_consumption} m.")
        return material_consumption


class Cell:
    def __init__(self, cell_number):
        self.cell_number = cell_number

    def __add__(self, other):
        return f"Cell({self.cell_number}) + Cell({other.cell_number}) = " \
               f"Cell({(self.cell_number + other.cell_number)})"

    def __sub__(self, other):
        if self.cell_number > other.cell_number:
            return f"Cell({self.cell_number}) - Cell({other.cell_number}) = " \
                   f"Cell({self.cell_number - other.cell_number})"
        else:
            return f"The minuend is bigger then subtrahend. Cannot perform the operation."

    def __mul__(self, other):
        return f"Cell({self.cell_number}) x Cell({other.cell_number}) = " \
               f"Cell({self.cell_number * other.cell_number}"

    def __truediv__(self, other):
        return f"Cell({self.cell_number}) : Cell({other.cell_number}) = " \
               f"Cell({self.cell_number // other.cell_number})"

    def make_order(self, cells_in_line):
        num_of_lines = self.cell_number // cells_in_line
        for i in range(num_of_lines):
            print("*" * cells_in_line)
        print("*" * (self.cell_number - num_of_lines * cells_in_line), end="")
        print()
        return
