import math
a, b, h, m = map(int, input().split())
res = math.pi/2
hx = 0
hy = a
mx = 0
my = b
ho = res-2*math.pi*(h/12 + m/720)
mi = res-2*math.pi*m/60
hx = a*math.cos(ho)
hy = a*math.sin(ho)
mx = b*math.cos(mi)
my = b*math.sin(mi)

print(math.sqrt((hx-mx)**2 + (hy-my)**2))
