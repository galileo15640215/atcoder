n = int(input())
c = list(input())
p = -1
q = -1
cnt = 0
for i in range(n-1, -1, -1):
    if c[i] == 'R' and q == -1:
        p = i
        break
for i in range(p-1, -1, -1):
    if c[i] == 'R' and p != -1 and q == -1:
        q = i
    elif c[i] == 'W':
        break
if p == -1:
    print(0)
elif q == -1:
    for i in range(p):
        if c[i] == 'W':
            cnt += 1
    print(cnt)
else:
    for i in range(n):
        if c[i] == 'W' and i < p:
            cnt += 1
    print(cnt-(q-p+1))