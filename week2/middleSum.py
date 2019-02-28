now = int(input())

sum = 0
i = 0
while now != 0:
    sum += now
    now = int(input())
    i += 1

print(sum / i)
