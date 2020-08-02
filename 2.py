n, d = map(int, input().split())
cnt = 0
for i in range(n):
    p, q = map(int, input().split())
    if (p*p+q*q)**0.5 <= d:
        cnt += 1
print(cnt)