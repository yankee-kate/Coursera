import math
num = float(input())

part = num % 1

if part < 0.5:
    num = math.trunc(num)
else:
    num = math.trunc(num) + 1
print(num)
