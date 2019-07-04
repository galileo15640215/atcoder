a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
k = int(input())
 
if k >= max(b-a, c-a, d-a, e-a, c-b, d-b, e-b, d-c, e-c, e-d):
  print('Yay!')
else:
  print(':(')