n, m = map(int, input().split())
x = list(map(int, input().split()))
if n >= m:
    print(0)
else:
    x.sort()
    ku = []
    for i in range(len(x)-1):
        ku.append(abs(x[i]-x[i+1]))
    ku.sort()
    sum = 0
    for i in range(m-n):
        sum += ku[i]
    print(sum)