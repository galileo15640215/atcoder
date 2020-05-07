h, w = map(int, input().split())
s = []
s.append(['.']*(w+2))
for i in range(1, h+1):
    t = input()
    u = ['.']
    for j in range(w):
        u.append(t[j])
    u.append('.')
    s.append(u)
s.append(['.']*(w+2))
key = True
d = [[0, -1], [0, 1], [-1, 0], [1, 0]]
flag = True
for i in range(1, h+1):
    for j in range(1, w+1):
        if s[i][j] == '#':
            key = False
            for k in range(len(d)):
                if s[i+d[k][0]][j+d[k][1]] == '#':
                    key = True
            if not key:
                flag = False
                break
    if not flag:
        break
if flag:
    print("Yes")
else:
    print("No")