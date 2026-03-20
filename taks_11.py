# Реализуйте класс Dessert c геттерами и сеттерами name и calories, конструктором,
# принимающим на вход name и calories (не обязательные параметры), а также двумя
# методами is_healthy (возвращает true при условии калорийности десерта менее
# 200) и is_delicious (возвращает true для всех десертов).

class Dessert:
    """
    Клачч принимает необязательные параметры name, calories
    Геттеры и сеттеры реализованы через объект свойства property
    Атрибуты записываются в _name и _calories

    """
    def __init__(self, name:str=None, calories:int=None):
        if not isinstance(name, str):
            raise ValueError('Введите строку')
        self.name = name
        if not isinstance(calories, int):
            raise ValueError('Введите число')
        self.calories = calories

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value

    @property
    def calories(self):
        return self._calories

    @calories.setter
    def calories(self, value):
        self._calories = value

    def is_healthy(self):
        """
        (возвращает true при условии калорийности десерта менее 200)
        """
        return True if self._calories < 200 else False

    def is_delicious(self):
        """
        (возвращает true для всех десертов)
        """
        return True

a = Dessert('tort', 350)

assert (a.name) == 'tort'
a.name ='tortik'
assert (a.name) == 'tortik'
assert (a.calories) == 350
assert (a.is_healthy()) == False
a.calories = 150
assert (a.calories) == 150
assert ( a.is_healthy()) == True
assert (a.is_delicious()) == True

try:
    b = Dessert(22,243)
except ValueError as e:
    assert 'Введите строку'
try:
    с = Dessert('cake', '194')
except ValueError as e:
    assert 'Введите число'