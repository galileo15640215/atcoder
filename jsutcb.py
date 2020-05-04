n = int(input())
xr = []
xb = []
cr = 0
cb = 0
for i in range(n):
    s, t = map(str, input().split())
    if t == "R":
        xr.append(int(s))
        cr += 1
    elif t == "B":
        xb.append(int(s))
        cb += 1
xr.sort()
xb.sort()
while cr+cb > 0:
    if cr > 0:
        print(xr.pop(0))
        cr -= 1
    else:
        print(xb.pop(0))
        cb -= 1