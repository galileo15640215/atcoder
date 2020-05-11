n, m = map(int, input().split())
cnt = 0
if 2*n <= m:
    m -= n*2
    cnt += n
    m //= 4
    cnt += m
else:
    cnt = m//2
print(cnt)