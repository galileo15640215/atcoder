c = []
for i in range(3):
    t = list(map(int, input().split()))
    c.append(t)
a = [0, 0, 0]
b = [0, 0, 0]
for d in range(101):
    for e in range(101):
        for f in range(101):
            for g in range(101):
                for h in range(101):
                    for k in range(101):
                        if d+e+f+g+h+k > 100:
                            flag = False
                            break
                        a[0] = d
                        a[1] = e
                        a[2] = f
                        b[0] = g
                        b[1] = h
                        b[2] = k
                        flag = True
                        for i in range(3):
                            for j in range(3):
                                if c[i][j] != a[i]+b[j]:
                                    flag = False
                                    break
                            if not flag:
                                break
                        if flag:
                            break
                    if flag:
                        break
                if flag:
                    break
            if flag:
                break
        if flag:
            break
    if flag:
        break
if flag:
    print("Yes")
else:
    print("No")