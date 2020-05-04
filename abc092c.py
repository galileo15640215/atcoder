n = int(input())
a = []
a = list(map(int, input().split()))
a.insert(0, 0)
a.append(0)
sum = 0
for i in range(n+1):
    sum += abs(a[i]-a[i+1])
for i in range(1, n+1):
    print(sum - abs(a[i-1]-a[i]) - abs(a[i]-a[i+1]) + abs(a[i-1]-a[i+1]))
