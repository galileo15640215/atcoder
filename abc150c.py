import itertools
n = int(input())
p = tuple(map(int, input().split()))
q = tuple(map(int, input().split()))
l = []
for i in range(1, n+1):
    l.append(i)
ll = list(itertools.permutations(l))
for i in range(len(ll)):
    if ll[i] == p:
        pre = i
    if ll[i] == q:
        pos = i
print(abs(pre-pos))