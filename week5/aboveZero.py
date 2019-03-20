myList = input().split()
j = 0
for i in range(len(myList)):
    if int(myList[i]) > 0:
        j += 1
print(j)
