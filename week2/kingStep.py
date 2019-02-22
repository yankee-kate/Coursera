col1 = int(input())
lin1 = int(input())
col2 = int(input())
lin2 = int(input())

if abs(col1 - col2) == 1 or col1 == col2:
    if abs(lin1 - lin2) == 1 or lin2 == lin1:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
