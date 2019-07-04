x, y, z, k = map(int, input().split())
a = []
b = []
c = []
li = input().rstrip().split()
for i in li:
    a.append(int(i))
li = input().rstrip().split()
for i in li:
    b.append(int(i))
li = input().rstrip().split()
for i in li:
    c.append(int(i))
ans = []
for i in range(x):
  for j in range(y):
    for l in range(z):
      ans.append(a[i]+b[j]+c[l])
print(ans)      
ans.sort()
ans.reverse()     
for i in range(k):
  print(ans[i])