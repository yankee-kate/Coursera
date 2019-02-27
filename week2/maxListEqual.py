# now = int(input())
#
# n1 = n2 = 0
# i = 1
# ar = []
# while now != 0:
#     if n1 == now:
#         if i > 1:
#             if n2 == now:
#                 i += 1
#             else:
#                 n2 = n1
#                 i = 2
#         else:
#             i += 1
#             n2 = n1
#     else:
#         ar.append(i)
#         n1 = now
#         n2 = 0
#     now = int(input())
# print(max(ar))
prev = -1
curr_rep_len = 0
max_rep_len = 0
element = int(input())
while element != 0:
    if prev == element:
        curr_rep_len += 1
    else:
        prev = element
        max_rep_len = max(max_rep_len, curr_rep_len)
        curr_rep_len = 1
    element = int(input())
max_rep_len = max(max_rep_len, curr_rep_len)
print(max_rep_len)
