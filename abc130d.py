n, k = map(int, input().split())
a = list(map(int, input().split()))
sum = 0
right = 0
ans = 0
for left in range(n):
    while right < n and sum < k:
        sum += a[right]
        right += 1
    if sum < k:
        break
    ans += n - right + 1
    if right == left:
        right += 1
    else:
        sum -= a[left]
print(ans)