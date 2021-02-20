"""4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.

5. Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую
подходящую структуру, например словарь."""

from abc import ABC, abstractmethod


class OfficeEquipment(ABC):
    def __init__(self, tab_num, model, place):
        self.tab_num = tab_num
        self.model = model
        self.place = place

    @abstractmethod
    def switch_on(self):
        pass

    @abstractmethod
    def switch_off(self):
        pass


class Printer(OfficeEquipment):
    def __init__(self, tab_num, model, place, is_color, tray_size, print_speed):
        super().__init__(tab_num, model, place)
        self.is_color = is_color
        self.tray_size = tray_size
        self.print_speed = print_speed

    def switch_on(self):
        print(f'Принтер {self.model} т/н:{self.tab_num} включен.')

    def switch_off(self):
        print(f'Принтер {self.model} т/н:{self.tab_num} выключен.')

    @staticmethod
    def print_file(file_name, copy_num):
        print(f'Напечатан файл {file_name} копий: {copy_num}.')


class Scanner(OfficeEquipment):
    def __init__(self, tab_num, model, place, max_paper_size):
        super().__init__(tab_num, model, place)
        self.max_paper_size = max_paper_size

    def switch_on(self):
        print(f'Сканер {self.model} т/н:{self.tab_num} включен.')

    def switch_off(self):
        print(f'Сканер {self.model} т/н:{self.tab_num} выключен.')

    @staticmethod
    def scan_document():
        print('Документ отсканирован')
        return 'scan_file'


class Xerox(OfficeEquipment):   # я не смог отнаследоваться от (Printer, Scanner)
    # хотел переиспользовать их параметры и методы
    # затык поймал на __init__
    def __init__(self, tab_num, model, place, is_color, tray_size, max_paper_size, copy_speed):
        super().__init__(tab_num, model, place)     # я не понял как раскидать по двум родителям атрибуты, из которых (tab_num, model, place) общие
        # так не получилось
        # Printer.__init__(self, tab_num, model, place, is_color, tray_size, None)
        # Scanner.__init__(self, tab_num, model, place, max_paper_size)
        self.is_color = is_color    # это должно наследоваться
        self.tray_size = tray_size      # это должно наследоваться
        self.max_paper_size = max_paper_size    # это должно наследоваться
        self.copy_speed = copy_speed    # а это атрибут Xerox

    def switch_on(self):
        print(f'Ксерокс {self.model} т/н:{self.tab_num} включен.')

    def switch_off(self):
        print(f'Ксерокс {self.model} т/н:{self.tab_num} выключен.')

    # метод копирования хотел реализовать вот так
    # def scan_document(self, copy_num):
    #     self.print_file(self.scan_document(), copy_num)
    #     print(f'Документ отксерокопирован копий: {copy_num}.')
    def scan_document(self, copy_num):
        print(f'Документ отксерокопирован копий: {copy_num}.')


class Warehouse:
    def __init__(self):
        pass


pr1 = Printer('111', 'HP-3000', 'ГО', True, 500, 30)
pr1.switch_on()
pr1.print_file('fff.txt', 1)
pr1.switch_off()

pr1 = Scanner('133', 'HP-S600', 'ГО',  30)
pr1.switch_on()
pr1.scan_document()
pr1.switch_off()

x1 = Xerox('112', 'Xerox-3D200', 'ДО-1', False, 1000, 'A3', 30)
x1.switch_on()
x1.scan_document(1)
x1.switch_off()
