import math
n = int(input())
a = list(map(int, input().split()))
res = a[0]
for i in range(1, n):
    res = math.gcd(res, a[i])
print(res)