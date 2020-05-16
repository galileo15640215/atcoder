def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr
n = int(input())
dic = {}
for i in range(2, n+1):
    l = factorization(i)
    for j in range(len(l)):
        if l[j][0] not in dic.keys():
            dic[l[j][0]] = 1
        else:
            dic[l[j][0]] += l[j][1]
ans = 1
for i in dic.keys():
    ans *= dic[i]+1
MOD = 10**9+7
print(ans%MOD)