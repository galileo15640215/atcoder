s = input()
t = input()
sc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
so = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
flag1 = True
flag2 = True
for i in range(3):
    if s[i] == t[i]:
        pass
    elif s[i] != t[i]:
        flag1 = False
        if s[i] in sc:
            if s[i].upper() == t[i]:
                pass
            else:
                flag2 = False
        elif s[i] in so:
            if s[i].lower() == t[i]:
                pass
            else:
                flag2 = False
if flag1 and flag2:
    print("same")
elif not flag1 and flag2:
    print("case-insensitive")
else:
    print("different")