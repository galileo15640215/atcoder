s = input()
flag = True
for i in range(len(s)):
    if i%2 == 0:
        if s[i] == "R" or s[i] == "U" or s[i] == "D":
            pass
        else:
            flag = False
            break
    elif i%2 == 1:
        if s[i] == "L" or s[i] == "U" or s[i] == "D":
            pass
        else:
            flag = False
            break
if flag:
    print("Yes")
else:
    print("No")