n, k = map(int, input().split())
d = list(map(str, input().split()))
"""
l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(k):
    for j in range(len(l)):
        if d[i] == l[j]:
            l.pop(j)
            break
"""
while True:
    tmp = list(str(n))
    flag = True
    for i in range(len(d)):
        if d[i] in tmp:
            flag = False
            break
    if flag:
        break
    n += 1
print(n)