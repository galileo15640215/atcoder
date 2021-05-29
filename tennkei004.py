h, w = map(int, input().split())
a = [list(map(int, input().split())) for i in range(h)]
hh = [0 for i in range(h)]
ww = [0 for i in range(w)]
for i in range(h):
    for j in range(w):
        hh[i] += a[i][j]
for j in range(w):
    for i in range(h):
        ww[j] += a[i][j]
for i in range(h):
    for j in range(w):
        print(hh[i] + ww[j] - a[i][j], end=' ')
    print()
