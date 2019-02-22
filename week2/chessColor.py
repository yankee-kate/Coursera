col1 = int(input())
lin1 = int(input())
col2 = int(input())
lin2 = int(input())

if (col1 - col2) % 2 == 0 and (lin1 - lin2) % 2 == 0:
    print("YES")
elif (col1 - col2) % 2 != 0 and (lin1 - lin2) % 2 != 0:
    print("YES")
else:
    print("NO")
