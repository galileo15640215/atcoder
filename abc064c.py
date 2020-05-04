n = int(input())
a = list(map(int, input().split()))
col = [0 for i in range(10)]
for i in range(n):
    if 1 <= a[i] and a[i] <= 399:
        col[0] = 1
    elif 400 <= a[i] and a[i] <= 799:
        col[1] = 1
    elif 800 <= a[i] and a[i] <= 1199:
        col[2] = 1
    elif 1200 <= a[i] and a[i] <= 1599:
        col[3] = 1
    elif 1600 <= a[i] and a[i] <= 1999:
        col[4] = 1
    elif 2000 <= a[i] and a[i] <= 2399:
        col[5] = 1
    elif 2400 <= a[i] and a[i] <= 2799:
        col[6] = 1
    elif 2800 <= a[i] and a[i] <= 3199:
        col[7] = 1
    elif 2800 <= a[i] and a[i] <= 3199:
        col[8] = 1
    elif 3200 <= a[i]:
        col[9] += 1
s = 0
for i in range(len(col)-1):
    s += col[i]
if s == 0 and col[9] >= 1:
    print(1, col[9])
elif col[9] >= 1:
    print(s, s+col[9])
else:
    print(s, s)