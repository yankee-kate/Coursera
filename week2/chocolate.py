l = int(input())
w = int(input())
k = int(input())

if k < l * w:
    if k % l == 0 or k % w == 0:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
