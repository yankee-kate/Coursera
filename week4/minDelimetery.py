import math


def MinDivisor(n):
    i = 1
    while i < math.sqrt(n):
        i += 1
        if n % i == 0:
            return i
    return n


n = int(input())
print(MinDivisor(n))
