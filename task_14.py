# Реализуйте класс EvenNumbers, который в конструкторе принимает целое число n
# — количество чётных чисел для генерации. Итератор должен выдавать числа по
# порядку, начиная с 0: 0, 2, 4, ..., 2*(n-1).
# Тесты для примеров и проверки:
# evens = EvenNumbers(5)
# for num in evens:
# print(num) # Должно вывести 0, 2, 4, 6, 8

class EvenNumbers:
    """
        Класс, принимающий целое число 'n' и возвращающий итератор
        целых четных чисел 'n'- штук. Иначе берется первый позиционный аргумент,
        или если их нет - значение первого именованного аргумента.
        Если аргументов нет - вызывается исключение TypeError('Нет аргументов')
    """

    def __init__(self, *args, **kwargs):

        if not args and not kwargs:
            raise TypeError('Нет аргументов')
        elif not args and kwargs:
            self.n = [v for k,v in kwargs.items()][0]
        elif len(args)>1 :
            self.n = args[0]
            print(f'Взят первый аргумент, {args[0]}')
        else:
            self.n = args[0]

    def __iter__(self):
        if not isinstance(self.n, int) or self.n <= 0:
            raise ValueError('Введите целое число больше 0')
        else:
            a = (i for i in range(2*(self.n)) if i%2==0)
            return  a


def test_func(*args, **kwargs):

    try:
        evens = EvenNumbers(*args, **kwargs)
        s = ''
        for num in evens:
            s += f'{num} '
        return (s)
    except TypeError as e:
        return str(e)
    except ValueError as e:
        return str(e)

assert test_func(5) == '0 2 4 6 8 '
assert test_func(8) == '0 2 4 6 8 10 12 14 '
assert test_func(0) == 'Введите целое число больше 0'
assert test_func('1') == 'Введите целое число больше 0'
assert test_func(1.5) == 'Введите целое число больше 0'
assert test_func() == 'Нет аргументов'
assert test_func(a = 5, b =3) == '0 2 4 6 8 '
