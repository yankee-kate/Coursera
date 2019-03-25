def changeNearest(lst):
    i = 0
    newLst = lst
    while i + 1 < len(newLst):
        newLst[i], newLst[i + 1] = newLst[i + 1], newLst[i]
        i += 2
    return newLst


myLst = list(map(int, input().split()))
print(*changeNearest(myLst))
