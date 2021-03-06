# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить
# сумму этих чисел к полученной ранее сумме и после этого завершить программу.

def sum_list(in_list):
    res = str_sum
    for i in in_list:
        if i.isdigit():
            res += int(i)
        elif i == 'q':
            break
    return res


print('ВВедите строку чисел, разделенных пробелом.')
print('Для завершения обработки последовательности введите "q".')
print('-'*20)
str_sum = 0
while True:
    s = input('ВВедите числа (или "q"): ')
    l = s.lower().split(' ')
    str_sum = sum_list(l)
    print(str_sum)
    if 'q' in l:
        print('Ввод чисел завершен.')
        break
