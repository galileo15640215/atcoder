l, r = map(int, input().split())
m = int(input())
n = list(map(int, input().split()))
ans = r-l+1
for i in range(m):
    ans -= (r-l)//n[i]
print(ans)