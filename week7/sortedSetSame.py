newSet = set(map(int, input().split())) & set(map(int, input().split()))
lst = sorted(list(newSet))
print(*lst)
