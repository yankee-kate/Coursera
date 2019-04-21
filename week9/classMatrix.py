from sys import stdin
import copy


class MatrixError(BaseException):
    def __init__(self, matrix1, matrix2):
        self.first = matrix1
        self.second = matrix2


class Matrix:
    def __init__(self, lst):
        self.lst = copy.deepcopy(lst)

    def __str__(self):
        lst_to_str = ''
        for i in range(len(self.lst) - 1):
            lst_to_str += '\t'.join(map(str, self.lst[i])) + '\n'
        lst_to_str += '\t'.join(map(str, self.lst[-1]))
        return lst_to_str

    def size(self):
        size_cort = (len(self.lst), len(self.lst[0]))
        return size_cort

    def __add__(self, other):
        res_array = list()
        error = MatrixError(self, other)
        if len(self.lst) != len(other.lst):
            raise error
        for i in range(len(self.lst)):
            new_lst = list()
            if len(self.lst[i]) != len(other.lst[i]):
                raise error
            for j in range(len(self.lst[i])):
                new_lst.append(self.lst[i][j] + other.lst[i][j])
            res_array.append(new_lst)
        return Matrix(res_array)

    def __mul__(self, other):
        if other == 0:
            return 0
        elif isinstance(other, int) or isinstance(other, float):
            res_array = list()
            for i in range(len(self.lst)):
                new_lst = list()
                for j in range(len(self.lst[i])):
                    new_lst.append(self.lst[i][j] * other)
                res_array.append(new_lst)
        else:
            error = MatrixError(self, other)
            raise error
        return Matrix(res_array)

    __rmul__ = __mul__

    def transpose(self):




m1 = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
m2 = Matrix([[0, 1, 0], [20, 0, -1], [20, 0]])

try:
    print(m1 + m2)
except MatrixError as me:
    print('Cannot summarize next arrays: \n', me.first,
          '\n, second param: \n', me.second, sep='')

exec(stdin.read())
