def create_cortage(lst):
    cortage = []
    for i in range(len(lst)):
        cortage.append((i, lst[i]))
    return cortage


def lensort(cort):
    return cort[1]


def nearestGrob(safe_place, vilage, n, m):
    safe_place = create_cortage(safe_place)
    vilage = create_cortage(vilage)
    safe_place.sort(key=lensort)
    vilage.sort(key=lensort)

    nearestGrobLst = []
    i = j = 0
    while i < len(vilage):
        if vilage[i][1] <= safe_place[j][1]:
            nearestGrobLst.append(safe_place[j][0])
            i += 1
            j += 1
        elif safe_place[j][1] < vilage[i][1]:
            if safe_place[j + 1]:
                if abs(vilage[i][1] - safe_place[j][1]) <= abs(vilage[i][1] - safe_place[j + 1][1]):
                    nearestGrobLst.append(safe_place[j][0])
                    i += 1
                    j += 1
                else:
                    nearestGrobLst.append(safe_place[j + 1])
                    i += 1
                    j += 1
            else:
                nearestGrobLst.append(safe_place[j])
        else:
            j += 1
    return nearestGrobLst


n = int(input())
vilages = list(map(int, input().split()))
m = int(input())
safe_places = list(map(int, input().split()))

print(*nearestGrob(vilages, safe_places))
