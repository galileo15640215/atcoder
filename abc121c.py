n, m = map(int, input().split())
a = []
for i in range(n):
    l = list(map(int, input().split()))
    a.append(l)
a.sort(key=lambda x: x[0])
sum = 0
cnt = 0
for i in range(n):
    if cnt + a[i][1] >= m:
        sum += (m-cnt)*a[i][0]
        cnt += m-cnt
        break
    else:
        sum += a[i][0]*a[i][1]
        cnt += a[i][1]
print(sum)