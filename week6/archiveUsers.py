def archive_users(n, storage):
    lst = []
    for i in range(n):
        lst.append(int(input()))
    lst.sort()
    user_stor = 0
    user_count = 0
    for i in range(len(lst)):
        user_stor += lst[i]
        if user_stor <= storage:
            user_count += 1
        else:
            return user_count
    return user_count


inp_data = list(map(int, input().split()))
print(archive_users(inp_data[1], inp_data[0]))
