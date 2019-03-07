import math
price = float(input())

rub = math.trunc(price)
kop = (price % 1) * 100

print(rub, round(kop))
