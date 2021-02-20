"""1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных."""


class Date:
    def __init__(self, date_str):
        self.date_str = date_str

    @classmethod
    def get_int(cls, date_str):
        d = date_str.split('-')
        cls.dd = int(d[0])
        cls.mm = int(d[1])
        cls.yyyy = int(d[2])

    @staticmethod
    def valid_date(date_str):
        d = date_str.split('-')
        if d[0].isdigit() and d[1].isdigit() and d[2].isdigit():
            if int(d[1]) in [1,3,5,7,8,10,12] and int(d[0]) >= 1 and int(d[0]) <= 31:
                return True
            elif int(d[1]) in [4,6,9,11] and int(d[0]) >= 1 and int(d[0]) <= 30:
                return True
            elif int(d[1]) == 2 and int(d[0]) >= 1 and int(d[0]) <= 28:
                return True
            elif int(d[1]) == 2 and int(d[2]) % 4 == 0 and int(d[0]) == 29:
                return True
            else:
                return False
        else:
            return False


Date.get_int('01-01-2021')
print(Date.dd)
print(Date.mm)
print(Date.yyyy)


print(Date.valid_date('01-01-2021'))
print(Date.valid_date('31-04-2020'))
