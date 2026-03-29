# Анаграмма — литературный приём, состоящий в перестановке букв или звуков
# определённого слова (или словосочетания), что в результате даёт другое слово
# или словосочетание.
# Разработайте метод combine_anagrams(words_array), который принимает на вход
# массив слов и разбивает их в группы по анаграммам, регистр букв не имеет
# значения при определении анаграмм.
# Тест для примеров и проверки:
# combine_anagrams(["cars", "for", "potatoes", "racs", "four", "scar",
# "creams", "scream"]) # => [ ["cars", "racs", "scar"], ["four"], ["for"],
# ["potatoes"], ["creams", "scream"] ]

class Anagramm:
    """
    Метод combine_anagrams принимает список строк и возвращает список слов,
    являющихся анаграммами.
    В цикле сравнимаем каждое следующее слово с предыдущим(они отсортированы)
    Таким образом создается отдельный список слов анаграм. В результате создается
    список списков слов анаграм
    """
    def combine_anagrams(self, list_ar: list[str]):
        if not isinstance(list_ar, list):
            return []
        l = list(list_ar)
        combine_result = []
        for n in range(len(l) - 1):
            res1 = []
            res1.append(l[n].lower())
            for k in range(1 + n, len(l)):
                if sorted(l[n]) == sorted(l[k].lower()):
                    res1.append(l[k])
                    l[k] = ''
            combine_result.append(res1)
            combine_result = [i for i in combine_result if '' not in i]

        return combine_result


anagram = Anagramm()
assert (anagram.combine_anagrams(["cars", "for", "potatoes", "racs", "four", "scar", "creams", "scream"])) == \
    [['cars', 'racs', 'scar'], ['for'], ['potatoes'], ['four'], ['creams', 'scream']]
assert (anagram.combine_anagrams(['python', 'lypton', 'caiman', 'recap', 'caper', 'pacer', 'maniac'])) == \
    [['python'], ['lypton'], ['caiman', 'maniac'], ['recap', 'caper', 'pacer']]
assert (anagram.combine_anagrams(3)) == []

def combine_anagrams(list_ar):
    return Anagramm().combine_anagrams(list_ar)