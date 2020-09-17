n = int(input())
s = [list(map(str, input().split())) for i in range(n)]
su = 0
ma = -1
idx = -1
for i in range(n):
    su += int(s[i][1])
    if ma < int(s[i][1]):
        ma = int(s[i][1])
        idx = i
if ma > su/2:
    print(s[idx][0])
else:
    print("atcoder")