import math
import heapq

def lcm(x, y):
    return (x * y) // math.gcd(x, y)
def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y) #再帰定義
def is_prime(n):
    if n == 1: return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True

#nの約数を全て求める
def divisor(n): 
    i = 1
    table = []
    while i * i <= n:
        if n%i == 0:
            table.append(i)
            table.append(n//i)
        i += 1
    table = list(set(table))
    return table
#公約数を求める
def cf(x1,x2):
    cf=[]
    for i in range(2,min(x1,x2)+1):
        if x1 % i == 0 and x2 % i == 0:
            cf.append(i)
    return cf

''.join(s)
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

#2分探索
from bisect import bisect_left
def index(lst, e):
    i = bisect_left(lst, e)    
    if i == len(lst):
        raise ValueError
    if lst[i] != e:
        raise ValueError    
    return i
lst = [7, 31, 41, 78, 91]
index(lst,   7)
index(lst,  31)

import bisect
#配列を用意。作りながら昇順にソート
#(勿論、適当に配列を作ってソートしてもOKだけど、
#bisectの例題なので、insort_leftを使ってみた。）
array = []
bisect.insort_left(array, 9)
bisect.insort_left(array, 1)
bisect.insort_left(array, 7)
bisect.insort_left(array, 3)
bisect.insort_left(array, 11)
bisect.insort_left(array, 5)
#配列を書き出してみるとソートされている
print array
[1, 3, 5, 7, 9, 11]
# 検索　（戻り値はインデックス）
bisect.bisect_left(array, 8)
bisect.bisect_right(array, 9)

#bit全探索
for i in range(n**2):
    op = [False]*n
    for j in range(n):
        if i >> j & 1:
            op[n-1-j] = True
    print(op)

#ゼロ埋め
s.zfill(8)

#コピー
import copy
q = copy.copy(p)

#素因数分解
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