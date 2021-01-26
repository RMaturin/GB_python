# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

from datetime import datetime

file_name = f"file{datetime.strftime(datetime.now(), '%Y%m%d')}.txt"
print(f'Идет запись в файл {file_name}')

with open(file_name, 'w', encoding='UTF-8') as f_obj:
    while True:
        line = input()
        if len(line) > 0:
            f_obj.write(line+'\n')
        else:
            break
