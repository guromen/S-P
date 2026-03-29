# Разработайте метод is_palindrome(string), который будет определять, является ли
# параметр string палиндромом (строкой, которая читается одинаково как сначала
# так и с конца), при условии игнорирования пробелов, знаков препинания и
# регистра.
# Тесты для примеров и проверки:
# is_palindrome("A man, a plan, a canal -- Panama") # => True
# is_palindrome("Madam, I'm Adam!") # => True
# is_palindrome(333) # => True
# is_palindrome(None) # => False
# is_palindrome("Abracadabra") # => False

class Palindrome:
    """ Класс с методом is_palindrome. Метод проверяет, является ли строка палиндромом.
        Принимает на вход число или строку.
        Делаем копию входной строки, игнорируем регистр и удаляем знаки препинания и пробелы
        (Конечно можно было бы быстрее и проще это реализовать через регулярные выражения)
        В цикле проверяются с двух стронон равенстрво символов, иначе сразу же строка- не палиндром
    """

    def is_palindrome(self, phrase:int|str=''):
        if phrase:
            s = ''.join(str(phrase).lower().split())
            s = s.replace('!', '')
            s = s.replace('-', '')
            s = s.replace(',', '')
            s = s.replace('.', '')
            s = s.replace('?', '')
            s = s.replace('\'', '')
            s = s.replace('(', '')
            s = s.replace(')', '')


            i = 0
            res = None
            while i < len(s) // 2:

                if s[i] == s[len(s) - i - 1]:
                    i += 1
                    res = True
                else:
                    res = False
                    break

            return True if res else False
        return False

p1=Palindrome()
assert p1.is_palindrome() == False, 'Добдно быть False'
assert p1.is_palindrome("A man, a plan, a canal -- Panama") == True, 'Добдно быть True'
assert p1.is_palindrome("Madam, I'm Adam!") == True, 'Добдно быть True'
assert p1.is_palindrome(333) == True, 'Добдно быть True'
assert p1.is_palindrome(None) == False, 'Добдно быть False'
assert p1.is_palindrome("Abracadabra") == False, 'Добдно быть False'

def is_palindrome(phrase):
    return Palindrome().is_palindrome(phrase)

