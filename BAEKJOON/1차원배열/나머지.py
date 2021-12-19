import sys

set = set([]) # set 함수 중복을 없애줍니다
for i in range(10):
    a = int(sys.stdin.readline())
    set.add(a%42)

print(len(set))