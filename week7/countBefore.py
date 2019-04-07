fin = open('input.txt')
myDict = dict()
myLst = list()
myCort = list()
for line in fin:
    myLst = line.strip().split()
    for item in range(len(myLst)):
        if myLst[item] in myDict:
            myDict[myLst[item]] += 1
            myCort.append(myDict[myLst[item]])
        else:
            myDict[myLst[item]] = 0
            myCort.append(0)
print(*myCort)
