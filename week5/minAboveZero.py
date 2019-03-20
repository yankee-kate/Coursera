def minAboveZero(A):
    j = 0
    val = ''
    for i in range(len(A)):
        if j == 0:
            if int(A[i]) > 0:
                val = int(A[i])
                j += 1
        else:
            if int(A[i]) > 0 and val > int(A[i]):
                val = int(A[i])
    return val


myList = input().split()
print(minAboveZero(myList))
