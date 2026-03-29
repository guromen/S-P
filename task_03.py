# Дан список элементов произвольной природы. Необходимо разработать метод
# max_odd(array), который определит максимальный нечетный элемент (21.000 = 21 и
# тоже считается нечетным элементом). Вернуть None, если таких элементов нет в
# переданном массиве.
# Тесты для примеров и проверки:
# max_odd([1, 2, 3, 4, 4]) # => 3
# max_odd([21.0, 2, 3, 4, 4]) # => 21
# max_odd(['ololo', 2, 3, 4, [1, 2], None]) # => 3
# max_odd(['ololo', 'fufufu']) # => None
# max_odd([2, 2, 4]) # => None

class Check:
    """
    Метод max_odd: сначала проверяем, является ли каждый элемент списка нечетным числом
    и находим наибольшее, округляя до целого.
    Если элемент исходного списка - тоже список - по рекурсии так же ищем максимальный
    и возвращаем его или None, если нечетных нет или элементы не числа.
    """
    def max_odd(self, l:list):

        copy_l = list(l)
        max_item = 0
        for i in copy_l:
            if isinstance(i,int|float) and int(i)%2 != 0 and i > max_item:
                    max_item= int(i)
            elif isinstance(i, list):
                return max(self.max_odd(i),max_item)

        return max_item if max_item else None


my_array = Check()

assert my_array.max_odd([1, 2, 3, 4, 4]) == 3
assert my_array.max_odd([21.0, 2, 3, 4, 4]) == 21
assert my_array.max_odd(['ololo', 2, 3, 4, [1, 2], None]) == 3
assert my_array.max_odd(['ololo', 'fufufu']) == None
assert my_array.max_odd([2, 2, 4]) == None
assert my_array.max_odd(['ololo', 2, 3, 4, [1, 2, 39.000], None]) == 39

def max_odd(l):
    return Check().max_odd(l)