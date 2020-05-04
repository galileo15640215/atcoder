s = input()
flag = True
ko = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
if s[0] == 'A':
    pass
else:
    flag = False
cnt = 0
for i in range(2, len(s)-1):
    if s[i] == 'C':
        cnt += 1
        id = i
if cnt == 1:
    pass
else:
    flag = False
if flag:
    for i in range(1, len(s)):
        if id != i:
            if s[i] not in ko:
                flag = False
if flag:
    print("AC")
else:
    print("WA")
