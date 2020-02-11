h, a = map(int, input().split())
ans = int(h/a)
if h%a == 0:
    print(ans)
else:
    print(ans+1)