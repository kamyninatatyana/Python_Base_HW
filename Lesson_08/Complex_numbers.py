""" Задание 7. Операции с комплексными числами."""


class ComplexNumber:
    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)
        self.complex_number = f'{self.a} {self.sign_checker(self.b)}{self.b}i'

    def __str__(self):
        return f'{self.complex_number}'

    @classmethod
    def set_param(cls, complex_number):
        if isinstance(complex_number, str):
            a, sign, imaginary_part = complex_number.split()
            b, i = imaginary_part
            b = sign + b
            return cls(a, b)
        elif isinstance(complex_number, list) or isinstance(complex_number, tuple):
            try:
                a, b = complex_number
                return cls(a, b)
            except (ValueError, AttributeError):
                print(f'Can not create complex number with attributes {complex_number}. Complex number like'
                      f'\'a + bi\' can be created with following ways:\n'
                      f'1. Directly via creating class copy with transferring of 2 arguments: a, b (in str or int'
                      f'format) with obligatory putting a negative sign,\nif a number is negative.\n'
                      f'2. Via class method set_param with transferring complex number by string like \'a + bi\'.\n'
                      f'3. Via class method set_param with transferring a and b via list or tuple with an obligatory'
                      f'putting a negative sign if a number is negative.')
                return cls(0, 0)

    @staticmethod
    def sign_checker(num):
        sign = "+" if num >= 0 else ""
        return sign

    def __add__(self, other):
        return f'({self.complex_number}) + ({other.complex_number})' \
               f'= {self.a + other.a} {self.sign_checker(self.b + other.b)}{self.b + other.b}i'

    def __mul__(self, other):
        return f'({self.complex_number}) * ({other.complex_number})' \
               f')= {self.a * other.a - self.b * other.b} {self.sign_checker(self.a * other.b + other.a * self.b)}' \
               f'{(self.a * other.b + other.a * self.b)}i'
