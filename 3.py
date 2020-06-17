t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    s = input()
    cnt = 0
    l = [-1]
    for j in range(n):
        if s[j] == '1':
            l.append(j)
    l.append(n)
    res = []
    for j in range(1, len(l)):
        res.append([l[j-1], l[j]])
    print(l)
    print(res)
    cnt = 0
    for j in range(len(res)):
        if res[j][1] - res[j][0] >= 2*k+1:
            cnt += (res[j][1] - res[j][0])/(2*k+1)
    print(cnt)

    """
    idx = -1
    for j in range(min(0+2*k+1, n)):
        if s[j] == '1':
            idx = j
    if idx == -1:
        idx = 0
        pass
    elif idx+1 < k:
        s[0] = '1'
        cnt += 1
    for j in range(idx, n):
        if s[j] == '1':
            flag = True
            for l in range(j+1, min(j+2*k+1, n)):
                if s[l] == '1':
                    flag = False
                    break
            if flag:
                s[j+k] == '1'
                cnt += 1
    """
