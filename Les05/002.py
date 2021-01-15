"""2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке."""

with open('file20210115.txt', 'r', encoding='UTF-8') as f_obj:
    line_cnt = 0
    for line in f_obj:
        line_cnt += 1
        print(f'Строка {line_cnt}: {len(line.split())} слов')
print('Всего сток: ', line_cnt)