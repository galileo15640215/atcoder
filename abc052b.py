n = int(input())
s = input()
x = 0
ans = 0
for i in range(n):
    if s[i] == 'I':
        x += 1
        ans = max(ans, x)
    elif s[i] == 'D':
        x -= 1
print(ans)