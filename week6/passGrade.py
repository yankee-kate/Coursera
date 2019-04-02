def mySplit(line):
    thirdGrade = int(line[line.rfind(' '):])
    newline = line[:line.rfind(' ')]
    secondGrade = int(newline[newline.rfind(' '):])
    newline = newline[:newline.rfind(' ')]
    firstGrade = int(newline[newline.rfind(' '):])
    newline = newline[:newline.rfind(' ')]
    name = newline
    summ = firstGrade + secondGrade + thirdGrade
    return (name, firstGrade, secondGrade, thirdGrade, summ)


def maxGrade(lst, numPositions):
    lst.sort(key=lambda x: x[4], reverse=True)
    if numPositions + 1 >= len(lst):
        return 0  # more positions than students
    else:
        flag = False
        for i in range(numPositions + 1):
            if lst[i][4] == lst[i + 1][4]:
                flag = True
            else:
                flag = False
                break
        if flag is True:
            return 1  # all the same
    while numPositions >= 0:
        if lst[numPositions][4] == lst[numPositions + 1][4]:
            numPositions -= 1
        else:
            break
    if numPositions < 0:
        return 1
    else:
        return lst[numPositions][4]


fin = open('input.txt', encoding='utf8')
fout = open('output.txt', 'w', encoding='utf8')
k = int(fin.readline().strip()) - 1
gradesLst = []
for student in fin:
    gradesLst.append(mySplit(student.strip()))
i = 0
while i < len(gradesLst):
    if gradesLst[i][1] < 40 or gradesLst[i][2] < 40 or gradesLst[i][3] < 40:
        gradesLst.pop(i)
    else:
        i += 1
# print(maxGrade(gradesLst, k))
# print(gradesLst)
print(maxGrade(gradesLst, k), file=fout)
