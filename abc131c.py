from fractions import gcd
def lcm(x, y):
    return (x * y) // gcd(x, y)
a, b, c, d = map(int, input().split())
print(b-(a-1) - b//c + (a-1)//c - b//d + (a-1)//d + b//lcm(c, d) - (a-1)//lcm(c, d))