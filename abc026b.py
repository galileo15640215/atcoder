import math
n = int(input())
r = [int(input()) for i in range(n)]
ans = 0
for i in range(n):
    if i%2 == 0:
        ans += r[i]*r[i]*math.pi
    else:
        ans -= r[i]*r[i]*math.pi
print(ans)