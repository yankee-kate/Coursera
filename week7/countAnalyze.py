fin = open('input.txt')
myDict = dict()
myLst = list()
for line in fin:
    myLst = line.strip().split()
    for word in range(len(myLst)):
        if myLst[word] in myDict:
            myDict[myLst[word]] += 1
        else:
            myDict[myLst[word]] = 0
myLst.clear()
for pair in myDict:
    myLst.append((pair, myDict[pair]))
myLst = sorted(myLst, key=lambda k: (-k[1], k[0]))
for i in range(len(myLst)):
    print(myLst[i][0])
