n, m, q = map(int, input().split())
s = [list(map(int, input().split())) for i in range(q)]
sco = [0 for i in range(n+1)]
poi = [n for i in range(m+1)]
dic = {}
for i in range(1, n+1):
    dic[i] = []
for i in range(q):
    if s[i][0] == 1:
        su = 0
        for j in dic[s[i][1]]:
            su += poi[j]
        print(su)
    elif s[i][0] == 2:
        poi[s[i][2]] -= 1
        dic[s[i][1]].append(s[i][2])