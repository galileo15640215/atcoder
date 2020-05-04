n = int(input())
a = []
for i in range(n):
    s, t = map(int, input().split())
    a.append([s, t])
a = sorted(a, key=lambda x: x[1])
time = 0
flag = True
for i in range(n):
    time += a[i][0]
    if time > a[i][1]:
        flag = False
        break
if flag:
    print("Yes")
else:
    print("No")