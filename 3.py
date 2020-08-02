k = int(input())
if int(str(k)[0])%2 == 0 or k%2 == 0:
    print(-1)
else:
    s = 7
    cnt = 1
    while k < 7:
        s = s*10+7
        cnt += 1
    tmp = k
    pre = 1
    for i in range(10):
        if str(tmp)[0] == '7':
            break
        pre += 1
        tmp += k
    print(tmp)
    print(pre)
    while True:
        chk = str(tmp)
        flag = True
        for i in range(len(chk)):
            if chk[i] != '7':
                flag = False
                break
        if flag:
            print(tmp)
            print(len(chk))
            break
        print(tmp)
        tmp = tmp*10 + k*pre
        cnt += pre+1