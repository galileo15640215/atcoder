def factorization(n):
    arr = [[1, 1]]
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
def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)
a, b = map(int, input().split())
g = gcd(a, b)
l = factorization(g)
print(len(l))