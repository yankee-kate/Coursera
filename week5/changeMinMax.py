def changeMM(lst):
    minim = lst.index(min(lst))
    maxim = lst.index(max(lst))
    lst[minim], lst[maxim] = lst[maxim], lst[minim]
    return lst


myLst = list(map(int, input().split()))
print(*changeMM(myLst))
