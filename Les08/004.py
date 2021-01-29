"""4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники."""

from abc import ABC, abstractmethod


class OfficeEquipment(ABC):
    def __init__(self, tab_num, place):
        self.tab_num = tab_num
        self.place = place


class Printer(OfficeEquipment):
    def __init__(self, tab_num, model, print_speed, place):
        super().__init__(tab_num, place)
        self.model = model
        self.print_speed = print_speed


class Scanner(OfficeEquipment):
    def __init__(self):
        pass


class Xerox(OfficeEquipment):
    def __init__(self):
        pass


class Warehouse:
    def __init__(self):
        pass