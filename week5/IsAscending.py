def IsAscending(A):
    i = 0
    while i < len(A) - 1:
        if int(A[i + 1]) <= int(A[i]):
            return 'NO'
        i += 1
    return 'YES'


myList = input().split()
print(IsAscending(myList))
