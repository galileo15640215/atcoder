h, w = map(int, input().split())
n = int(input())
a = list(map(int, input().split()))
field = [[0 for j in range(w)] for i in range(h)]
#[y, x]
d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
y, x = 0, 0
if h == 1 and w == 1:
    print(1)
else:
    for i in range(n):
        cnt = a[i]
        while cnt > 0:
            for j in range(len(d)):
                if 0 <= y + d[j][0] and y + d[j][0] < h and 0 <= x + d[j][1] and x + d[j][1] < w:
                    if field[y+d[j][0]][x+d[j][1]] == 0: 
                        dy, dx = d[j][0], d[j][1]
                        break
            field[y][x] = i+1
            y += dy
            x += dx
            cnt -= 1
    for i in range(h):
        for j in range(w):
            print(field[i][j], end=' ')
        print()