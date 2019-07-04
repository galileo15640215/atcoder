n = int(input())
a = []
for i in range(n):
  a.append(int(input()))
a.sort(reverse=1)
cnt=1
max=a[0]
for i in range(1, n):
  if a[i]<max:
    cnt+=1
    max=a[i]
print(cnt)