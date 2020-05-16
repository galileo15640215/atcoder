"""
def f(n):
    if n < 2:
        return 1
    else:
        return n*f(n-2)
"""
n = int(input())
if n%2 == 1:
    print(0)
else:
    n -= n%10
    res = 0
    tmp = 10
    while tmp <= n:
        res += n // tmp
        tmp *= 5
    print(res)