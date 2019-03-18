def flag(n):
    if n in range(1, 10):
        print('+___ ' * n)
        for i in range(1, n + 1):
            if i != n:
                print('|' + str(i) + ' / ', end='')
            else:
                print('|' + str(i) + ' / ', end='\n')
        print('|__\\ ' * n)
        print('|    ' * n)


a = int(input())
flag(a)
