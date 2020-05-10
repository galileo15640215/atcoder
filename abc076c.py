s = list(input())
t = list(input())
idx = -1
jdx = -1
for i in range(len(s)-1, -1, -1):
    for j in range(len(t)-1, -1, -1):
        if s[i] == t[j]:
            print(i, j)
            k = i
            l = j
            while s[k] == t[l]:
                k += 1
                l += 1
            idx = i
            jdx = k
print(idx, jdx)
for i in range(0, idx):
    if s[i] == '?':
        print('a', end='')
    else:
        print(s[i], end='')
for i in range(idx, jdx):
    print(t[i], end='')
for i in range(jdx, len(s)):
    if s[i] == '?':
        print('a', end='')
    else:
        print(s[i], end='')