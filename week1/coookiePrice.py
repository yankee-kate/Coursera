A = int(input())
B = int(input())
N = int(input())

total = (A * 100 + B) * N
rub = total // 100
kop = total % 100

print(rub, kop)
