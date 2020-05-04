s, l, r = map(int, input().split())
x = s
while True:
    if l <= x <= r:
        break
    elif x < l:
        x += 1
    elif x > r:
        x -= 1
print(x)