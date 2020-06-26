f = open('b1.in')
a = list(f.read().split())
f.close()
n = int(a.pop(0))
b = []
for i in range(n):
    b.append(int(a[i]))
b.sort()
f = open('out2.txt','w')
for i in range(n):
    f.write(str(b[i]) + ' ')
f.close()