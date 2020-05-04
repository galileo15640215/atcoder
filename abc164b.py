a, b, c, d = map(int, input().split())
while True:
    c -= b
    if c <= 0:
        flag = True
        break
    a -= d
    if a <= 0:
        flag = False
        break
if flag:
    print("Yes")
else:
    print("No")