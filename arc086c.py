n, k = map(int, input().split())
a = list(map(int, input().split()))
l = [0 for i in range(n)]
for i in range(n):
    l[a[i]-1] += 1
l.sort()
cnt = 0
for i in range(n-k):
    cnt += l[i]
print(cnt)