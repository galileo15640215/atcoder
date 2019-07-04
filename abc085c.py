n, y = map(int, input().split())
ans = [-1, -1, -1]
for i in range(n+1):
  for j in range(n+1-i):
    k = n-i-j
    if i*10000+j*5000+k*1000 == y and k>=0:
      ans[0] = i
      ans[1] = j
      ans[2] = k
      break
print(ans[0], ans[1], ans[2])