n = int(input())
s = list(map(int, input().split()))
right = 0
ans = 0
for left in range(n):
    while right < n-1 and s[right] < s[right+1]:
        right += 1
    ans += right - left + 1
    if right == left:
        right += 1
print(ans)