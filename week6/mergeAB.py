def merge(a, b):
    pa = 0
    pb = 0
    result = []

    while pa < len(a) and pb < len(b):
        if a[pa] <= b[pb]:
            result.append(a[pa])
            pa += 1
        else:
            result.append(b[pb])
            pb += 1

    remained = a[pa:] + b[pb:]
    result.extend(remained)

    return result


A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(*merge(A, B))
