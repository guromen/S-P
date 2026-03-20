# Разработайте функцию count_words(string), которая будет возвращать словарь со
# статистикой частоты употребления входящих в неё слов.
# Тесты для примеров и проверки:
# count_words("A man, a plan, a canal -- Panama") # => {"a": 3, "man": 1,
# "canal": 1, "panama": 1, "plan": 1}
# count_words("Doo bee doo bee doo") # => {"doo": 3, "bee": 2}


def count_words(a = ""):
    """Метод создает список слов, а затем считаем количество каждых"""

    s = a.lower()
    s = s.replace('!', '')
    s = s.replace('-', '')
    s = s.replace(',', '')
    s = s.replace('.', '')
    s = s.replace('?', '')
    s = s.replace('\'', '')
    s = s.replace('(', '')
    s = s.replace(')', '')
    s = s.split()

    d = {}
    for i in sorted(s):
        d[i]= s.count(i)
    return (d)

assert count_words("A man, a plan, a canal -- Panama") == {'a': 3, 'canal': 1, 'man': 1, 'panama': 1, 'plan': 1}
assert count_words("Doo bee doo bee doo")  == {"doo": 3, "bee": 2}



