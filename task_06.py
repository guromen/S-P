# Разработать методы для программы Камень-Ножницы-Бумага. При реализации
# обработки исключений важно не использовать встроенные классы ошибок с
# передачей им сообщения, а разработать классы с представленными ниже
# названиями.
# Метод rps_game_winner должен принимать на вход массив следующей структуры
# [ ["player1", "P"], ["player2", "S"] ], где P — бумага, S — ножницы, R — камень, и
# функционировать следующим образом:
#
# • если количество игроков больше 2 необходимо вызывать исключение
# WrongNumberOfPlayersError
# • если ход игроков отличается от ‘R’, ‘P’ или ‘S’ необходимо вызывать
# исключение NoSuchStrategyError
# • в иных случаях необходимо вернуть имя и ход победителя, если оба
# игрока походили одинаково - выигрывает первый игрок.
#
# Тесты для примеров и проверки:
# rps_game_winner([['player1', 'P'], ['player2', 'S'], ['player3', 'S']]) #
# => WrongNumberOfPlayersError
# rps_game_winner([['player1', 'P'], ['player2', 'A']]) #
# => NoSuchStrategyError
# rps_game_winner([['player1', 'P'], ['player2', 'S']]) #
# => 'player2 S'
# rps_game_winner([['player1', 'P'], ['player2', 'P']])
# => 'player1 P'



class WrongNumberOfPlayersError(Exception):
    """Исключение, вызываемое, когда игроков не 2."""
    def __init__(self):
        super().__init__(self)

class NoSuchStrategyError(Exception):
    """Исключение вызывается, когда передан неправильный символ (не P, R или S)"""
    def __init__(self):
        super().__init__(self)

def rps_game_winner(l: list):
    """
        Функция rps_game_winner принимает список [игрок, Буква].Если игроков не 2 -
    вызывается пользовательское исключение WrongNumberOfPlayersError; если недопустимая
    Буква - вызывается пользовательское исключение NoSuchStrategyError.
        Реализация: создаем словарь, где ключ- кортеж допустимых комбинаций со значением
    победителя в этом кортеже. Далее создаем объект zip входных данных и проверяем полученную
    комбинацию в словаре. Таких образом определяем победителя
    """
    win_dict = {
        ('P', 'R'):0,
        ('S', 'P'):0,
        ('R', 'S'):0,
        ('R', 'P'):1,
        ('P', 'S'):1,
        ('S', 'R'):1,
        ('P', 'P'):0,
        ('S', 'S'):0,
        ('R', 'R'):0
    }
    if len(l) != 2:
        raise WrongNumberOfPlayersError()
    a,b = [(a,b) for a,b in zip(l[0], l[1])]
    if b not in win_dict:
        raise NoSuchStrategyError()
    return (f'{a[win_dict.get(b)]} {b[win_dict.get(b)]}')


def test_func(l):
    """
    Тесты функции rps_game_winner

        param l: [['player1', 'P'], ['player2', 'S'], ['player3', 'S']]
    return: 'Игроков должно быть 2' (Вызвано исключение WrongNumberOfPlayersError)

        param l: [['player1', 'P'], ['player2', 'A']]
    return: 'Символ должен быть P, R или S' (Вызвано исключение NoSuchStrategyError)

        param l: [['player1', 'P'], ['player2', 'S']]
    return: 'player2 S'

        param l: [['player1', 'P'], ['player2', 'P']]
    return: 'player1 P'
    """
    try:
        res = rps_game_winner(l)
    except WrongNumberOfPlayersError:
        res = ('Игроков должно быть 2')
    except NoSuchStrategyError:
        res = ('Символ должен быть P, R или S')
    return res

assert (test_func([['player1', 'P'], ['player2', 'S'], ['player3', 'S']])) == 'Игроков должно быть 2'
assert (test_func([['player1', 'P'], ['player2', 'A']])) == 'Символ должен быть P, R или S'
assert (test_func([['player1', 'P'], ['player2', 'S']])) == 'player2 S'
assert (test_func([['player1', 'P'], ['player2', 'P']])) == 'player1 P'