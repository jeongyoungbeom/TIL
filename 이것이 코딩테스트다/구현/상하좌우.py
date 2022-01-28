n = int(input())
List = input().split()
# for i in List:
#     if i == 'U':
#         if x == 1:
#             continue
#         else:
#             x -= 1
#     elif i == 'D':
#         if x == n:
#             continue
#         else:
#             x += 1
#     elif i == 'R':
#         if y == n:
#             continue
#         else:
#             y += 1
#     elif i == 'L':
#         if y == 1:
#             continue
#         else:
#             y -= 1
# print(x, y)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']
x, y = 1, 1
nx, ny = 1, 1
for plan in List:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny
print(x, y)