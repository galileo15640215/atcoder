n, x, y = map(int, input().split())
l = [0]*(n-1)
for i in range(1, n+1):
    for j in range(i+1, n+1):
        num = min(abs(i-j), abs(i-x) + abs(j-y) + 1)
        l[num-1] += 1
for i in l:
    print(i)