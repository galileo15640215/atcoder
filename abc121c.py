n, m = map(int, input().split())
x = [[int(j) for j in input().split()] for i in range(n)]
a = []
b = []
for i in range(n):
  a.append(x[i][0])
  b.append(x[i][1])
mon = 0
cnt = 0
ind = 100000
while(cnt < m):
  min = 10000000000
  for i in range(n):
    if a[i] < min:
      min = a[i]
      ind = i
  while(b[ind] > 0 and cnt != m):
    cnt += 1
    mon += a[ind]
    b[ind] -= 1
  a[ind] = 100000000000
print(mon)