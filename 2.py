x, y = map(int, input().split())
flag = False
su = 2*x
if su == y:
    flag = True
for i in range(x):
    su += 2
    if su == y:
        flag = True
        break
if flag:
    print("Yes")
else:
    print("No")