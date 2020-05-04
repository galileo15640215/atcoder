n, m = map(int, input().split())
s = [0 for i in range(n)]
e = [0 for i in range(n)]
for i in range(m):
    x, y = map(int, input().split())
    if x == 1:
        s[y] = 1
    elif y == n:
        e[x] = 1
flag = False
for i in range(n):
    if s[i] == 1 and e[i] == 1:
        flag = True
        break
if flag:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")