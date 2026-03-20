# Напишите декоратор @cached, который кэширует результаты функции, чтобы
# избежать повторных вычислений для одних и тех же аргументов. Декоратор
# должен поддерживать:
#
# • ограничение размера кэша: при превышении максимально хранимого
# количества записей (max_size) удаляются самые старые записи:
# • если max_size=None, то размер кэша не ограничен
# • если max_size не соответствует целому числу, то также
# инициализировать его как None
# • время жизни записей: автоматически удалять результаты, сохранённые
# более seconds назад:
# • если seconds=None, то записи не устаревают
# • размер кэша не ограничен, если seconds не соответствует целому
# числу, то также инициализировать его как None
# • декоратор должен учитывать как позиционные (*args), так и
# именованные аргументы (**kwargs)
#
# 13
#
# Тесты для примеров и проверки:
# @cached(max_size=3, seconds=10)
# def slow_function(x):
# print(f"Вычисляю для {x}...")
# return x ** 2
# # Первый вызов — вычисляется
# print(slow_function(2)) # Вывод: "Вычисляю для 2..." → 4
# # Повторный вызов с теми же аргументами — берётся из кэша
# print(slow_function(2)) # Вывод: 4 (без вычисления)
# # Через 15 секунд кэш устареет, и будет новое вычисление
# time.sleep(15)
# print(slow_function(2)) # Вывод: "Вычисляю для 2..." → 4
import time


import time
def cached( max_size:int=None, seconds:int=None):
    """
    Декоратор создает словарь. Проверяем налицие ключа и сразу его возвращаем если находим.
    При привышении max_size - удаляется  через метод pop первый ключ:значение(что возможно не будет работать
    в python версии меньше 3.7)
    Время отсчитывается с момента создания словаря и затем(после очистки)- с момента добавления нового ключа

    """
    if not isinstance(seconds, int):
        seconds = None
    if not isinstance(max_size, int):
        max_size = None
    d = {}
    start =time.time()
    def wrapper(func):
        def inner(*args):
            nonlocal start
            end = time.time()
            # print('time =', end-start)
            if  (seconds==None or (end - start)<seconds):
                print('end-start<seconds')
                if d.get(args[0], None) == None:
                    if max_size==None or len(d)<max_size:
                        d[args[0]] = func(args[0])
                        print(f'1) Ключ не найден. Поэтому записываем {args[0]} в кэш', d)
                        return f'Ответ: {d[args[0]]}'
                    elif len(d)>=max_size:
                        first_key = next(iter(d))
                        d[args[0]] = func(args[0])
                        d.pop(first_key)
                        print(f'Удален первый элемент в кэше')
                        print(f'2)Записываем {args[0]} в кэш', d)
                        return f'Ответ: {d[args[0]]}'
                res = d.get(args[0])
                print(f'3) Ключ найден, поэтому берем {args[0]} из кэша')
                return f'Ответ: {res}'
            d.clear()
            start = time.time()
            print('Кэш очистили, так как end-start > seconds')
            d[args[0]] = func(args[0])
            print(f'4)Записываем {args[0]} в кэш', d)
            return f'Ответ: {d[args[0]]}'
        return inner
    return wrapper

@cached(2,seconds=10)
def slow_function(x):
    print(f'\n.......Долгое вычисление функции с аргументом {x}.......')
    time.sleep(1)
    return x*2

print(slow_function(2))
print(slow_function(2))
time.sleep(15)
print(slow_function(2))
print(slow_function(2))
print(slow_function(4))
print(slow_function(3))
print(slow_function(3))



