# Задание является не обязательным, но его выполнение поможет лучше
# ознакомиться с итераторами.
# Реализовать класс BlockTranspositionCipher, который будет шифровать и
# расшифровывать текст методом блочной перестановки с помощью текстового
# ключа.
# Основная идея:
#
# 1. Ключ — строка, состоящая из уникальных английских букв. Пример:
# acb
# 2. Шифрование — алгоритм, который преобразует исходный текст в
# набор зашифрованных символов.
# 3. Дешифрование — алгоритм, который преобразует набор
# зашифрованных символов в исходный текст.
#
# 14
#
# Ключ и его обработка:
#
# • ключ состоит только из букв английского алфавита
# • символы в ключе должны быть уникальны (регистр букв не имеет
# значения — "A" и "a" считаются одинаковыми)
# • ключ преобразуется в числовой массив. Каждому символу
# присваивается его порядковый номер в алфавите (a = 0, b = 1, ..., z =
# 25)
#
# Правила шифрования:
#
# • исходный текст делится на блоки длины, равной длине ключа
# • если длина блока не кратна длине ключа, то оставшийся блок
# дополняется пробелами
# • в каждом из блоков символы переставляются согласно порядку из
# ключа
#
# Пример алгоритма шифрования:
# Ключ: "acb"
# Текст: "helloworld"
# Блоки: ["hel", "low", "orl", "d "]
# Блоки после перестановки: ["hle", "lwo", "olr", "d "]
# Результат: "hlelwoolrd "
# Правила дешифрование:
#
# • исходный порядок восстанавливает символы в каждом блоке
# • лишние пробелы после дешифровки удаляются
#
# Валидации и работа с ошибками:
#
# • проверяется, что ключ состоит только из букв английского алфавита
# • проверяется, что все буквы в ключе уникальны, игнорируя регистр
# • если ключ не соответствует требованиям, вызывается исключение
# ValueError с понятным сообщением об ошибке
#
# Тесты для примеров и проверки:
# Пример 1: Шифрование с явной итерацией по блокам
# text = "HELLOWORLD"
# key = "bAc"
# print("Процесс шифрования по блокам:")
# cipher = BlockTranspositionCipher(text, key)
# for i, encrypted_block in enumerate(cipher, 1):
# print(f"Блок {i}: '{encrypted_block}'")*
#
# 15
#
# Пример 2: Полное шифрование
# cipher = BlockTranspositionCipher(text, key)
# encrypted = ''.join(cipher)
# print(f"\nПолный зашифрованный текст: '{encrypted}'")
# Пример 3: Дешифрование с итерацией
# print("\nПроцесс дешифрования по блокам:")
# decipher = BlockTranspositionCipher(encrypted, key, decrypt=True)
# for i, decrypted_block in enumerate(decipher, 1):
# print(f"Блок {i}: '{decrypted_block}'")
# Пример 4: Полное дешифрование с обрезкой пробелов
# decipher = BlockTranspositionCipher(encrypted, key, decrypt=True)
# decrypted = ''.join(decipher)
# print(f"\nПолный расшифрованный текст: '{decrypted}'")

class BlockTranspositionCipher:
    """
        Класс принимает 2 обязательных параметра.
     Итак, что я тут намудрил...Проверяю, делится ли текст на блоки длины ключа без остатка.
     Если остаток есть - создаю список длинною нужного количества блоков и заполняю их None.
     Прохожу в цикле и каждый None заменяю на элементы тескта.Таким образом получаем
     определенное количество блоков длинною равной длине ключа, а последний блок
     заполняется нехватающим числом пробелов
     """

    def __init__(self, text, key, decrypt = False):
        self.text = text.lower()
        self.key = self.validate_key(key)
        self.cript_res = []


        if (len(self.text) % len(self.key)):
            res = [None] * ((len(self.text) // len(self.key)) + 1)
            for i in range((len(self.text) // len(self.key)) + 1):
                res[i] = self.text[i * len(self.key):i * len(self.key) + len(self.key)]
        else:
            res = [None] * ((len(self.text) // len(self.key)))
            for i in range((len(self.text) // len(self.key))):
                res[i] = self.text[i * len(self.key):i * len(self.key) + len(self.key)]
        r = res[-1] + len(self.key) * ' '
        res[-1] = r[:len(self.key)]


        for i in res:
            block =''
            for j in self.key:
                block += (i[int(j)]) #Делаю перестновку в блоке согласно элементам ключа
                if len(block) == len(self.key) and ' ' not in block:
                    self.cript_res.append(block)
                    block=''
                if len(block) == len(self.key) and ' ' in block  and decrypt==False:
                    s = block.count(' ')
                    stprip_block = block.strip() + ' '*s
                    self.cript_res.append(stprip_block[:len(self.key)]) #Перемещаю пробелы в конец блока
                if len(block) == len(self.key) and ' ' in block  and decrypt==True:
                    # s = block.count(' ')
                    stprip_block = block.strip()
                    self.cript_res.append(stprip_block.strip())


    def __iter__(self):
        """Устанавливаем значение -1, чтобы при инициализации итератора
        начальное значение стало 0 -т.е. первый элемент списка"""
        self.i = -1
        return self
    def __next__(self):
        """Проходимся по всем блокам, иначе исключение StopIteration"""
        if self.i + 1 < len(self.cript_res):
            self.i += 1
            return self.cript_res[self.i]
        else:
            raise StopIteration

    @staticmethod
    def validate_key(k:str):
        """Валидируем ключ и возвращаем список чисел, соответствующих каждой букве ключа"""
        key =k.lower()
        if not key.isalpha():
            raise ValueError('Ключ должен содержать английские буквы a..z')
        if len(set(key)) != len(key):
            raise ValueError('Ключ не должен сожержать повторяющиеся буквы')
        list_int_key = []
        for i in key:
            list_int_key.append(ord(i) - 97)
        return  list_int_key

def test1(key):
    """
    Небольшой тест посмотреть исключения и шифрованный\дешифрованный результат
    """
    text = "HELLOWORLD"

    try:
        cipher = BlockTranspositionCipher(text, key)
        encrypted = ''.join(cipher)
        decipher = BlockTranspositionCipher(encrypted, key, decrypt=True)
        decrypted = ''.join(decipher)
        return (encrypted, decrypted)
    except ValueError as e:
        return (str(e))


assert test1('abca') == 'Ключ не должен сожержать повторяющиеся буквы'
assert test1('ac2b') == 'Ключ должен содержать английские буквы a..z'
assert (test1('acb')) == ('hlelwoolrd  ', 'helloworld')


        #Просто тесты из задания, видны блоки итерации
text = "HELLOWORLD"
key = "bAc"
print("Процесс шифрования по блокам:")
cipher = BlockTranspositionCipher(text, key)
for i, encrypted_block in enumerate(cipher, 1):
    print(f"Блок {i}: '{encrypted_block}'")

cipher = BlockTranspositionCipher(text, key)
encrypted = ''.join(cipher)
print(f"\nПолный зашифрованный текст: '{encrypted}'")

print("\nПроцесс дешифрования по блокам:")
decipher = BlockTranspositionCipher(encrypted, key, decrypt=True)
for i, decrypted_block in enumerate(decipher, 1):
    print(f"Блок {i}: '{decrypted_block}'")

decipher = BlockTranspositionCipher(encrypted, key, decrypt=True)
decrypted = ''.join(decipher)
print(f"\nПолный расшифрованный текст: '{decrypted}'")