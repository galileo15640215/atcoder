n, q = map(int, input().split())
dic = {}
cnt = [0 for i in range(n+1)]
for i in range(1, n+1):
    dic[i] = []
a = [list(map(int, input().split())) for i in range(n-1)]
for i in range(n-1):
    dic[a[i][0]].append(a[i][1])
p = [list(map(int, input().split())) for i in range(q)]

def dfs(y, x):
    cnt[y] += x
    for k in dic[y]:
        dfs(k, x)
for i in range(q):
    for j in dic[p[i][0]]:
        dfs(j, p[i][1])
    cnt[p[i][0]] += p[i][1]
for i in range(1, n+1):
    print(cnt[i], end=' ')
print()