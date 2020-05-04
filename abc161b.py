n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)
s = sum(a)
flag = True
for i in range(m):
    if a[i] < 1/(4*m)*s:
        flag = False
        break
if flag:
    print("Yes")
else:
    print("No")