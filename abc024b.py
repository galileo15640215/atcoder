import math
n = int(input())
r = [int(input() for i in range(n)]
ans = 0
for i in range(n):
    if i%2 == 0:
        ans += a[i]*a[i]*math.pi
    else:
        ans -= a[i]*a[i]*math.pi
print(ans)