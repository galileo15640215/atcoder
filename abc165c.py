import itertools
n, m, q = map(int, input().split())
a = []
b = []
c = []
d = []
for i in range(q):
    s = list(map(int, input().split()))
    a.append(s[0])
    b.append(s[1])
    c.append(s[2])
    d.append(s[3])
sum = 0
l = list(itertools.combinations(range(1, m+1), n))
print(l)
for i in range(len(l)):
    A = l[i]
    tmp = 0
    for j in range(q):
        if A[b[j]-1] - A[a[j]-1] == c[j]:
            tmp += d[j]
    if sum < tmp:
        sum = tmp
print(sum)