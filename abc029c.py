n = int(input())
l = ['a', 'b', 'c']
sub = l
for i in range(n-1):
    for j in range(len(sub)):
        tmp = ''.join(sub[j])
        for k in range(3):
            sub.append(tmp+l[k])
for i in range(len(sub)):
    if len(sub[i]) == n:
        print(sub[i])