n, k = map(int, input().split())
cnt = 0
MOD = 1000000007
for i in range(k, n+2):
    left = i*(i-1)//2
    right = i*(2*n-i+1)//2
    add = right - left + 1
    cnt = (cnt+add)%MOD
print(cnt)