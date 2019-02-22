N = int(input())

hours = N // 60
if hours > 23:
    hours = hours % 24
min = N % 60

print(hours, min)
