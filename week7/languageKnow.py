n = int(input())
lstName = []
i = 0
while i < n:
    m = int(input())
    j = 0
    lstName.append([])
    while j < m:
        lstName[i].append(input())
        j += 1
    i += 1

not_intersectionSet = intersectionSet = (set(tuple(lstName[0])))
i = 1
while i < n:
    intersectionSet = intersectionSet & (set(tuple(lstName[i])))
    not_intersectionSet = not_intersectionSet | (set(tuple(lstName[i])))
    i += 1

# not_intersectionSet = not_intersectionSet - intersectionSet

intersectionTup = tuple(intersectionSet)
not_intersectionTup = tuple(not_intersectionSet)

print(len(intersectionTup))
for i in range(len(intersectionTup)):
    print(intersectionTup[i])

print(len(not_intersectionTup))
for i in range(len(not_intersectionTup)):
    print(not_intersectionTup[i])
