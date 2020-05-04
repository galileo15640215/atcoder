import copy
n = int(input())
x = list(map(int, input().split()))
y = copy.copy(x)
y.sort()
cen1 = y[(n-1)//2]
cen2 = y[n//2]
for i in range(n):
    if x[i] < y[n//2]:
        print(cen2)
    else:
        print(cen1)
