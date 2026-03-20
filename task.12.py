# Создайте класс JellyBean, расширяющий класс Dessert (из Упражнения 11) новым
# геттером и сеттером для атрибута flavor (все параметры являются не
# обязательными). Измените метод is_delicious таким образом, чтобы он возвращал
# false только в тех случаях, когда flavor равняется «black licorice».

from taks_11 import Dessert

class JellyBean(Dessert):

    def __init__(self, name:str=None, calories:int=None, flavour:str=None):
        super().__init__(name, calories)
        self._flavour = flavour

    @property
    def flavour(self):
        return self._flavour

    @flavour.setter
    def flavour(self, value):
        if  isinstance(value, str):
            self._flavour = value
        else:
            raise AttributeError('Должна быть строка')
    def is_delicious(self):
        """Переопределяюм метод"""
        if self._flavour == 'black licorice':
            return False
        return True

a = JellyBean('sdf',10)
assert (a.is_healthy()) == True
assert (a.is_delicious()) == True
a.flavour = 'Cherry'
assert (a.flavour) == 'Cherry'
assert (a.is_delicious()) == True
a.flavour = 'black licorice'
assert (a.is_delicious()) == False
try:
    b = Dessert(22,243)
except ValueError as e:
    assert 'Введите строку'
try:
    с = Dessert('cake', '194')
except ValueError as e:
    assert 'Введите число'