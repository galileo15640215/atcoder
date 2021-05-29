n = int(input())
s = list(input() for i in range(n))
dic = {}
for i in range(n):
    if s[i] not in dic.keys():
        dic[s[i]] = i+1
for i in list(dic.values()):
    print(i)