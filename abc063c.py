n = int(input())
a = []
b = []
for i in range(n):
    s = int(input())
    if s%10 == 0:
        b.append(s)
    else:
        a.append(s)
a.sort()
b.sort()
if a:
    if sum(a)%10 == 0:
        print(sum(a)-a[0]+sum(b))
    else:
        print(sum(a)+sum(b))        
else:
    print(0)