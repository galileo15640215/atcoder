import bisect

n, k = map(int, input().split())
x, y = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
now = 0
cnt = 0
while True:
    if now > a[-1]:
        break
    i = bisect.bisect_right(a, now)
    if a[i-1] == now:
        now = a[i-1] + x
    else:
        now = a[i] + x
    if now > b[-1]:
        break
    i = bisect.bisect_right(b, now)
    if b[i-1] == now:
        now = b[i-1] + y
    else:
        now = b[i] + y
    cnt += 1

print(cnt)
