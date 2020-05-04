a, b, x = map(int, input().split())
n = 100000000
right = n
left = 0
flag = False
if x >= a*n + b*len(str(n)):
    ans = n
    flag = True
else:
    pre = n
    while True:
        #print(left, right)
        n = (left+right)//2
        if x >= a*n + b*len(str(n)):
            left = n
        else:
            right = n
        if left == right:
            ans = right
            flag = True
            break        
        if pre == n:
            flag = True
            ans = right
            break
        pre = n
if flag:
    print(ans)
else:
    print(0)