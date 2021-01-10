# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def div_func(p1, p2):
    try:
        return p1 / p2
    except ZeroDivisionError:
        return 'division by zero!'


print(div_func(4, 2))
print(div_func(4, 8))
print(div_func(4, 0))
