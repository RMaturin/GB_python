# 2. Пользователь вводит время в секундах. Переведите время в часы,
#    минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

sec = int(input('Введите время в секундах: '))

hh = sec // 3600
mm = (sec % 3600) // 60
ss = (sec % 3600) % 60

print (f'{hh:02}:{mm:02}:{ss:02}')