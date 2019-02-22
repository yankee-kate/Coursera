a = int(input())
b = int(input())
c = int(input())

if a == b == c:
    print(3)
elif a == b or c == b or c == a:
    print(2)
else:
    print(0)
