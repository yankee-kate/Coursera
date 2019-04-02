fin = open('input.txt', encoding='utf8')
lst = []
for line in fin:
    lst.append(line.strip().split())
lst.sort()
for i in range(len(lst)):
    print(lst[i][0], lst[i][1], lst[i][3])
