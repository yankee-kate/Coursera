lst = list(map(int, input().split()))
mySet = {lst[0]}
i = 1
print('NO')
while i < len(lst):
    if lst[i] in mySet:
        print('YES')
    else:
        print('NO')
        mySet.add(lst[i])
    i += 1
