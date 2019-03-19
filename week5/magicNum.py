for i in range(10, 100):
    num = tuple(str(i))
    if 2 * (int(num[0]) * int(num[1])) == i:
        print(i)
