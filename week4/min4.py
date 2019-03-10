def min4(a, b, c, d):
    min1 = min(a, b)
    min2 = min(c, d)
    return min(min1, min2)


a = input()
b = input()
c = input()
d = input()

print(min4(a, b, c, d))
