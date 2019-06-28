h, w = map(int, input().split())
c = [list(input()) for i in range(h)]
ans = []
cnt = 0
while(cnt != h*w):
    for i in range(h):
        for j in range(w):
            tmp = 0
            if c[i][j] == '.':
                me = [i,j]
                # 上
                mas = c[i][j]
                if me[0]-1 >= 0:
                    mast = c[me[0]-1][me[1]]
                    while(mast == '.' and me[0]-1 >= 0):
                        mast = c[me[0]-1][me[1]]
                        me[0] -= 1
                        tmp += 1
                # 下
                me = [i,j]
                if me[0]+1 < h:
                    mast = c[me[0]+1][me[1]]
                    while(mast == '.' and me[0]+1 < h):
                        mast = c[me[0]+1][me[1]]
                        me[0] += 1
                        tmp += 1
                # 左
                me = [i,j]
                if me[1]-1 >= 0:
                    mast = c[me[0]][me[1]-1]
                    while(mast == '.' and me[1]-1 >= 0):
                        mast = c[me[0]][me[1]-1]
                        me[1] -= 1
                        tmp += 1
                # 右
                me = [i,j]
                if me[1]+1 < w:
                    mast = c[me[0]][me[1]+1]
                    while(mast == '.' and me[1]+1 < w):
                        mast = c[me[0]][me[1]+1]
                        me[1] += 1
                        tmp += 1
            ans.append(tmp)
    cnt += 1
print(max(ans))