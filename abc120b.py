a, b, k = map(int, input().split())
l = []
for i in range(1, 101):
  if a%i == 0 and b%i == 0:
    l.append(i)
l.sort(reverse=1)
print(l[k-1])