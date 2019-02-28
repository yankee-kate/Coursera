h = int(input())
up = int(input())
down = int(input())

if (h - up) % (up - down) > 0:
    time = (h - up) // (up - down) + 2
else:
    time = (h - up) // (up - down) + 1

print(time)
