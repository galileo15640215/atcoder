n = int(input())
h = list(map(int, input().split()))
dp = [int(10000000000)]*100000
dp[0] = 0
cost = 0
for i in range(1, n):
  if dp[i] > dp[i-1]+abs(h[i]-h[i-1]):
    dp[i]=dp[i-1]+abs(h[i]-h[i-1])
  if i > 1:
    if dp[i] > dp[i-2]+abs(h[i]-h[i-2]):
      dp[i]=dp[i-2]+abs(h[i]-h[i-2])
print(dp[n-1])