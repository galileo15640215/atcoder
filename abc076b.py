n = int(input())
k = int(input())
val = 1
for i in range(n):
    val = min(val*2, val+k)
print(val)