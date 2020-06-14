def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

n = int(input())
a = list(map(int, input().split()))
a.sort()
cnt = n
dic = {}
for i in range(n):
    if a[i] not in dic.keys():
        dic[a[i]] = 1
    else:
        dic[a[i]] += 1
l = []
res = list(dic.keys())
for i in res:
    l.append(make_divisors(i)[1:])
print(l)
print(res)
chk = [0 for i in range(len(res))]
for i in range(res):
    for j in range(i+1, len(l)):
        if chk[j] == 0:
            for k in range(len(l[j])):
                if res[i] == l[j][k]:
                    cnt -= dic[res]
                    break
            
"""
flag = True
for i in range(n-1):
    if a[i] != a[i+1]:
        flag = False
        break
if n == 1:
    cnt = 1
elif flag:
    cnt = 0
else:
    for i in range(n-1, 0, -1):
        for j in range(0, i, 1):
            if a[i] == a[j] or a[i] == a[j+1]:
                cnt -= 1
                break
            elif a[i]/2 < a[j]:
                break
            elif a[i]%a[j] == 0:
                cnt -= 1
                break
print(cnt)
"""