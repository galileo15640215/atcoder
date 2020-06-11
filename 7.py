import math

def get_sieve_of_eratosthenes(n):
    if not isinstance(n, int):
        raise TypeError('n is int type.')
    if n < 2:
        raise ValueError('n is more than 2')
    prime = []
    limit = math.sqrt(n)
    data = [i + 1 for i in range(1, n)]
    while True:
        p = data[0]
        if limit <= p:
            return prime + data
        prime.append(p)
        data = [e for e in data if e % p != 0]

l, r = map(int, input().split())
m = int(input())
n = list(map(int, input().split()))

n.sort()
flag = True
while flag:
    flag = False
    for i in range(len(n)-1):
        for j in range(i+1, len(n)):
            if n[j]%n[i] == 0:
                n.pop(j)
                flag = True
                break
        if flag:
            break
ans = r-l+1
m = len(n)
if 1 in n:
    print(0)
else:
    for i in range(l, r+1):
        for j in range(m):
            if i%n[j] == 0:
                ans -= 1
                break
    print(ans)