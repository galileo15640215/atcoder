x, n = map(int, input().split())
if n == 0:
    print(x)
else:
    p = list(map(int, input().split()))
    p.sort()
    mi = 101
    chk = [1 for i in range(0, 102)]
    for i in range(n):
        chk[p[i]] = 0

    for i in range(0, 102):
        if chk[i] == 1:
            if abs(i - x) < mi:
                mi = abs(i - x)
                ans = i
    print(ans)