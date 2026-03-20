# Разработать метод date_in_future(integer), который вернет дату через integer дней.
# Если integer не является целым числом, то метод должен вывести текущую дату.
# Формат возвращаемой методом даты должен иметь следующий вид '24-03-2001
# 22:33:44'.
# Тесты для примеров и проверки:
# date_in_future([]) # => текущая дата
# date_in_future(2) # => текущая дата + 2 дня

from datetime import datetime,timedelta

def date_in_future(integer:any):
    """
    Метод возращает текущую дату + количество дней, если передан int.
    Иначе просто выводится текущая дата, формат '24-03-2001 22:33:44'
    """
    if isinstance(integer, int):
        now = datetime.now()
        days = timedelta(days=integer)
        future = now + days
        res_date = future.strftime(f'%d-%m-%Y %H:%M:%S')
        return res_date
    else:
        now = datetime.now()
        res = now.strftime(f'%d-%m-%Y %H:%M:%S')
        return res
print(date_in_future(2)) #текущая дата +2 дня в формате '24-03-2001 22:33:44'
print(date_in_future([])) #текущая дата
print(date_in_future('4')) #текущая дата
