n = int(input())
a = list(map(int,input().split()))
ans = 0
for i in a:
    if i == 2:
        ans += 1
    elif i == 4:
        ans += 1
    elif i == 5:
        ans += 2
    elif i == 6:
        ans += 3
    elif i == 8:
        ans += 1
print(ans)
