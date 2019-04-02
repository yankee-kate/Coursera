def countSort(lst):
    count = [0] * 101
    for num in lst:
        count[num] += 1
    newLst = []
    for num in range(len(count)):
        newLst += [num] * count[num]
    return newLst


lst = list(map(int, input().split()))
print(*countSort(lst))
