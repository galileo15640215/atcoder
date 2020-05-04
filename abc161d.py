k = int(input())
l = []
for i in range(1, 10):
    l.append(i)
judge = l
for d in range(1, 10):
    tmp = []
    for i in range(len(judge)):
        val = judge[i]
        for j in range(-1, 2):
            add = val%10 + j
            if add >= 0 and add <= 9:
                tmp.append(val*10 + add)
    for i in range(len(tmp)):
        l.append(tmp[i])
    judge = tmp
print(l[k-1])