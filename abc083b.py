n, a, b = map(int, input().split())
ans = 0
for i in range(1, n+1):
    s = str(i)
    su = 0
    for j in range(len(s)):
        su += int(s[j])
    if a <= su and su <= b:
        ans += i
print(ans)