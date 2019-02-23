k = int(input())

# if k != 0 and (k % 3 == 0 or k % 5 == 0 or k % 8 == 0):
#     print("YES")
# elif (k % 5) % 3 == 0 or (k % 3) % 5 == 0:
#     print("YES")
# else:
#     print("NO")
b = "NO"
for x in range(k + 1):
    for y in range(k + 1):
        if k == 3 * x + 5 * y:
            b = "YES"
print(b)
