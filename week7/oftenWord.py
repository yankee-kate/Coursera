fin = open('input.txt')
myLst = list()
myDict = dict()
for line in fin:
    myLst = line.strip().split()
    for item in range(len(myLst)):
        if myLst[item] in myDict:
            myDict[myLst[item]] += 1
        else:
            myDict[myLst[item]] = 0
mx = max(myDict.values())
print(min([k for k, v in myDict.items() if v == mx]))
