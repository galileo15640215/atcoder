t = int(input())
for case in range(t):
    n, b = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    cnt = 0
    for i in range(n):
        if b - a[i] >= 0:
            b -= a[i]
            cnt += 1
        else:
            break
    print("Case #"+str(case+1)+": ", end='')
    print(cnt)