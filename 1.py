s, t = map(str, input().split())
if s[0] == 'B' and t[0] == 'B':
    ans = abs(int(s[1]) - int(t[1]))
elif s[1] == 'F' and t[1] == 'F':
    ans = abs(int(s[0]) - int(t[0]))
elif s[0] == 'B' and t[1] == 'F':
    ans = int(t[0]) + int(s[1]) - 1
elif s[1] == 'F' and t[0] == 'B':
    ans = int(s[0]) + int(t[1]) - 1
print(ans)