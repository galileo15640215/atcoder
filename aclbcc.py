n, m = map(int, input().split())
a = [list(map(int, input().split())) for i in range(m)]
flag = [0 for i in range(n)]
dic = {}
l = [0 for i in range(n)]
for i in range(m):
    if a[i][0] not in dic.keys():
        dic[a[i][0]] = [a[i][1]]
    else:
        dic[a[i][0]].append(a[i][1])
    l[a[i][0]-1] = 1
    l[a[i][1]-1] = 1
stack = [a[0][0]]
print(dic)
cnt = n-sum(l)
while stack:
    print(stack)
    tmp = stack.pop()
    if tmp in dic:
        for i in dic[tmp]:
            stack.append(i)
        if flag[tmp] == 0:
            flag[tmp] = 1
        else:
            cnt += 1
print(cnt-1)