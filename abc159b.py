s = input()
flag = True
n = len(s)
for i in range(n):
    if s[i] != s[n-1-i]:
        flag = False
for i in range((n-1)//2):
    if s[i] != s[(n-1)//2-1-i]:
        flag = False
for i in range((n+3)//2+1, n):
    if s[i] != s[n-1-i]:
        flag = False
if flag:
    print("Yes")
else:
    print("No")666666   222                                                                                                                                 