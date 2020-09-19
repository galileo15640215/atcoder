n = int(input())
flag = True
cnt = 0
for i in range(1, n):
    for j in range(1, n):
        c = n-i*j
        if c <= 0:
            #flag = False
            break
        elif isinstance(c, int):
            cnt += 1
print(cnt)