n = int(input())
a = list(map(int, input().split()))
dic = {}
for i in range(n):
    if a[i] not in dic.keys():
        dic[a[i]] = 1
    else:
        dic[a[i]] += 1
cnt = 0
for i in dic.keys():
    if dic[i] > i:
        cnt += i
    else:
        cnt += i-dic[i] 
print(cnt)