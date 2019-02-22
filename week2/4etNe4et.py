A = int(input())
B = int(input())
C = int(input())

if A % 2 == 0 and B % 2 == 0 and C % 2 == 0:
    print("NO")
elif A % 2 != 0 and B % 2 != 0 and C % 2 != 0:
    print("NO")
else:
    print("YES")
