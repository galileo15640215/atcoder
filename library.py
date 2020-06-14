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
#第2キーの点数を降順にしたい場合、-をつける
sorted(a, key=lambda x:(x[0],-x[1]))
l = list(itertools.combinations(range(1, m+1), n))
#ソート済みの状態を維持
import bisect
index = bisect.bisect_left(l, j)
l.insert(index, j)
#切り上げ
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


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


#BFS幅優先探索
#bfs
import queue

visited = [[0 for i in range(lim)] for j in range(lim)]
c = [['.' for j in range(lim)] for i in range(lim)]
c[201][201] = 'S'
c[w][h] = 'G'
for i in range(n):
    s, t = map(int, input().split())
    s += 201
    t += 201
    visited[t][s] = 999999999
    c[t][s] = '#'
q = queue.Queue()
q.put([201, 201])
ans = 0
visited[201][201] = 1
dy_dx = [[1,1], [1,0], [1,-1], [0,1], [0,-1], [-1,0]]
flag = False
while not q.empty():
    now = q.get() # now[0]..y, now[1]..x
    if c[now[0]][now[1]] == 'G':
        flag = True
        break
    for i in range(6):
        y = now[0] + dy_dx[i][0]
        x = now[1] + dy_dx[i][1]
        if 0 <= y < lim and 0 <= x < lim:
            if c[y][x] != '#' and visited[y][x] == 0:
                visited[y][x] = visited[now[0]][now[1]] + 1
                q.put([y, x])
#累積和
rui = [0]
for j in range(1, n):
    rui.append(rui[j-1] + a[j-1])
