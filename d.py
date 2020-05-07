n = int(input())
a = list(map(int, input().split()))
cnt = 2
for i in range(n):
    if a[i] < 0:
        cnt += 1
sum = 0
for i in range(n):
    sum += abs(a[i])
if cnt%2 == 0:
    print(sum)
else:
    mi = abs(a[0])
    for i in range(n):
        if mi > abs(a[i]):
            mi = abs(a[i])
    print(sum - mi - mi)