s = input()
s = list(s)
cnt = []
for i in range(len(s)):
  c = 0
  j = i
  while s[j] == 'A' or s[j] == 'T' or s[j] == 'C' or s[j] == 'G':
    c +=1
    j += 1
    cnt.append(c)
    if j == len(s):
      break
if not cnt:
  print(0)
else:
  print(max(cnt))