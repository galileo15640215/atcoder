n = int(input())
a = list(map(int, input().split()))
cnt = [0 for i in range(n)]
for i in range(n-1):
    cnt[a[i]-1] += 1
for i in range(n):
    print(cnt[i])