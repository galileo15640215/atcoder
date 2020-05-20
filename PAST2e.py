n = int(input())
a = list(map(int, input().split()))
ans = []
for i in range(n):
    key = a[i]
    x = i
    cnt = 1
    x = a[x]-1
    while i != x:
        cnt += 1
        x = a[x]-1
    ans.append(cnt)
for i in range(n-1):
    print(ans[i], end=' ')
print(ans[-1])