import copy
n, m = map(int, input().split())
p = [list(map(int, input().split())) for i in range(m)]
dic = {}
q = copy.copy(p)
q.sort(key=lambda x: x[1])
cnt = [0 for i in range(n+1)]
for i in range(m):
    cnt[q[i][0]] += 1
    dic[q[i][1]] = cnt[q[i][0]]
for i in range(m):
    print(str(p[i][0]).zfill(6)+str(dic[p[i][1]]).zfill(6))