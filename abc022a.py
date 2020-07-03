n, s, t = map(int, input().split())
w = int(input())
a = [int(input()) for i in range(n-1)]
cnt = 0
if s <= w <= t:
    cnt += 1
for i in range(n-1):
    w += a[i]
    if s <= w <= t:
        cnt += 1
print(cnt)