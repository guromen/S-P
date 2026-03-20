# Дан список list и числовой диапазон range. Разработайте метод coincidence(list,
# range) для определения элементов из массива list, значения которого входят в
# указанный диапазон range. Если не передан хотя бы один из параметров, то
# должен вернуться пустой массив.
# Тесты для примеров и проверки:
# coincidence([1, 2, 3, 4, 5], range(3, 6)) # => [3, 4, 5]
# coincidence() # => []
# coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4)) # => [1, 2, 2.5]

def coincidence(l:list=[], r:range=range(0)):
    """Метод проверяет на основе List Comprehention, является ли
    каждый элемент списка числом, и если да, то округляет его
    и проверяет на вхождение в заданный диапазон. Если не передан
    хотя бы один из параметров - возвращается пустой список.
    """
    res = [i for i in l if (isinstance(i, int | float) and (int(i) in r))]
    return res


assert coincidence([1, 2, 3, 4, 5], range(3, 6)) == [3, 4, 5]
assert coincidence() == []
assert coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4)) == [1, 2, 2.5]
assert coincidence([1,2,3,4]) == []