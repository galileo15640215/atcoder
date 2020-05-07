n, m = map(int, input().split())
a = list(map(int, input().split()))
b = []
a.sort()
for i in range(m):
    s, t = map(int, input().split())
    if t > a[0]:
        b.append([s, t])
b.sort(reverse=True, key=lambda x: x[1])
j = 0
for i in range(len(b)):
    if j >= n:
        break
    while a[j] < b[i][1] and b[i][0] >= 1:
        a[j] = b[i][1]
        b[i][0] -= 1
        j += 1
        if j >= n:
            break
print(sum(a))