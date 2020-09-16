n, q = map(int, input().split())
l = [list(map(int, input().split())) for i in range(q)]
a = [0 for i in range(n)]
for i in range(q):
    for j in range(l[i][0]-1, l[i][1]):
        a[j] = l[i][2]
for i in range(n):
    print(a[i], end=' ')