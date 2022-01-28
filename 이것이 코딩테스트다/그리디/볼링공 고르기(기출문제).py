n, m = map(int, input().split())
data = list(map(int, input().split()))

result = 0
# for i in range(n):
#     for j in range(i+1, n):
#         if data[i] != data[j]:
#             result += 1
array = [0] * 11
for i in data:
    array[i] += 1
for i in range(1, m+1):
    n -= array[i]
    result += array[i] * n
print(result)
