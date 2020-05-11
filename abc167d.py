n, k = map(int, input().split())
a = list(map(int, input().split()))
s = []
ord = [-1 for i in range(n+1)]
v = 1
c = 1
l = 0
while ord[v] == -1:
    ord[v] = len(s)
    s.append(v)
    v = a[v-1]
c = len(s) - ord[v]
l = ord[v]
if k < l:
    print(s[k])
else:
    k -= l
    k %= c
    print(s[l+k])