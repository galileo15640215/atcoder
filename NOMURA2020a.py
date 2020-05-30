h, m, x, y, k = map(int, input().split())
mi = x*60 + y - (h*60+m) - k
print(mi)