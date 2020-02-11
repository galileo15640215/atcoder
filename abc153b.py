h, n = map(int, input().split())
a = list(map(int, input().split()))
key = 0
for i in range(n):
    h -= a[i]
    if h <= 0:
        key = 1
        break
if key == 1:
    print("Yes")
else:
    print("No")