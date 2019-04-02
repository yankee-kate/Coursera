n = int(input())
# fin = open('input.txt')
patList = []
# for man in range(n):
#     patList.append(fin.readline().strip().split())
for i in range(n):
    patList.append(list(input().split()))
patList.sort(key=lambda point: int(point[1]), reverse=True)
for i in range(len(patList)):
    print(patList[i][0])
