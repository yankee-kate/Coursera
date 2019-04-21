import copy
from sys import stdin


class MatrixError(BaseException):
    def __init__(self, Matrix, other):
        self.matrix1 = Matrix
        self.matrix2 = other


class Matrix:
    def __init__(self, lst):
        self.lst = copy.deepcopy(lst)

    def __str__(self):
        rows = []
        for row in self.lst:
            rows.append('\t'.join(map(str, row)))
        return '\n'.join(rows)

    def size(self):
        size_cort = (len(self.lst), len(self.lst[0]))
        return size_cort

    def __add__(self, other):
        if len(self.lst) == len(other.lst):
            res_array = copy.deepcopy(self.lst)
            for i in range(len(self.lst)):
                for j in range(len(self.lst[i])):
                    res_array[i][j] += other.lst[i][j]
        else:
            raise MatrixError(self, other)
        return Matrix(res_array)

    def __mul__(self, other):
        if other == 0:
            return 0
        elif isinstance(other, int) or isinstance(other, float):
            res_array = copy.deepcopy(self.lst)
            for i in range(len(self.lst)):
                for j in range(len(self.lst[i])):
                    res_array[i][j] *= other
        else:
            raise MatrixError(self, other)
        return Matrix(res_array)

    __rmul__ = __mul__

    @staticmethod
    def transposed(m):
        return Matrix(list(map(list, zip(*m.lst))))

    def transpose(self):
        new_lst = list(map(list, zip(*self.lst)))
        self.lst = new_lst
        return self


exec(stdin.read())
