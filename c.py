import itertools
n, m, x = map(int, input().split())
c = [list(map(int, input().split())) for i in range(n)]
comb = []
for i in range(1, n+1):
    comb.append(list(itertools.combinations(c, i)))
ans = []
for i in range(len(comb)):
    for j in range(len(comb[i])):
        flag = True
        for l in range(1, m):
            sum = 0
            for k in range(n):
                print(i, j, comb[i][j][k], comb[i][j][k][l])
                sum += comb[i][j][k][l]
            if sum < x:
                flag = False
                break
            if flag:
                cos = 0
                for k in range(len(comb[i][j])):
                    cos += comb[i][j][k][0]
        if not flag:
            break
    if flag:
        ans.append(cos)
print(ans)
if ans:
    print(min(ans))
else:
    print(-1)