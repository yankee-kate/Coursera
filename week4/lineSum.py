def lineSum():
    n = int(input())
    if n != 0:
        return n + lineSum()
    else:
        return 0


print(lineSum())
