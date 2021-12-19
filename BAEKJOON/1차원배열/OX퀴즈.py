import sys

n = int(input())
for i in range(n):
    cnt = 0
    sum = 0
    a = sys.stdin.readline()
    for j in range(len(a)):
        if a[j] == "O":
           cnt +=1
           sum +=cnt
        else:
            cnt = 0
    print(sum)

