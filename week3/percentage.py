import math
procent = int(input())
rub = int(input())
kop = int(input())

vklad = ((rub * 100 + kop) + (rub * 100 + kop) * procent / 100) / 100
rub = math.trunc(vklad)
kop = math.ceil((vklad % 1) * 100)

print(rub, kop)
