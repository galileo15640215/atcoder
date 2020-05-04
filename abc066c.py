n = int(input())
a = list(map(int, input().split()))
b = []
c = []
flag = True
for i in range(n):
    if flag:
        b.append(a[i])
        flag = False
    else:
        c.append(a[i])
        flag = True
if flag:
    c.reverse()
    ans = c+b
else:
    b.reverse()
    ans = b+c
for i in range(n):
    print(ans[i], end=" ")
print()