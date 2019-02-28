k = int(input())

b = "NO"
for x in range(k + 1):
    for y in range(k + 1):
        if k == 3 * x + 5 * y:
            b = "YES"
print(b)
