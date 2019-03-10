str = input()

x = str.find(' ')
newstr = str[x+1:] + ' ' + str[:x]
print(newstr)
