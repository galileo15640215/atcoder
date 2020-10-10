x,y = 0,0
s = str(input())
t = int(input())
q = 0
for moji in s:
    if moji =='L':
        x -= 1
    elif moji == 'R':
        x += 1
    elif moji == 'U':
        y += 1
    elif moji == 'D':
        y -= 1
    else:
        q += 1
#print(abs(x)+abs(y))
if t == 1:
    print(abs(x)+abs(y)+q)
else:
    if abs(x)+abs(y) >= q:
        print(abs(x)+abs(y)-q)
    else:
        tmp = abs(abs(x)+abs(y)-q)
        print(tmp%2)