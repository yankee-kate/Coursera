# import math
#
# a = float(input())
# b = float(input())
# c = float(input())
#
# discr = b ** 2 - 4 * a * c
#
# if discr > 0:
#     x1 = (-b + math.sqrt(discr)) / (2 * a)
#     x2 = (-b - math.sqrt(discr)) / (2 * a)
#     print(x1, x2)
# elif discr == 0:
#     x = -b / (2 * a)
#     print(x)
# else:
#     print('')
a = float(input())
b = float(input())
c = float(input())

x = x2 = 0

D = b ** 2.0 - 4.0 * a * c

if D == 0:
    x = -b / (2.0 * a)
    print('{0:.6f}'.format(x))
elif D > 0:
    x = (-b + D ** 0.5) / (2.0 * a)
    x2 = (-b - D ** 0.5) / (2.0 * a)
    if x2 < x:
        print('{0:.6f}'.format(x2))
        print('{0:.6f}'.format(x))
    else:
        print('{0:.6f}'.format(x))
        print('{0:.6f}'.format(x2))
else:
    print('')
