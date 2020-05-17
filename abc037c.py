n, k = map(int, input().split())
a = list(map(int, input().split()))
rui = [a[0]]
for i in range(1, n):
    rui.append(rui[i-1] + a[i])
ans = rui[k-1]
for i in range(n-k):
    ans += rui[i+k] - rui[i]
print(ans)