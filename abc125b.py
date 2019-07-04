n=int(input())
v=list(map(int, input().split()))
c=list(map(int, input().split()))
x = 0
y = 0
z = []
min = 1000000
 
for i in range(n):
  z.append(v[i]-c[i])
 
ans1 = z[0]
for i in range(1, n):
  if ans1 < ans1 + z[i]:
    ans1 += z[i]
 
ans2 = 0
for i in range(1, n):
  if ans2 < ans2 + z[i]:
    ans2 += z[i]
 
print(max(ans1, ans2))