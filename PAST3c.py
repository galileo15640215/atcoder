mas = 10**9
def pow_k(x, n):
    """
    O(log n)
    """
    if n == 0:
        return 1

    K = 1
    while n > 1:
        if n % 2 != 0:
            K *= x
        x *= x
        n //= 2
    return K * x
"""
2**30
3**19
4**15
5**13
6**9
7**
"""
a, r, n = map(int, input().split())
if r == 1 :
    ans = a
elif r >= 2 and n >= 31:
    ans = mas + 1
else:
    ans = a*(pow(r, n-1))
if ans > mas:
    print("large")
else:
    print(ans)