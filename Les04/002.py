# 2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

start_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result_list = [start_list[i] for i in range(1, len(start_list)) if start_list[i-1] < start_list[i]]
print(start_list)
print(result_list)

""" Жестко затупил и создал вот такого монстра)) А потом посмотрел разбор домашки
Я очень долго не мог придумать, как же мне в '... for el in start_list ...' обратиться к предидущему значению списка
result_list = [
    x[1]
    for x in [(i, el) for i, el in enumerate(start_list) if i > 0]
    for n, y in enumerate(start_list, 1)
    if x[0] == n and x[1] > y
]
"""

