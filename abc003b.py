s = list(input())
t = list(input())
l = ['a', 't', 'c', 'o', 'd', 'e', 'r']
flag = True
for i in range(len(s)):
    if s[i] != t[i]:
        if (s[i] == '@' and (t[i] in l)) or (t[i] == '@' and (s[i] in l)):
            pass
        else:
            flag = False
if flag:
    print("You can win")
else:
    print("You will lose")