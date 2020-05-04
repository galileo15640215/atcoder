k, n = map(int, input().split())
a = list(map(int, input().split()))
ma = -1
mi = -1
for i in range(n-1):
    if abs(a[i] - a[i+1]) > ma:
        ma = abs(a[i] - a[i+1])
        mi = i
flag = False
if abs(a[n-1]-k-a[0]) > ma:
    ma = abs(a[n-1]-k-a[0])
    mi = n-1
    flag = True
sum = 0
if flag:
    for i in range(0, n-1):
        sum += abs(a[i] - a[i+1])
else:
    for i in range(0, mi):
        sum += abs(a[i] - a[i+1])
    for i in range(mi+1, n-1):
        sum += abs(a[i] - a[i+1])
    sum += abs(a[n-1]-k-a[0])
print(sum)