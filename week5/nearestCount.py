def nearest(lst, target):
    myNewList = []
    for i in range(len(lst)):
        myNewList.append(abs(target - lst[i]))
    return lst[myNewList.index(min(myNewList))]


num = input()
myList = list(map(int, input().split()))
n = int(input())
print(nearest(myList, n))
