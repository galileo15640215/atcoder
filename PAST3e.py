n, m, q = map(int, input().split())
u = [list(map(int, input().split())) for i in range(m)]
c = list(map(int, input().split()))
s = [list(map(int, input().split())) for i in range(q)]
dic = {}
for i in range(1, n+1):
    dic[i] = []
for i in range(m):
    dic[u[i][0]].append(u[i][1])
    dic[u[i][1]].append(u[i][0])
for i in range(q):
    print(c[s[i][1]-1])
    if s[i][0] == 1:
        for j in dic[s[i][1]]:
            c[j-1] = c[s[i][1]-1]
    elif s[i][0] == 2:
        c[s[i][1]-1] = s[i][2]
