n = int(input())
dic = {}
for i in range(n):
    s = input()
    if s not in dic:
        dic[s] = 1
    else:
        dic[s] += 1
dic_sorted = sorted(dic.items(), key=lambda x:x[1], reverse=True)
ans = []
s = []
for k, v in dic_sorted:
    s.append(v)
pre = s[0]
for k, v in dic_sorted:
    if v == pre:
        ans.append(k)
    else:
        break
ans.sort()
for i in ans:
    print(i)