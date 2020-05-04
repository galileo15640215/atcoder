n = int(input())
h = list(map(int, input().split()))
x = [0 for i in range(n)]
cnt = 0
flag = False
while True:
    id = 0
    jd = 0
    ff = False
    for i in range(n):
        if x[i] < h[i]:
            flag = True
            id = i
            jd = i
            ff = True
            for j in range(i+1, n):
                if x[j] < h[j]:
                    jd = j
                else:
                    break
        if ff:
            break
    for i in range(id, jd+1):
        x[i] += 1
    if flag:
        cnt += 1
    f = True
    for i in range(n):
        if h[i] != x[i]:
            f = False
            break
    if f:
        break
print(cnt)