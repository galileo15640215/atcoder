n = int(input())
a = list(map(int, input().split()))
su = sum(a)
if su%n != 0:
    print(-1)
else:
    left = 0
    right = su
    cnt = 0
    for i in range(n):
        left += a[i]
        right -= a[i]
        if left != su//n*(i+1) or right != su//n*(n-i-1):
            cnt += 1
    print(cnt)