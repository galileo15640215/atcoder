n, m = map(int, input().split())
h = list(map(int, input().split()))
a = [[] for i in range(n)]
for i in range(m):
    s, t = map(int, input().split())
    a[s-1].append(t-1)
    a[t-1].append(s-1)
cnt = 0
for i in range(0, n):
    flag = True
    for j in range(len(a[i])):
        if h[i] <= h[a[i][j]]:
            flag = False
            break
    if flag:
        cnt += 1
print(cnt)