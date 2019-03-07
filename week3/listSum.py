n = int(input())

i = 1
sum = 0.0
while i <= n:
    sum += 1 / i**2
    i += 1
print('{0:.6f}'.format(sum))
