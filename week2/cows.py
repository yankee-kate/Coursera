n = int(input())

if 10 < n < 20 or int(str(n)[-1]) in [0, 5, 6, 7, 8, 9]:
    print(n, "korov")
elif int(str(n)[-1]) == 1:
    print(n, "korova")
else:
    print(n, "korovy")
