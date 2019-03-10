procent = int(input())
rub = int(input())
kop = int(input())

vklad = rub * 100 + kop
proc = vklad + (vklad * procent / 100)
rub = int(proc // 100)
kop = int(proc % 100)

print(rub, kop)
