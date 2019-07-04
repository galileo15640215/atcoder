a, b, c, d = list(input())
a, b, c, d = int(a), int(b), int(c), int(d)
if a+b+c+d == 7:
  print(str(a)+'+'+str(b)+'+'+str(c)+'+'+str(d)+'=7')
elif a+b+c-d == 7:
  print(str(a)+'+'+str(b)+'+'+str(c)+'-'+str(d)+'=7')
elif a+b-c+d == 7:
  print(str(a)+'+'+str(b)+'-'+str(c)+'+'+str(d)+'=7')
elif a+b-c-d == 7:
  print(str(a)+'+'+str(b)+'-'+str(c)+'-'-str(d)+'=7')
elif a-b+c+d == 7:
  print(str(a)+'-'+str(b)+'+'+str(c)+'+'+str(d)+'=7')
elif a-b+c-d == 7:
  print(str(a)+'-'+str(b)+'+'+str(c)+'-'-str(d)+'=7')
elif a-b-c+d == 7:
  print(str(a)+'-'+str(b)+'-'+str(c)+'+'+str(d)+'=7')
elif a-b-c-d == 7:
  print(str(a)+'-'+str(b)+'-'+str(c)+'-'-str(d)+'=7')