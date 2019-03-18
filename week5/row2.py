def row2(a, b):
    if a <= b:
        for i in range(a, b + 1):
            print(i)
    elif a > b:
        for i in range(a, b - 1, -1):
            print(i)


A = int(input())
B = int(input())
row2(A, B)
