import sys

c = int(input())
for i in range(c):
    a = list(map(int, sys.stdin.readline().split()))
    b = 0
    cnt = 0
    for j in range(1, len(a)):
        b += a[j]
    b /=a[0]
    for j in range(1, len(a)):
        if b < a[j]:
            cnt +=1
    print("%.3f%%" %(cnt/a[0]*100))
