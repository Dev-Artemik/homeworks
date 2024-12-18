class Car:
    def __init__(self, model, vin, numbers):
        self.model = model
        self.__vin = vin
        self.__numbers = numbers

    def __is_valid_vin(self, vin_number):
        if vin_number == self.__vin:
            return True
        else:
            return 'Исключение ----------------'

    def __is_valid_numbers(self, numbers):
        if numbers == self.__numbers:
            return True
        else:
            return 'Исключение2 ---------------'


class IncorrectVinNumber(Exception):

    = 'Некорректный тип vin номера'

class IncorrectCarNumbers(Exception):
    message = ''