n, x = map(int, input().split())
a = [int(input()) for i in range(n)]
cnt = 0
for i in range(n-1):
    for j in range(i+1, n):
        if a[i]^a[j] == x:
            cnt += 1
print(cnt)