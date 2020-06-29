d = int(input())
c = list(map(int, input().split()))
s = [list(map(int, input().split())) for i in range(d)]
t = [int(input()) for i in range(d)]
m = int(input())
q = [list(map(int, input().split())) for i in range(d)]
mem = [0 for i in range(26)]
ans = []
v = 0
su = sum(c)
ol = t
for b in range(m):
    for j in range(26):
        mem[j] = 0
    ol[q[b][0]-1] = q[b][1]
    v = 0
    for a in range(d):
        v += s[a][ol[a]-1]
        mem[ol[a]-1] = a+1
        for i in range(26):
            v -= c[i]*(a+1 - mem[i])
    print(v)