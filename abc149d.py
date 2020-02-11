a, b = map(int, input().split())
n = 1
while True:
    if n%a == 0 and n%b == 0:
        print(n)
        break
    n += 1