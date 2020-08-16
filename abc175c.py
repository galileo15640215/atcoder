x, k, d = map(int, input().split())
if x >= 0:
    if x - k*d >= 0:
        ans = abs(x - k*d)
    else:
        pre = x//d
        x -= pre*d
        k -= pre
        if k%2 == 0:
            ans = abs(x)
        elif k%2 == 1:
            ans = min(abs(x-d), abs(x+d))
elif x <= 0:
    if x + k*d <= 0:
        ans = abs(x + k*d)
    else:
        pre = abs(x)//d
        x += pre*d
        k -= pre
        if k%2 == 0:
            ans = abs(x)
        elif k%2 == 1:
            ans = min(abs(x-d), abs(x+d))
print(ans)