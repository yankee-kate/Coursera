fin = open('input.txt')
mx = int(fin.readline())
mySet = set()
noSet = set()
for i in range(1, mx + 1):
    noSet.add(str(i))
for line in fin:
    line = line.strip()
    if line != 'HELP':
        if fin.readline().strip() == 'YES':
            if len(mySet) == 0:
                mySet = set(line.split())
            else:
                mySet &= set(line.split())
        else:
            mySet -= set(line.split())
            noSet -= set(line.split())
    else:
        if len(mySet) == 0:
            print(*sorted(noSet))
        else:
            print(*sorted(mySet))
