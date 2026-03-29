# Написать метод multiply_numbers(inputs), который вернет произведение цифр,
# входящих в inputs.
# Тест для примеров и проверки:
# multiply_numbers() # => None
# multiply_numbers('ss') # => None
# multiply_numbers('1234') # => 24
# multiply_numbers('sssdd34') # => 12
# multiply_numbers(2.3) # => 6
# multiply_numbers([5, 6, 4]) # => 120


def multiply_numbers(inputs=None):
    """
    Метод создает сначала список элементов,
    а затем список чисел и производит их перемножение. Иначе если цифр нет- None
    """

    if inputs is None:
        return None
    str_input = str(inputs)
    list_input = ('_'.join(str_input)).split('_')

    int_list = [int(x) for x in list_input if x.isdigit()]
    if int_list == []:
        return None
    prdct = 1
    for i in int_list:
        prdct *=int(i)
    return (prdct)


assert multiply_numbers() == None
assert multiply_numbers('1234') == 24
assert multiply_numbers('sssdd34') == 12
assert multiply_numbers(2.3) == 6
assert multiply_numbers([5, 6, 4]) == 120
assert multiply_numbers('') == None
