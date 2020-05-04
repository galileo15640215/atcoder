n, m = map(int, input().split())
INF=float('inf')
dist = [[INF for j in range(n)] for i in range(n)]
for i in range(n):
    dist[i][i] = 0
for i in range(m):
    a, b, t = list(map(int, input().split()))
    dist[a-1][b-1] = t
    dist[b-1][a-1] = t
for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k]+ dist[k][j])
print(min(max(i) for i in dist))
"""
su = INF
for i in range(n):
    if su > sum(dist[i]):
        idx = i
        su = sum(dist[i])
print(max(dist[idx]))
"""