a, b = map(int, input().split())
flag = True
for i in range(1010):
    t1 = i*1.08
    t2 = i*1.10
    if int(t1-i) == a and int(t2-i) == b:
        print(i)
        flag = False
        break
if flag:
    print(-1)