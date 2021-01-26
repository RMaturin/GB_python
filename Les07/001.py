"""1. Реализовать класс Matrix (матрица).
Обеспечить перегрузку конструктора класса (метод __init__()), который должен
принимать данные (список списков) для формирования матрицы.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
класса Matrix (двух матриц). Результатом сложения должна быть новая матрица."""


class Matrix:
    def __init__(self, m_body):
        # размер матрицы m * n
        self.m = len(m_body)
        self.n = max([len(el) for el in m_body])
        # инициализируем матрицу. Если не хватает элементов в строке, добиваем нулями
        self.__body = list()
        self.__max_el_width = 0
        for i in range(self.m):
            self.__body.append(list())
            for j in range(self.n):
                if j < len(m_body[i]):
                    self.__body[i].append(m_body[i][j])
                    self.__max_el_width = max(self.__max_el_width, len(str(m_body[i][j])))
                else:
                    self.__body[i].append(0)

    def __str__(self):
        return '\n'.join([','.join(map(lambda x: str(x).rjust(self.__max_el_width+1, ' '), i)) for i in self.__body])

    def __add__(self, other):
        if self.m != other.m or self.n != other.n:
            raise ValueError('Matrices have different sizes')
        else:
            result = list()
            for i in range(self.m):
                result.append(list())
                for j in range(self.n):
                    result[i].append(self.__body[i][j] + other.__body[i][j])
            return Matrix(result)


in_m = [[1, 2, 39], [4, 5, 6], [7, 38, -9], [1, 1, 1]]

my_m1 = Matrix(in_m)
my_m2 = Matrix(in_m)

r = my_m1 + my_m2 + my_m1
print(my_m1)
print(r)
