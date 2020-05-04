n = int(input())
a = list(map(int, input().split()))
x = []
s = 0
for i in range(1, n, 2):
    s += a[i]
x.append(sum(a) - 2*s)
for i in range(n):
    x.append(2*a[i]-x[i])
x.pop(-1)
for i in range(n):
    print(x[i], end=' ')
print()