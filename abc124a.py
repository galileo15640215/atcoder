a,b = (int(i) for i in input().split())  
sum = 0
sum += max(a,b)
if a > b:
  a -= 1
else:
  b -= 1
sum += max(a,b)
print(sum)