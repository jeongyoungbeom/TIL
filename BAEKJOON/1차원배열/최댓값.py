# import sys
#
# max = 0
# cnt = 0
# b = 0
# for i in range(9):
#     a = int(sys.stdin.readline())
#     b += 1
#     if a > max :
#         max = a
#         cnt = b
#
# print("%d\n%d" %(max, cnt))

import sys
a = []
for i in range(9):
    a.append(int(sys.stdin.readline()))

print(max(a), a.index(max(a))+1)
