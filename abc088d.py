#bfs
import queue

h, w = map(int, input().split())
c = [list(input()) for i in range(h)]
emp = 0
for i in range(h):
    for j in range(w):
        if c[i][j] == '.':
            emp += 1

visited = [[0 for i in range(w)] for j in range(h)]
q = queue.Queue()
q.put([0, 0, 1])
visited[0][0] = 1
dyx = [[0, 1], [1, 0], [-1, 0], [0, -1]]
flag = False
while not q.empty():
    now = q.get()
    if now[0] == h-1 and now[1] == w-1:
        flag = True
        break
    for i in range(4):
        y = now[0] + dyx[i][0]
        x = now[1] + dyx[i][1]
        z = now[2]
        if 0 <= y < h and 0 <= x < w:
            if c[y][x] != '#' and visited[y][x] == 0:
                visited[y][x] = 1
                q.put([y, x, z+1])
if flag:
    print(emp-now[2])
else:
    print(-1)