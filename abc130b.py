n, x = map(int, input().split())
l = [int(i) for i in input().split()]
cnt = 1
i = 0
now = 1
ans = [1]*(x+l[-1])
sum = 0
for i in range(n):
    for j in range(sum + l[i], x+l[-1]):
        ans[j] += 1
    sum += l[i]
print(ans[x])