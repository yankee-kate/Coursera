def winner(canDict, file):
    for candidate in canDict:
        canDict[candidate] = canDict[candidate] * 100 / count
        if canDict[candidate] > 50:
            return print(candidate, file=file)
    canLst = sorted(list(canDict.items()), key=lambda k: k[1], reverse=True)
    return print(canLst[0][0], canLst[1][0], file=file, sep='\n')


fin = open('input.txt', encoding='utf8')
candidates = dict()
for line in fin:
    if line.strip() in candidates:
        candidates[line.strip()] += 1
    else:
        candidates[line.strip()] = 1
count = sum(candidates.values())

fout = open('output.txt', 'w', encoding='utf8')
winner(candidates, fout)
