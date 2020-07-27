t = int(input())
x = []
y = []
for m in range(t):
    p = int(input())
    q = input()
    x.append(p)
    y.append(q)
for case in range(t):
    n = x[case]
    a = y[case]
    A = 0
    B = 0
    for i in range(n):
        if a[i] == 'A':
            A += 1
        elif a[i] == 'B':
            B += 1
    if abs(A-B) < 3:
        ans = 'Y'
    else:
        ans = 'N'   
    print("Case #"+str(case+1)+": "+ans)
