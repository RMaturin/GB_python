"""7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.

Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста."""

import json

profit_dict = dict()
damages_dict = dict()
avg_dict = dict()
with open('firms.txt', 'r', encoding='UTF-8') as f_obj:
    total_profit = 0
    profit_firm_cnt = 0
    for line in f_obj.read().split('\n'):
        split_line  = line.split()
        profit = int(split_line[2])-int(split_line[3])
        if profit >= 0:
            profit_dict[split_line[0]] = profit
            total_profit += profit
            profit_firm_cnt += 1
        else:
            damages_dict[split_line[0]] = profit
    avg_dict['average_profit']=total_profit/profit_firm_cnt

l = [profit_dict, damages_dict, avg_dict]

with open('firms.json', 'w', encoding='UTF-8') as j_obj:
    json.dump(l, j_obj)
