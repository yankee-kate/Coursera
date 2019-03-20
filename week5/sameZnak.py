def sameZnak(A):
    for i in range(len(A) - 1):
        if (int(A[i + 1]) >= 0 and int(A[i]) >= 0) \
                or (int(A[i + 1]) < 0 and int(A[i]) < 0):
            return A[i], A[i + 1]
    return ''


myList = input().split()
print(*sameZnak(myList))
