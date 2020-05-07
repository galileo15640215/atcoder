import math
import heapq

def lcm(x, y):
    return (x * y) // math.gcd(x, y)

def is_prime(n):
    if n == 1: return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True

s = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

list.insert(idx, num)
list.reverse()
v.sort(key=lambda x: x[0])
l = list(itertools.combinations(range(1, m+1), n))
math.ceil(num)
#貪欲法

#ワーシャルフロイド
for k in range(10):
    for i in range(10):
        for j in range(10):
            c[i][j] = min(c[i][j], c[i][k] + c[k][j])

#しゃく取り法
right = 0
ans = 0
for left in range(n):
    while right < n-1 and s[right] < s[right+1]:
        right += 1
    ans += right - left + 1
    if right == left:
        right += 1

#優先度付きキュー
a = list(map(lambda x: x*(-1), a)) #最大値
heapq.heapify(a)
heapq.heappush(a, tmp)
