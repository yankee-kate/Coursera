# First moment:
h1 = int(input())
m1 = int(input())
s1 = int(input())
# Second moment:
h2 = int(input())
m2 = int(input())
s2 = int(input())

moment1 = (h1 * 3600) + (m1 * 60) + s1
moment2 = (h2 * 3600) + (m2 * 60) + s2

print(moment2 - moment1)
