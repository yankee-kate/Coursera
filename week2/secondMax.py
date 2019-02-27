now = int(input())

n1 = n2 = 0
while now != 0:
    if now > n2:
        n1, n2 = n2, now
    elif now > n1:
        n1 = now
    now = int(input())
print(n1)
