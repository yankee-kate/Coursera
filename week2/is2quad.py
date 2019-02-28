n = int(input())


if n > 1:
    while n > 1:
        if n % 2 == 0:
            b = "YES"
            n = n // 2
        else:
            b = "NO"
            n = 0
elif n == 1:
    b = "YES"
print(b)
