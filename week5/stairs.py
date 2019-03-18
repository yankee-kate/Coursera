def stairs(n):
    if n <= 9:
        string = ''
        for i in range(1, n + 1):
            string = string + str(i)
            print(string)


N = int(input())
stairs(N)
