n = int(input())

if n == 0:
    print(0)
elif n == 1:
    print(1, 2)
else:
    fib = 0
    num = 2
    n1 = n2 = 1
    while n2 < n:
        n1, n2 = n2, n1 + n2
        num += 1
    if n2 == n:
        print(num)
    else:
        print(-1)
