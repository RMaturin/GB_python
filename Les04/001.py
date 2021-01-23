# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv


def emp_salary(in_h, in_rate, in_prem):
    return int(in_h) * int(in_rate) + int(in_prem)


path, h, rate, prem = argv
print(path)
print(emp_salary(h, rate, prem))
