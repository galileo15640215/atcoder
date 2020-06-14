a = list(map(int, input().split()))
l = [0, 0]
for i in range(3):
    if a[i] == 5:
        l[0] += 1
    elif a[i] == 7:
        l[1] += 1
if l[0] == 2 and l[1] == 1:
    print("YES")
else:
    print("NO")