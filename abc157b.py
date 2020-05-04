a = []
for i in range(3):
    aa = list(map(int, input().split()))
    a.append(aa)
n = int(input())
flag = []
for i in range(3):
    flag.append([0, 0, 0])
for i in range(n):
    b = int(input())
    for j in range(3):
        for k in range(3):
            if a[j][k] == b:
                flag[j][k] = 1
ans = False
for j in range(3):
    if flag[0][j] == 1 and flag [1][j] == 1 and flag[2][j] == 1:
        ans = True
for i in range(3):
    if flag[i][0] == 1 and flag [i][1] == 1 and flag[i][2] == 1:
        ans = True
if flag[0][0] == 1 and flag [1][1] == 1 and flag[2][2] == 1:
        ans = True
if flag[2][0] == 1 and flag [1][1] == 1 and flag[0][2] == 1:
        ans = True
if ans:
    print("Yes")
else:
    print("No")