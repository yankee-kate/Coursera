str = input()

x = str.find('h')
y = int(str.rfind('h')) + 1
newstr = str[:x] + str[y:]
print(newstr)
