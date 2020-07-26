t = int(input())
for case in range(t):
    n = int(input())
    a = input()
    b = input()
    print("Case #"+str(case+1)+": ")
    for i in range(n):
        ans = ''
        if b[i] == 'N':
            for j in range(n):
                if i == j:
                    ans += 'Y'
                else:
                    ans += 'N'
        elif b[i] == 'Y':
            id = 0
            for j in range(i, -1, -1):
                if i == j:
                    pass
                elif a[j] == 'N':
                    id = j
                    break
            jd = n
            for j in range(i, n):
                if i == j:
                    pass
                elif a[j] == 'N':
                    jd = j-1
                    break
            #print(id, jd)
            for j in range(0, id):
                if i == j:
                    ans += 'Y'
                else:
                    ans += 'N'
            for j in range(id, jd):
                ans += 'Y'
            for j in range(jd, n):
                if i == j:
                    ans += 'Y'
                else:
                    ans += 'N'
        print(ans)
