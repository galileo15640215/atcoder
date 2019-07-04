n = int(input())
w = list(map(int, input().split()))
l = []
for i in range(1, n):
    s1 = 0
    s2 = 0
    for j in range(0, i):
        s1 += w[j]
    s2 = sum(w) -s1
    l.append(abs(s1-s2))
print(min(l))