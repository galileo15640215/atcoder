
n, m = map(int, input().split())
s = list(input())
k = list(input())
l = [0 for i in range(len(k))]
dic = {}
d = {}
for i in k:
    if i not in dic.keys():
        dic[i] = 1
    else:
        dic[i] += 1
for i in s:
    if i not in d.keys():
        d[i] = 1
    else:
        d[i] += 1
cnt = -1
flag = True
for i in s:
    if i not in dic.keys():
        flag = False
if flag:
    cnt = 0
    while True:
        flag = True
        cnt += 1
        for i in k:
            if i in d.keys():
                d[i] -= 1
        for i in d.keys():
            if d[i] > 0:
                flag = False
        if flag:
            break
print(cnt)