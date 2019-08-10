import math
n, d = map(int, input().split())
x = []
for i in range(n):
    l = list(map(int, input().split()))
    x.append(l)

cnt  = 0
for k in range(n-1):
    for i in range(k+1, n):
        sum = 0
        for j in range(d):
            sum += pow((x[k][j] - x[i][j]), 2)
        if math.sqrt(sum) %1 == 0:
            cnt += 1

print(cnt)