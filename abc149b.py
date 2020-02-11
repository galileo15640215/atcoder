a, b, k = map(int, input().split())
ca = a-k
if ca >= 0:
    print(ca, b)
else:
    cb = b + ca
    if cb < 0:
        print(0, 0)
    else:
        print(0, cb)