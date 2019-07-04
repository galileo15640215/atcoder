n, m, c = map(int, input().split())
b = [int(i) for i in input().split()]
a = [[int(j) for j in input().split()] for i in range(n)]
ans = 0
for i in range(n):
  sum = 0
  for j in range(m):
    sum += a[i][j]*b[j]
  sum += c
  if sum > 0:
    ans += 1
print(ans)