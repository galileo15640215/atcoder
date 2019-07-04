r, d, x = map(int, input().split())
xx = []
tmp = x
for i in range(10):
  tmp = r*tmp-d
  xx.append(tmp)
 
for i in range(10):
  print(xx[i])