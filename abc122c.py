a = input().split() 
n = a[0]
q = a[1]
s = input()
s = list(s)
cnt = []
l = []
r = []
for i in range(int(q)):
  a,b=map(int,input().split())
  l.append(a)
  r.append(b)
  cnt.append(0)
for i in range(int(q)):
  for j in range(int(l[i]), int(r[i])):
    if j == len(s)-1:
      break
    if s[j-1] == 'A' and s[j] == 'C':
      cnt[i] += 1
for i in range(len(cnt)):
  print(cnt[i])