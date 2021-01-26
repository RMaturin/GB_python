"""4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл."""

d = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('digits.txt', 'r', encoding='UTF-8') as f_obj:
    with open('digits_new.txt', 'w', encoding='UTF-8') as f_obj_new:
        while True:
            line = f_obj.readline().split()
            if not line:
                break
            line[0] = d[line[0]]
            f_obj_new.write(' '.join(line)+'\n')
