s = list(input())
t = list(input())
ls = len(s)
lt = len(t)
if ls < lt:
    print("UNRESTORABLE")
else:
    res = []
    for i in range(ls-lt+1):
        res.append(s[i:i+lt])
    tmp = []
    for i in range(len(res)):
        flag = True
        for j in range(lt):
            if res[i][j] == t[j] or res[i][j] == '?':
                pass
            else:
                flag = False
                break
        if flag:
            tmp.append(i)
    ans = []
    for i in tmp:
        q = []
        for j in range(0, i):
            q.append(s[j])
        for j in range(0, lt):
            q.append(t[j])
        for j in range(i+lt, ls):
            q.append(s[j])
        for j in range(ls):
            if q[j] == '?':
                q[j] = 'a'
        ans.append(''.join(q))
    if ans:
        print(min(ans))
    else:
        print("UNRESTORABLE")