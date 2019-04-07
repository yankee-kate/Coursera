fin = open('input.txt', encoding='utf8')
lst = []
wordLst = []
for line in fin:
    # lst = (tuple(re.compile('\w+').findall(line)))
    lst = tuple(line.split())
    for i in range(len(lst)):
        wordLst.append(lst[i])
tup = tuple(wordLst)
wordSet = set(tup)
print(len(wordSet))
