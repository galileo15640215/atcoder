n = int(input())
res = []
for i in range(1, int(n**0.5)+1):
    if n%i == 0:
        res.append([i, int(n/i)])
ans = 10**9+1
for i in range(len(res)):
    tmp = max(len(str(res[i][0])), len(str(res[i][1])))
    if ans > tmp:
        ans = tmp
print(ans)