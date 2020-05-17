t = int(input())
for case in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    cnt = 0
    for i in range(n-k+1):
        if a[i] == k:
            flag = True
            tmp = k
            for j in range(i, i+k):
                if a[j] == tmp:
                    tmp -= 1
                else:
                    flag = False
                    break
            if flag:
                cnt += 1
    print("Case #"+str(case+1)+": ", end='')
    print(cnt)