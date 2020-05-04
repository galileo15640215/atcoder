n, w = map(int, input().split())
c = []
for i in range(n):
    s = list(map(int, input().split()))
    c.append(s)
dp = [[0 for j in range(w+1)]for i in range(n)]
c.sort(key=lambda x: x[0])
for i in range(c[0][0], w+1):
    dp[0][i] = c[0][1]
for i in range(1, n):
    for j in range(w+1):
        if  j-c[i][0] >= 0:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-c[i][0]] + c[i][1])
        if dp[i][j] == 0:
            dp[i][j] = dp[i-1][j]
print(dp[n-1][w])