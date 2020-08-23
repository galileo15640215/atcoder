n = input()
su = 0
for i in range(len(n)):
    su += int(n[i])
if su%9 == 0:
    print("Yes")
else:
    print("No")