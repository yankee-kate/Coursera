myList = input().split()
i = 0
while i < len(myList):
    if int(myList[i]) % 2 != 0:
        myList.pop(i)
    else:
        i += 1
print(*myList)
