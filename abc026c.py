n = int(input())
b = [int(input()) for i in range(n-1)]
dic = {1 : []}
for i in range(len(b)):
    if b[i] not in dic.keys():
        dic[b[i]] = []
    dic[b[i]].append(i+2)
q = [1]
res = []
mon = [0 for i in range(n+1)]
while q:
    tmp = q.pop(0)
    if tmp in dic.keys():
        for i in dic[tmp]:
            q.append(i)
    else:
        res.append(tmp)
for i in range(len(res)):
    mon[res[i]] = 1
while 0 in mon[1:]:
    for i in dic.keys():
        res = []
        flag = True
        for j in dic[i]:
            if mon[j] == 0:
                flag = False
                break
            else:
                res.append(mon[j])
        if flag:
            mon[i] = max(res) + min(res) + 1
print(mon[1])