n = input ()
m = list(n)
cnt = 0
for i in range(len(m)-1):
  if m[i] != m[i+1] :
    pass
  elif m[i] == m[i+1] and m[i] == '0':
    m[i+1] = '1'
    cnt += 1
  elif m[i] == m[i+1] and m[i] == '1':
    m[i+1] = '0'
    cnt += 1
print(cnt)