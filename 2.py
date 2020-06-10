import math
from decimal import *
a, b, c, d = map(int, input().split())
n = int(input())
t = [list(map(str, input().split())) for i in range(n)]
su = 0
for i in range(n):
    res = b
    p, q = t[i][0], int(t[i][1])
    if q > a:
        res += math.ceil((q-a)/c)*d
    if p[0] == '0':
        pass
    elif int(p[0:2]) >= 22:
        res = Decimal(str(res)) * Decimal("1.2")
    su += res
print(int(su))