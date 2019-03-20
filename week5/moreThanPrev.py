myList = input().split()
myNewList = []
for i in range(len(myList) - 1):
    if int(myList[i + 1]) > int(myList[i]):
        myNewList.append(myList[i + 1])
print(*myNewList)
