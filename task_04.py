# Дан список целых чисел. Необходимо разработать метод sort_list(list), который
# поменяет местами все минимальные и максимальные элементы массива, а также
# добавит в конец массива одно минимальное значение из него.
# Тесты для примеров и проверки:
# sort_list([]) # => []
# sort_list([2, 4, 6, 8]) # => [8, 4, 6, 2, 2]
# sort_list([1]) # => [1, 1]
# sort_list([1, 2, 1, 3]) # => [3, 2, 3, 1, 1]

class MySort:
    """
    В методе sort_list создаем копию исходного списка и сразу же находим
    максимальный и минимальный элементы, а так же их количество в списке.
    Чтобы не дублировать код, создал статик-метод list_of_indexes, который создает 2 списка с индексами
    минимальных и максимальных элементов,
    и затем присваиваем максимальное/минимальное значение.
    В конец готового списка добавляем минимальный элемент.
    """
    def sort_list(self, l: list):
        if not isinstance(l, list) or l==[]:
            return []
        copy_l = list(l)
        min_el = min(copy_l)
        max_el = max(copy_l)

        count_min = copy_l.count(min_el)  # Количество min в l
        count_max = copy_l.count(max_el)  # Количество max в l

        list_of_min_index = self.list_of_indexes(count_min, min_el, copy_l)
        list_of_max_index = self.list_of_indexes(count_max, max_el, copy_l)

        for i in list_of_min_index:
            copy_l[i] = max_el
        for i in list_of_max_index:
            copy_l[i] = min_el
        copy_l.append(min_el)

        return copy_l

    @staticmethod
    def list_of_indexes(count_max_min:int, max_min_el:int, copy_l:list):
        list_of_index = []
        ind = 0
        for i in range(count_max_min):
            ind = copy_l.index(max_min_el, ind)
            list_of_index.append(ind)
            ind += 1
        return list_of_index


a = MySort()

assert (a.sort_list([2, 4, 6, 8])) == [8, 4, 6, 2, 2]
assert (a.sort_list([1])) == [1, 1]
assert (a.sort_list([1, 2, 1, 3])) == [3, 2, 3, 1, 1]
assert (a.sort_list([])) == []

def sort_list(l):
    return MySort().sort_list(l)