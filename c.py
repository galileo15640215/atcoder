import math
a, b, h, m = map(int, input().split())

ho = 90
mi = 90

res = math.pi/2
"""
hx = a*math.cos(res)
hy = a*math.sin(res)
mx = b*math.cos(res)
my = b*math.sin(res)
"""
hx = 0
hy = a
mx = 0
my = b
print(hx, hy)
print(mx, my)

ho = res-2*math.pi*h/12
mi = res-2*math.pi*m/60

hx = a*math.cos(ho)
hy = a*math.sin(ho)
mx = b*math.cos(mi)
my = b*math.sin(mi)
print(hx, hy)
print(mx, my)
print(math.sqrt((hx-mx)**2 + (hy-my)**2))
