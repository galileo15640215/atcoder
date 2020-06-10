#bfs
import queue
 
h, w = map(int, input().split())
s = [list(input()) for i in range(h)]
visited = [[0 for i in range(w)] for j in range(h)]
c = [[99999999 for i in range(w)] for j in range(h)]
q = queue.Queue()
for i in range(h):
    for j in range(w):
        if s[i][j] == 'S':
            sy = i
            sx = j
        if s[i][j] == 'G':
            gy = i
            gx = j
q.put([sy, sx, 0])
visited[sy][sx] = 4
c[sy][sx] = 0
dyx = [[0, 1], [1, 0], [-1, 0], [0, -1]]
bre = 0
while not q.empty():
    now = q.get()
    flag = False
    if now[0] == gy and now[1] == gx:
        print(now[2])
        break
    for i in range(4):
        y = now[0] + dyx[i][0]
        x = now[1] + dyx[i][1]
        z = now[2]
        if 0 <= y < h and 0 <= x < w:
            if visited[y][x] != 4:
                visited[y][x] += 1
                q.put([y, x, z+1])
                if s[y][x] == '.':
                    if c[y][x] > c[now[0]][now[1]] + z + 1:
                        c[y][x] = c[now[0]][now[1]] + z + 1
                        q.put([y, x, z+1])
                elif s[y][x] == '#':
                    if c[y][x] > c[now[0]][now[1]] + z + bre + 1:
                        c[y][x] = c[now[0]][now[1]] + z + bre + 1
                        flag = True
                        q.put([y, x, z+bre+1])
    if flag:
        bre += 1
print(c)