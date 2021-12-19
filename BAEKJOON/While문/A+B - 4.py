import sys

a = int(sys.stdin.readline())
cnt = 0
f = a
while True :
    b = f // 10  # 십의자리
    c = f % 10   # 일의 자리
    d = (b + c) % 10 # 더해서 일의자리
    f = (c*10)+d
    cnt += 1
    if f == a:
        break

print(cnt)