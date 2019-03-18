def quickLevel(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return quickLevel(a, n / 2)**2
    else:
        return a * quickLevel(a, n - 1)


a = float(input())
n = float(input())
print(quickLevel(a, n))
