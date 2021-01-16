"""6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно
были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}"""


def find_numbers(in_str):
    l = list()
    find_next_flg = False
    num = ''
    for i in in_str:
        if i.isdigit():
            num += i
            find_next_flg = True
        else:
            if not find_next_flg and len(num)>0:
                l.append(int(num))
                num = ''
            find_next_flg = False
    if len(num) > 0:
        l.append(int(num))
    return l


subj_dict = dict()
with open('subjects.txt', 'r', encoding='UTF-8') as f_obj:
    while True:
        line = f_obj.readline()
        if not line:
            break
        if line.find(':') > 0:
            subj_name = line[0:line.find(':')]
            subj_hours = sum(find_numbers(line[line.find(':')+1:]))
            subj_dict[subj_name] = subj_hours
print(subj_dict)