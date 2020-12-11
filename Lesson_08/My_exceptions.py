class MyExceptionZeroDivision(Exception):
    def __init__(self, text):
        self.text = text


class MyExceptionTypeValidation(Exception):
    def __init__(self, text):
        self.text = text
