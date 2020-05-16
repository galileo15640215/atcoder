t = int(input())
for i in range(t):
    n = int(input())
    h = list(map(int, input().split()))
    cnt = 0
    for j in range(1, n-1):
        if h[j-1] < h[j] and h[j] > h[j+1]:
            cnt += 1
    print("Case #"+str(i+1)+": ", end='')
    print(cnt)