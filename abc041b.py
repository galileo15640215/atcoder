n = int(input())
a = list(map(int, input().split()))
b = []
for i in range(n):
    b.append([a[i], i+1])
b.sort(reverse=True, key=lambda x: x[0])
for i in range(n):
    print(b[i][1])