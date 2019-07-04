n=int(input())
a=list(map(int, input().split()))
b = []
sum = 0
for i in range(n):
  sum += a[i]
max = sum
c = a
min = c[0] + c[1]
key1 = 0
key2 = 1
while(1):
  for i in range(1, n-1):
    if min > c[i] + c[i+1]:
      min = c[i] + c[i+1]
      key1 = i
      key2 = i+1
    c[key1] = c[key1]*(-1)
    c[key2] = c[key2]*(-1)
  sum = 0
  for i in range(n):
    sum += c[i]
  if max < sum:
    max = sum
  else:
    break
print(max)