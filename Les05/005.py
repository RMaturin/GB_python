"""5. Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран."""

from random import randint


def gen_file(file_name):
    with open(file_name, 'w', encoding='UTF-8') as f:
        print(' '.join([str(randint(1, 100)) for i in range(randint(5, 15) + 1)]), end='', file=f)


my_file = 'numbers_string.txt'
gen_file(my_file)
with open(my_file, 'r', encoding='UTF-8') as f:
    line = f.read()
    print(line)
    print(sum(map(int, line.split(' '))))

