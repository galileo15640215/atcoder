s = list(input())
q = int(input())
left = []
right = []
rev = False
for i in range(q):
    x = list(input())
    if len(x) == 1:
        rev = not rev
        #s.reverse()
    else:
        if (x[2] == "1" and not rev) or (x[2] == "2" and rev):
            left.append(x[4])
        else:
            right.append(x[4])
ans = "".join(left[::-1]) + "".join(s) + "".join(right)
if rev:
    print(ans[::-1])
else:
    print(ans)