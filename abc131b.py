n, l = map(int, input().split())
sum = 0
min = 1000
for i in range(1, n+1):
    aji = l+i-1
    sum += aji
    if abs(min) > abs(aji):
        min = aji
print(sum-min)