x = float(input())
y = float(input())

i = 1
while x < y:
    x += x / 10
    i += 1
print(i)
