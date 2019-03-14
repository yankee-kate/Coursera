def sum_rec(a, b):
    if b != 0:
        return sum_rec(a, b - 1) + 1
    else:
        return a


a = float(input())
b = float(input())
print(sum_rec(a, b))
