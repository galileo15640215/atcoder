a, b, t = map(int, input().split())
 
cnt = 0
time = 0
while(1):
  if time > t:
    break
  cnt += b
  time += a
cnt -= b
print(cnt)