myList = input().split()
val = 0
j = 0
for i in range(len(myList)):
    if int(myList[i]) >= val:
        val = int(myList[i])
        j = i
print(val, j)
