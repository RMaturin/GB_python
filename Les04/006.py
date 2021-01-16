# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.

# Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание,
# что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.

# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

from itertools import count
from itertools import cycle


def iter_a(start_num):
    for el in count(start_num):
        yield el


def iter_b(in_list):
    for el in cycle(in_list):
        yield el


i1 = iter_a(3)
for i in i1:
    if i > 10:
        break
    else:
        print(i)

i2 = iter_b('abcdef')
c = 1
for i in i2:
    if c > 10:
        break
    else:
        print(i)
        c += 1