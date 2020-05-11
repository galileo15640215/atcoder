s = input()
t = input()
flag = True
for i in range(len(s)):
    if s[i] != t[i]:
        flag = False
if flag:
    print("Yes")
else:
    print("No")