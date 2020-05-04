n, k = map(int, input().split())
dic = {}
cnt = [0 for i in range(100001)]
for i in range(n):
    s, t = map(int, input().split())
    cnt[s] += t
for i in range(1, 100002):
    if k <= cnt[i]:
        print(i)
        break
    k -= cnt[i]
