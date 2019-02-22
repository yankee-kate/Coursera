flat1 = int(input())
flat2 = int(input())

if (flat1 - 1) % (flat2 - flat1 + 1) == 0:
    print("YES")
else:
    print("NO")
