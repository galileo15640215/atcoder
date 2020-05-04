n = int(input())
a = list(map(int, input().split()))
x = []
for i in range(n):
    x.append(a[i]-i-1)
x.sort()
if n%2 == 1:
    b = x[n//2]
else:
    b = (x[n//2-1] + x[n//2])/2
sum = 0
for i in range(n):
    sum += abs(a[i]-(b+i+1))
print(int(sum))