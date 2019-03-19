def zeroCount(n):
    j = 0
    for i in range(n):
        if int(input()) == 0:
            j += 1
    return j


n = int(input())
print(zeroCount(n))
