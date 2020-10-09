s = list(input())
n = int(input())

s.insert(0,'a')
for i in range(n):
  l,r = map(int,input().split())
  t = s[r:l-1:-1]
  s[l:r+1] = t
  
del s[0]
print(''.join(s))