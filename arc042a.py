n, m = map(int, input().split())
a = [int(input()) for i in range(m)]
cnt = [0 for i in range(n)]
l = []
for i in range(m-1,-1, -1):
    if cnt[a[i]-1] == 0:
        cnt[a[i]-1] += 1
        l.append(a[i])
for i in range(len(l)):
    print(l[i])
for i in range(n):
    if cnt[i] == 0:
        print(i+1)