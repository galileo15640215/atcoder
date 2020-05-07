n, k = map(int, input().split())
all = n*n*n
s = 1
s +=  (n-1)*3
if k != 1 and k != n:
    s += (k-1)*(n-k)*6
print(s/(n**3))