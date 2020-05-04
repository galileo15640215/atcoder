n, s = map(int, input().split())
c = [0 for i in range(n)]
t = [0 for i in range(n)]
for i in range(n):
    c[i], t[i] = map(int, input().split())
mi = 1001
ans = 0
for i in range(n):
    if s >= t[i] and mi > c[i]:
        mi = c[i]
        ans = c[i]
if ans == 0:
    print("TLE")
else:
    print(ans)