#bfs
import queue

n, h, w = map(int, input().split())
h += 201
w += 201
lim = 405
visited = [[0 for i in range(lim)] for j in range(lim)]
c = [['.' for j in range(lim)] for i in range(lim)]
c[201][201] = 'S'
c[w][h] = 'G'
for i in range(n):
    s, t = map(int, input().split())
    s += 201
    t += 201
    visited[t][s] = 999999999
    c[t][s] = '#'
q = queue.Queue()
q.put([201, 201])
ans = 0
visited[201][201] = 1
dy_dx = [[1,1], [1,0], [1,-1], [0,1], [0,-1], [-1,0]]
flag = False
while not q.empty():
    now = q.get() # now[0]..y, now[1]..x
    if c[now[0]][now[1]] == 'G':
        flag = True
        break
    for i in range(6):
        y = now[0] + dy_dx[i][0]
        x = now[1] + dy_dx[i][1]
        if 0 <= y < lim and 0 <= x < lim:
            if c[y][x] != '#' and visited[y][x] == 0:
                visited[y][x] = visited[now[0]][now[1]] + 1
                q.put([y, x])
"""
for i in range(lim):
    for j in range(lim):
        if visited[j][i] != 0:
            print(visited[j][i], j, i)
"""
if flag:
    print(visited[w][h]-1)
else:
    print(-1)