s = input()
l = ['A', 'B', 'C', 'D', 'E', 'F']
ans = [0 for i in range(6)]
for i in range(len(s)):
    for j in range(len(l)):
        if s[i] == l[j]:
            ans[j] += 1
for i in range(len(ans)):
    if i == len(ans)-1:
        print(ans[i])
    else:
        print(ans[i], end=' ')
