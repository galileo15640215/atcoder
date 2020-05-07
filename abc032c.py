n, k = map(int, input().split())
s = []
for i in range(n):
    t = int(input())
    s.append(t)
sum = 1
right = 0
ans = 0
if 0 in s:
    print(n)
else:
    for left in range(n):
        while right < n and sum*s[right] <= k:
            sum *= s[right]
            right += 1
        if ans < right - left:
            ans = right - left
        if right == left:
            right += 1
        else:
            sum /= s[left]
    print(ans)