n, k = map(int, input().split())
s = input()
s = list(s)
ans = s
len = []
for i in range(n):
  l = 0
  if s[i] == '0':
    l += 1
    j = i
    while s[j+1] != '0':
      l += 1
  len.append(l)
print(len)