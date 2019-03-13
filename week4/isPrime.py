import math


def IsPrime(n):
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            return False
        i += 1
    return True


n = int(input())
if IsPrime(n):
    print('YES')
else:
    print('NO')
