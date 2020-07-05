n = int(input())
for i in range(1000, 10001, 1000):
    if n <= i:
        print(i-n)
        break