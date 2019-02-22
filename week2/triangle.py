a = int(input())
b = int(input())
c = int(input())

if max(a, b, c)**2 == a**2 + b**2 + c**2 - max(a, b, c)**2:
    print("rectangular")
elif max(a, b, c)**2 < a**2 + b**2 + c**2 - max(a, b, c)**2:
    print("acute")
elif max(a, b, c)**2 > a**2 + b**2 + c**2 - max(a, b, c)**2:
    print("obtuse")
else:
    print("impossible")
