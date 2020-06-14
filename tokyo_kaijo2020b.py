a, v = map(int, input().split())
b, w = map(int, input().split())
t = int(input())
if v <= w:
  print("NO")
elif a <= b:
  if a+v*t >= b+w*t:
    print("YES")
  else:
    print("NO")
else:
  if a-v*t <= b-w*t:
    print("YES")
  else:
    print("NO")
