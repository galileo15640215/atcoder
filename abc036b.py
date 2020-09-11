n = int(input())
s = [input() for i in range(n)]
t = []
for i in range(n):
    l = []
    for j in range(n):
        l.append(s[n-1-j][i])
    t.append(l)
for i in range(n):
    for j in range(n):
        print(t[i][j], end='')
    print()