"""1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт."""

from time import sleep
from itertools import cycle

"""Т.к. нужно реализовать проверку порядка режимов, то running будет зажигать указанный цвет"""

class TrafficLight:

    def __init__(self):
        self.__color = None
        self.__color_dict = {'Red': 7, 'Yellow': 2, 'Green': 5}

    # метод running запускает указанный цвет.
    # Если указанные цвет не соответствует порядку райзим ошибку,
    # иначе ждем пока догарит текущий цвет и переключаем на указанный
    def running(self, color):
        self.__check_color(color)
        if self.__color is None:
            self.__color = color
        else:
            sleep(self.__color_dict[self.__color])
            self.__color = color

    def switch_off(self):
        self.__color = None

    def get_color(self):
        return self.__color

    def __check_color(self, color):
        if self.__color is None and color!='Red':
            raise ValueError('Must running from Red Light')
        elif (self.__color == 'Green' and color != 'Red') \
                or (self.__color == 'Red' and color != 'Yellow') \
                or (self.__color == 'Yellow' and color != 'Green'):
            raise ValueError('Wrong color')


light_list = ('Red', 'Yellow', 'Green')
a = TrafficLight()
cnt = 0
for i in cycle(light_list):
    a.running(i)
    print(a.get_color())
    cnt += 1
    if cnt == 10:
        a.switch_off()
        break

b = TrafficLight()
# raise ValueError('Must running from Red Light')
b.running('Green')

# raise ValueError('Wrong color')
b.running('Red')
b.running('Green')


