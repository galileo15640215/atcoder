s = input()
k = int(input())
flag = False
for i in range(k):
    if s[i] != '1':
        id = s[i]
        flag = True
        break
if flag:
    print(id)
else:
    print(1)
