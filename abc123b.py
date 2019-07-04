a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
 
num = []
num.append(a%10)
num.append(b%10)
num.append(c%10)
num.append(d%10)
num.append(e%10)
 
cnt = 0
for i in range(len(num)):
  if num[i] == 0:
    cnt += 1
ans = min(num)
x = 10
if min(num) == 0:
  if 9 in num:
    x = 9
    if 8 in num:
      x = 8
      if 7 in num:
        x = 7
        if 6 in num:
          x = 6
          if 5 in num:
            x = 5
            if 4 in num:
              x = 4
              if 3 in num:
                x = 3
                if 2 in num:
                  x = 2
                  if 1 in num:
                    x = 1
  sum = a+(10-a%10) + b+(10-b%10) + c+(10-c%10) + d+(10-d%10) + e+(10-e%10)-10-10*cnt+x
else:  
  sum = a+(10-a%10) + b+(10-b%10) + c+(10-c%10) + d+(10-d%10) + e+(10-e%10)-10-10*cnt+ans
print(sum)