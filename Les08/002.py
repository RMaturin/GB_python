"""2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
ситуацию и не завершиться с ошибкой."""


class MyZeroDivError(Exception):
    def __str__(self):
        return 'Делить на ноль нельзя'


def division_func(a,  b):
    if b == 0:
        raise MyZeroDivError
    else:
        return a / b


try:
    r = division_func(6, 0)
    print(r)
except MyZeroDivError as err:
    print(err)