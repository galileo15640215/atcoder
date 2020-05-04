n = int(input())
a = list(map(int, input().split()))
cnt = 0
for i in range(n):
    tmp = a[i]
    while tmp%2 == 0:
        tmp /= 2
        cnt += 1
print(cnt)