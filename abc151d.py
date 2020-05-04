#bfs
import queue

h, w = map(int, input().split())
c = [list(input()) for i in range(h)]
visited = [[0 for i in range(w)] for j in range(h)]
q = queue.Queue()
ans = 0
            
dyx = [[0, 1], [1, 0], [-1, 0], [0, -1]]

for i in range(h):
    for j in range(w):
        if c[i][j] == '.':
            q.put([i, j])
            visited[i][j] = 1
            while not q.empty():
                now = q.get()
                for k in range(4):
                    y = now[0] + dyx[k][0]
                    x = now[1] + dyx[k][1]
                    if 0 <= y < h and 0 <= x < w:
                        if c[y][x] != '#' and visited[y][x] == 0:
                            visited[y][x] = visited[now[0]][now[1]] + 1
                            q.put([y, x])
        for l in range(h):
            for m in range(w):
                ans = max(ans, visited[l][m])
        queue = []
        visited = [[0 for i in range(w)] for j in range(h)]
print(ans-1)