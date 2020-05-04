from collections import Counter
n=int(input())
s = []
for i in range(n):
    t = list(input())
    t.sort()
    s.append(''.join(t))
c = Counter(s)
sum = 0
for i in c.values():
    sum += i*(i-1)//2
print(sum)

"""
n = int(input())
dic = {}
for i in range(n):
    s = list(input())
    s.sort()
    t = "".join(s)
    if t in dic.keys():
        dic[t] += dic[t] + 1
    elif t not in dic.keys():
        dic[t] = 0
print(sum(dic.values()))
"""