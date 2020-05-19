s =input()
a = 0
b = 0
c = 0
for i in range(len(s)):
    if s[i] == 'a':
        a += 1
    elif s[i] == 'b':
        b += 1
    elif s[i] == 'c':
        c += 1
ans = max(max(a, b), c)
if ans == a:
    print('a')
elif ans == b:
    print('b')
else:
    print('c')