n = int(input())

i = 1
k = 2
if n >= 2:
    while i < 2:
        if n % k == 0:
            print(k)
            i += 1
        else:
            k += 1
