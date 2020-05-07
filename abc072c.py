n = int(input())
a = list(map(int, input().split()))
up = 100001
l = [0 for i in range(up)]
for i in range(n):
    l[a[i]] += 1
ma = -1
for i in range(1, up-1):
    if ma < l[i-1] + l[i] + l[i+1]:
        ma = l[i-1] + l[i] + l[i+1]
print(ma)