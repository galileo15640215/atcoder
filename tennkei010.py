n = int(input())
c = [list(map(int, input().split())) for i in range(n)]
q = int(input())
l = [list(map(int, input().split())) for i in range(q)]
for p in range(q):
    ans1 = 0
    ans2 = 0
    for i in range(l[p][0]-1, l[p][1]):
        if c[i][0] == 1:
            ans1 += c[i][1]
        elif c[i][0] == 2:
            ans2 += c[i][1]
    print(ans1, ans2)