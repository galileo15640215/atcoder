a = int(input())
b = int(input())
c = int(input())
l = [[a], [b], [c]]
l.sort(reverse=True)
l[0].append(1)
l[1].append(2)
l[2].append(3)
for i in range(3):
    if a == l[i][0]:
        print(l[i][1])
for i in range(3):
    if b == l[i][0]:
        print(l[i][1])
for i in range(3):
    if c == l[i][0]:
        print(l[i][1])
