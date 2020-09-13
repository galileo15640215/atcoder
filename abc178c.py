import math
n = int(input())
"""
0
[0, 9], [9, 0]
[0, 0, 9], [0, 1, 9] 9*3!

9**n*n!
"""
if n == 1:
    print(0)
else:
    print(10**(n-2)*(math.factorial(n))%(10**9+7))