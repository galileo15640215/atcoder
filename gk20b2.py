t = int(input())
for i in range(t):
    n, d = map(int, input().split())
    x = list(map(int, input().split()))
    now = d-d%x[-1]
    for j in range(len(x)-1, -1, -1):
        now = now-now%x[j]
    print("Case #"+str(i+1)+": ", end='')
    print(now)