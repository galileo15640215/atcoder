n, m = map(int, input().split())
s = []
c = []
for i in range(m):
    a, b = map(int, input().split())
    s.append(a)
    c.append(b)
val = 10**n
if n == 1 and m == 0:
    print(0)
else:
    for i in range(10**(n-1), val):
        flag = True
        for j in range(m):
            if str(i)[s[j]-1] == str(c[j]):
                pass
            else:
                flag = False
                break
        if flag:
            print(i)
            break
    if flag:
        pass
    elif n == 1 and m == 1 and s[0] == 1 and c[0] == 0:
        print(0)
    else:
        print(-1)