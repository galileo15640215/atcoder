import math
n, p = map(int, input().split())
a = list(map(int, input().split()))
even = 0
odd = 0
for i in range(n):
    if a[i]%2 == 0:
        even += 1
    else:
        odd += 1
ans = 0
if p == 0:
    ans += 1
    ans += even*(even+1)//2 + (odd-1)*odd//2 + even*(even+1)//2*(odd-1)*odd//2
else:
    ans += odd*(odd+1)//2 + math.factorial(even)*odd*(odd+1)//2
print(ans)