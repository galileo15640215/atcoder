n = int(input())
s = ['A', 'C', 'G', 'T']
list = []
cnt = 0
for h in range(10**4):
  for i in range(3):
    for j in range(3):
      for k in range(3):
        for l in range(3):
          l = s[i]+s[j]+s[k]+s[l]
  list.append(l)
for i in range(n):
  if 'AGC' in list[i]:
    cnt += 1
print((4**3-cnt)/(10**9+7))