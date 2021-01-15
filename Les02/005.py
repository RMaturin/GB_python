# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы
# с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.

my_list = [7, 5, 10, 3, 3, 2] # Тут можно организовать ввод
my_list.sort(reverse=True)
print(my_list)

x = True
while x:
    new_val = int(input('Введите число: '))
    need_del = 0
    for i in range(len(my_list)):
        if new_val > my_list[i]:
            my_list.insert(i, new_val)
            need_del = 1
            break
    if need_del == 1:
        my_list.pop(-1)
    print(my_list)
    if int(input('Выйти? (1/0) ')) == 1:
        x = False
