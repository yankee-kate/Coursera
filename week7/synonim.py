fin = open('input.txt')
n = int(fin.readline().strip())
myDict = dict()
for i in range(n):
    a, b = fin.readline().strip().split()
    myDict[a] = b
    myDict[b] = a
print(myDict[fin.readline().strip()])
