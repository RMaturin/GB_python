# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать
# параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def get_user_info(f_name='', l_name='', birth_y='', hometown='', email='', phone=''):
    return '; '.join([str(f_name), str(l_name), str(birth_y), str(hometown), str(email), str(phone)])


print(get_user_info(f_name='Bob', l_name='Green', hometown='London', birth_y=1975))

d = {'f_name': 'Steve', 'l_name': 'Cook', 'hometown': 'York', 'birth_y': 1975, 'email': 'scook@gmail.com'}
print(get_user_info(**d))