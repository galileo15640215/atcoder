n = int(input())
c = list(input())
if 'W' not in c or 'R' not in c:
    print(0)
else:
    for i in range(n-1, -1, -1):
        if c[i] == 'W':
            l = i
            break
    for i in range(n-1, -1, -1):
        if c[i] == 'R':
            r = i
            break
    if l > r:
        print(0)
    else:
        l = 0
        r = n-1
        cnt = 0
        while l < r:
            for i in range(r+1):
                if c[i] == 'W':
                    l = i
                    break
            for i in range(r, l-1, -1):
                if c[i] == 'R':
                    r = i
                    break
            c[l], c[r] = c[r], c[l]
            cnt += 1
        print(cnt-1)
"""
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
"""