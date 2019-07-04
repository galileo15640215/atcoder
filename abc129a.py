p, q,  r = map(int, input().split())
l = []
l.append(p+q)
l.append(q+r)
l.append(r+p)
print(min(l))