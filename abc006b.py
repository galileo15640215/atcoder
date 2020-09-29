n = int(input())

mod = 10007

a = [0] * (n if n >= 3 else 3)

a[0], a[1], a[2] = 0, 0, 1

for i in range(3,n):
  a[i] = (a[i-1] + a[i-2] + a[i-3]) % mod
  
print(a[n-1])
