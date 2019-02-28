n = input()

i = 1
count = 0
while i <= int(n):
    k = 1
    new = ''
    while k <= len(str(i)):
        new = new + str(i)[- k]
        k += 1
    if int(new) == i:
        count += 1
    i += 1
print(count)
