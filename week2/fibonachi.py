n = int(input())

n1 = n2 = 1
while n - 2 > 0:
    (n1, n2) = (n2, n1 + n2)
    n -= 1

print(n2)
