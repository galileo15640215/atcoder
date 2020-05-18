import queue
n, m = map(int, input().split())
a = [0 for i in range(m)]
b = [0 for i in range(m)]
dic = {}
for i in range(1, n+1):
    dic[i] = []
for i in range(m):
    a[i], b[i] = map(int, input().split())
    dic[a[i]].append(b[i])
    dic[b[i]].append(a[i])
res = 0
INF = 100010
l = [0 for i in range(n+1)]
l[1] = 1
michi = [INF for i in range(n+1)] 
michi[1] = 0
p = [1]
shi = 1
while True:
    tmp = []
    for i in p:
        for j in dic[i]:
            if l[j] == 0:
                l[j] = 1
                tmp.append(j)
    if not tmp:
        break
    for i in tmp:
        michi[i] = shi
    p = tmp
    shi = p[0]
flag = True
for i in range(2, n+1):
    if michi[i] == INF:
        flag = False
if flag:
    print("Yes")
    for i in range(2, n+1):
        print(michi[i])
else:
    print("No")