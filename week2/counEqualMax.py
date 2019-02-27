now = int(input())

max = 0
i = 0
while now != 0:
    if now == max:
        i += 1
    elif now > max:
        max = now
        i = 1
    now = int(input())
print(i)
