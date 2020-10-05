n, x = map(int, input().split())
a = [int(i) for i in input().split()]
ans = 0

for i in range(n):
  if ((x >> i) & 1):
    ans += a[i]
    
print(ans)
