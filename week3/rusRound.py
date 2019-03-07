import math
num = float(input())

part = int(num % 1)

if part < 5:
    num = math.trunc(num)
else:
    num = math.trunc(num) + 1
print(num)
