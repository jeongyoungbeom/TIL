s = input()
first = int(s[0])
result = 0
for i in range(1, len(s)):
    if first == 0 or s[i] == 0:
        result = first + int(s[i])
    else:
        result = first * int(s[i])
    first = result
print(result)