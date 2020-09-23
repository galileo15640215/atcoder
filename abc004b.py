a=[input() for i in range(4)]
a.reverse()
for i in range(4):
  print(*a[i][::-1])
