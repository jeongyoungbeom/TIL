import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = []
for i in range(len(a)):
    b.append(a[i]/max(a)*100)

c = sum(b)/n
print(c)