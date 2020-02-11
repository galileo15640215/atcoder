a, b = map(int, input().split())
flag = False
for i in range(1, 4):
    if a*b*i%2 == 1:
        flag = True
if flag:
    print("Yes")
else:
    print("No")