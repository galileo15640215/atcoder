q = int(input())
s = 0
st = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
dic = {}
dic_out = {}
for i in range(len(st)):
    dic[st[i]] = 0
    dic_out[st[i]] = 0
l = []
for i in range(q):
    a = list(map(str, input().split()))
    if a[0] == '1':
        a[2] = int(a[2])
        s += a[2]
        dic[a[1]] = a[2]
        l.append([a[1], a[2]])
    elif a[0] == '2':
        a[1] = int(a[1])
        if s <= a[1]:
            for j in range(len(l)):
                dic_out[l[j][0]] += l[j][1]
                dic[l[j][0]] = 0
            l = []
            s = 0
        else:
            cnt = 0
            for j in range(len(l)):
                id = j
                if cnt + l[j][1] <= a[1]:
                    cnt += l[j][1]
                    dic[l[j][0]] -= l[j][1]
                    dic_out[l[j][0]] += l[j][1]
                else:
                    dic[l[j][0]] -= a[1]-cnt
                    dic_out[l[j][0]] += a[1]-cnt
                    break
            l = l[id-1:len(l)]
            l[0][1] -= a[1]-cnt
            s -= a[1]
        out = 0
        for j in dic_out.keys():
            out += dic_out[j]**2
            dic_out[j] = 0
        print(out)