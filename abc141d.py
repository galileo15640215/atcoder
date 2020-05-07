import heapq
import math
n, m = map(int, input().split())
a = list(map(int, input().split()))
a = list(map(lambda x: x*(-1), a)) 
heapq.heapify(a)
for i in range(m):
    tmp = math.ceil(heapq.heappop(a)/2)
    heapq.heappush(a, tmp)
a = list(map(lambda x: x*(-1), a)) 
print(sum(a))