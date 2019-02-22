number = input()

if len(number) < 4:
    while len(number) < 4:
        number = "0" + number

part1 = number[0:2]
part2 = number[3] + number[2]

if int(part1) == int(part2):
    print(1)
else:
    print(0)
