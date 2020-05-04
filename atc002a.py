#bfs
import queue

h, w = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
c = [list(input()) for i in range(h)]
visited = [[0 for i in range(w)] for j in range(h)]
q = queue.Queue()
q.put([sy-1, sx-1, 0])
visited[sy-1][sx-1] = 1
dyx = [[0, 1], [1, 0], [-1, 0], [0, -1]]
while not q.empty():
    now = q.get()
    if now[0] == gy-1 and now[1] == gx-1:
        print(now[2])
        break
    for i in range(4):
        y = now[0] + dyx[i][0]
        x = now[1] + dyx[i][1]
        z = now[2]
        if 0 <= y < h and 0 <= x < w:
            if c[y][x] != '#' and visited[y][x] == 0:
                visited[y][x] = 1
                q.put([y, x, z+1])
