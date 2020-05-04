n, k = map(int, input().split())
a = list(map(int, input().split()))
dic = {}
for i in range(n):
    if a[i] not in dic.keys():
        dic[a[i]] = 1
    else:
        dic[a[i]] += 1
cnt = 0
d = sorted(dic.values())
for i, j in zip(range(len(dic)-k), d):
    cnt += j
print(cnt)