N = int(input())

h = N // 3600
m = (N % 3600) // 60
s = (N % 3600) % 60

if h > 23:
    h = h % 24
if m // 10 == 0:
    m = "0" + str(m)
if s // 10 == 0:
    s = "0" + str(s)

print(h, m, s, sep=":")
