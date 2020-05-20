import bisect
n = int(input())
dic = {}
for i in range(n):
    s, t = map(int, input().split())
    if s not in dic.keys():
        dic[s] = [t]
    else:
        dic[s].append(t)
for i in dic.keys():
    dic[i].sort()
poi = 0
l = []
for i in range(n):
    ma = -1
    if i+1 in dic.keys():
        for j in dic[i+1]:
            index = bisect.bisect_left(l, j)
            l.insert(index, j)
    poi += l.pop(-1)
    print(poi)