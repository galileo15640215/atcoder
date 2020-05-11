n = int(input())
a = [int(input()) for i in range(n)]
l = [0 for i in range(100001)]
cnt = 0
for i in range(n):
    if l[a[i]] == 1:
        cnt += 1
    else:
        l[a[i]] = 1
print(cnt)
