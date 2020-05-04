n = int(input())
s = input()

ans = 0
for i in range(1, n):
    x = s[0:i]
    y = s[i:n]
    xl = list(x)
    yl = list(y)
    cnt = 0
    pre = []
    for j in range(len(xl)):
        if xl[j] in yl and xl[j] not in pre:
            cnt += 1
            pre.append(xl[j])
    if ans < cnt:
        ans = cnt
print(ans)