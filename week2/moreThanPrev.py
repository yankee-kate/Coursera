now = int(input())

i = 0
if now != 0:
    next = int(input())
    while next != 0:
        if next > now:
            i += 1
        now = next
        next = int(input())
print(i)
