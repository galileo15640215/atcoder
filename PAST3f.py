n = int(input())
a = [list(input()) for i in range(n)]
l = []
m = []
ans = []
flag = True
for i in range(n//2):
    l = a[i]
    m = a[n-i-1]
    flag = False
    for j in range(n):
        if l[j] in m:
            ans.append(l[j])
            flag = True
            break
    if not flag:
        break
if flag:
    for i in range(n//2):
        print(ans[i], end='')
    if n%2 == 1:
        print(a[n//2][0], end='')
    for i in range(n//2-1, -1, -1):
        print(ans[i], end='')
    print()
else:
    print(-1)