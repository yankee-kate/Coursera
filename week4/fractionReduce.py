def fractionReduce(n, m):
    def gdc(a, b):
        while a % b:
            a, b = b, a % b
        return b

    g = gdc(n, m)
    return n // g, m // g


a = int(input())
b = int(input())
result = fractionReduce(a, b)
print(result[0], result[1])
