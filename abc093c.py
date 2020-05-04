a, b, c = map(int, input().split())
l = [a, b, c]
l.sort()
a, b, c = l[0], l[1], l[2]
cnt = 0
while not (a == b and b == c and a == c):
    a, b, c = l[0], l[1], l[2]
    if a+2 <= c:
        a += 2
    elif b+2 <= c:
        c += 2
    else:
        a += 1
        b += 1
    l[0] = a
    l[1] = b
    l[2] = c
    l.sort()
    cnt += 1
print(cnt)