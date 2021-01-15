# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(p1, p2, p3):
    iter_obj=[p1, p2, p3]
    return sum(iter_obj)-min(iter_obj)


print(my_func(4, 3, 3))