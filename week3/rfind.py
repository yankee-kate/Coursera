str = input()
substr = 'f'

if str.find(substr) != -1:
    if str.rfind(substr) != str.find(substr):
        print(str.find(substr))
        print(str.rfind(substr))
    elif str.rfind(substr) == str.find(substr):
        print(str.find(substr))
