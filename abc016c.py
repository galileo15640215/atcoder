n, m = map(int, input().split())
cnt = [0 for i in range(n)]
dic = {}
for i in range(1, n+1):
    dic[i] = []
for i in range(m):
    a, b = map(int, input().split())
    dic[a].append(b)
    dic[b].append(a)
for i in dic.keys():
    tmp = set()
    for j in dic[i]:
        for k in dic[j]:
            if (not k in dic[i]) and k != i:
                tmp.add(k)
    print(len(tmp))