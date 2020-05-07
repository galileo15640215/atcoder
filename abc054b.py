n, m = map(int, input().split())
a = [list(input()) for i in range(n)]
b = [list(input()) for i in range(m)]
for i in range(n-m+1):
    for j in range(n-m+1):
        flag = True
        if a[i][j] == b[0][0]:
            for k in range(m):
                for l in range(m):
                    if a[i+k][j+l] != b[k][l]:
                        flag = False
                        break
                if not flag:
                    break
        else:
            flag = False
        if flag:
            break
    if flag:
        break
if flag:
    print("Yes")
else:
    print("No")