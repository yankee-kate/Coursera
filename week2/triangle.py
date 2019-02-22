a = int(input())
b = int(input())
c = int(input())

if a < b + c and b < a + c and c < a + b:
    if max(a, b, c)**2 == a**2 + b**2 + c**2 - max(a, b, c)**2:
        print("rectangular")
    elif max(a, b, c)**2 < a**2 + b**2 + c**2 - max(a, b, c)**2:
        print("acute")
    elif max(a, b, c)**2 > a**2 + b**2 + c**2 - max(a, b, c)**2:
        print("obtuse")
    else:
        print("impossible")
else:
    print("impossible")
