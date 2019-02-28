x = int(input())
while True:
    y = int(input())
    if y == 0:
        break
    elif x < y:
        x = y
print(x)
