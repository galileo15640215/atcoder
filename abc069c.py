n = int(input())
a = list(map(int, input().split()))
x = 0
y = 0
z = 0
for i in range(n):
    if a[i]%4 == 0:
        x += 1
    elif a[i]%2 == 0:
        y += 1
    else:
        z += 1
if y == 0:
    if x+1 >= z:
        print("Yes")
    else:
        print("No")
else:
    if x >= z:
        print("Yes")
    else:
        print("No")
