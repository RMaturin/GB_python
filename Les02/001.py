# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа. Элементы списка можно
# не запрашивать у пользователя, а указать явно, в программе.

l = [1, True, 'строка', 3.14, b'xxx', None, [1, 2], ('f', 'g'), {1, 2, 3}, {'k1': 'a', 'k2': 'b'}]

for i in l:
    print(i, type(i))