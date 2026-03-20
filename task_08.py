# Написать метод multiply_numbers(inputs), который вернет произведение цифр,
# входящих в inputs.
# Тест для примеров и проверки:
# multiply_numbers() # => None
# multiply_numbers('ss') # => None
# multiply_numbers('1234') # => 24
# multiply_numbers('sssdd34') # => 12
# multiply_numbers(2.3) # => 6
# multiply_numbers([5, 6, 4]) # => 120


def multiply_numbers():
    """
    Метод принимает строку из input, и создает из нее сначала список элементов,
    а затем список чисел и производит их перемножение. Иначе если цифр нет- None
    """

    str_input = input('Введите числа: ')
    str_input = str_input.strip()
    if str_input == '' or str_input ==[]:
        return ('пустая строка',None)
    list_input = ('_'.join(str_input)).split('_')

    int_list = [int(x) for x in list_input if x.isdigit()]
    if int_list == []:
        return ('пустой список',None)
    prdct = 1
    for i in int_list:
        prdct *=int(i)
    return (prdct)


print(multiply_numbers())
