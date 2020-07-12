t = int(input())
for case in range(t):
    n = int(input())
    v = list(map(int, input().split()))
    ans = 0
    if n == 1:
        print(0)
    else:
        if v[0] > v[1]:
            ans += 1
        ma = v[0]
        for i in range(1, n):
            if i == n-1:
                if ma < v[i]:
                    ans += 1
            elif ma < v[i] and v[i] > v[i+1]:
                ans += 1
            if ma < v[i]:
                ma = v[i]
        print("Case #"+str(case+1)+": ", end='')
        print(ans)