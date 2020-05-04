x, y, a, b, c = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))
p.sort()
q.sort()
r.sort()
tx = 0
ty = 0
sc= 0
while tx != x or ty != y:
    fp = True
    fq = True
    fr = True
    if p and r:
        if p[-1] >= r[-1] and tx < x:
            sc += p.pop(-1)
            tx += 1
            fp = False
    if q and r:
        if q[-1] >= r[-1] and ty < y:
            sc += q.pop(-1)
            ty += 1
            fq = False
    if p and r:
        if p[-1] <= r[-1] and tx < x:
            sc += r.pop(-1)
            tx += 1
            fr = False
    if q and r:
        if q[-1] <= r[-1] and ty < y:
            sc += r.pop(-1)
            ty += 1
            fr = False
    if fp:
        if p and tx < x:
            sc += p.pop(-1)
            tx += 1
    if fq:
        if q and ty < y:
            sc += q.pop(-1)
            ty += 1
    if fq:
        if r and tx < x:
            sc += r.pop(-1)
            tx += 1
        elif r and ty < y:
            sc += r.pop(-1)
            ty += 1
print(sc)