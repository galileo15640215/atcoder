a, b = map(int, input().split())
n = 1
for i in range(1, b+1):
    if (a*i) % b == 0:
        print(a*i)
        break
