n, w = map(int, input().split())
c = []
sum_w = 0
for i in range(n):
    s = list(map(int, input().split()))
    c.append(s)
    sum_w += s[0]
dp = [[0 for j in range(sum_w+1)]for i in range(n)]
c.sort(key=lambda x: x[0])
for i in range(c[0][0], sum_w+1):
    dp[0][i] = c[0][1]
for i in range(1, n):
    for j in range(sum_w+1):
        if  j-c[i][0] >= 0:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-c[i][0]] + c[i][1])
        if dp[i][j] == 0:
            dp[i][j] = dp[i-1][j]
print(dp[n-1][w])